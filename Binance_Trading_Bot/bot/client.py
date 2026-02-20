"""
Direct REST client for Binance Futures Testnet.

WHY NOT python-binance's built-in testnet support?
  - python-binance's `testnet=True` targets the *Spot* testnet (testnet.binance.vision).
  - The Futures Testnet (testnet.binancefuture.com) is a completely separate system.
  - The library's `_request_futures_api` ignores `FUTURES_URL` overrides for signed
    requests, regenerating the URL from internal state — causing -1022 signature errors.

SOLUTION: Use `requests` directly against the Futures Testnet base URL.
  HMAC-SHA256 signing is standard and straightforward to implement manually.
"""

import hashlib
import hmac
import os
import time
from urllib.parse import urlencode

import requests


class BinanceAPIException(Exception):
    # Minimal replica of binance.exceptions.BinanceAPIException — no external dependency.

    def __init__(self, response, status_code: int, text: str):
        self.status_code = status_code
        self.response = response
        try:
            import json as _json
            data = _json.loads(text)
            self.code = data.get("code", 0)
            self.message = data.get("msg", text)
        except Exception:
            self.code = 0
            self.message = text
        super().__init__(f"APIError(code={self.code}): {self.message}")



from bot.logging_config import setup_logger

logger = setup_logger("client")

BASE_URL = "https://testnet.binancefuture.com"


def _get_credentials() -> tuple[str, str]:
    api_key = os.environ.get("BINANCE_API_KEY", "")
    secret_key = os.environ.get("BINANCE_SECRET_KEY", "")
    if not api_key or not secret_key:
        raise EnvironmentError(
            "BINANCE_API_KEY and BINANCE_SECRET_KEY environment variables must be set."
        )
    return api_key, secret_key


class BinanceFuturesClient:
    # Minimal direct-REST client for Binance Futures Testnet. Signs every request with HMAC-SHA256 using timestamp + query string.


    def __init__(self):
        self.api_key, self._secret = _get_credentials()
        self.session = requests.Session()
        self.session.headers.update({
            "X-MBX-APIKEY": self.api_key,
            "Content-Type": "application/x-www-form-urlencoded",
        })
        logger.info("Binance Futures Testnet client ready. Base URL: %s", BASE_URL)

    # ------------------------------------------------------------------
    # Signing
    # ------------------------------------------------------------------

    def _sign(self, params: dict) -> str:
        """
        Build a signed query string for Binance Futures Testnet.

        CRITICAL: We return a raw query STRING (not a dict) and append the signature manually.  If we passed a dict to requests, it would
        re-encode the keys in its own order — producing a query string that differs from the one we signed, causing -1022 Signature errors.
        """
        params["timestamp"] = int(time.time() * 1000)
        query_string = urlencode(params)
        signature = hmac.new(
            self._secret.encode("utf-8"),
            query_string.encode("utf-8"),
            hashlib.sha256,
        ).hexdigest()
        return query_string + "&signature=" + signature

    # Raw HTTP helpers
    def _get(self, path: str, params: dict = None, signed: bool = False) -> dict | list:
        params = params or {}
        url = BASE_URL + path
        if signed:
            # Build full query string with signature appended — do NOT pass as dict
            query_string = self._sign(params)
            logger.debug("GET %s (signed)", url)
            resp = self.session.get(url, params=query_string)
        else:
            logger.debug("GET %s params=%s", url, params)
            resp = self.session.get(url, params=params)
        return self._handle(resp)

    def _post(self, path: str, params: dict = None) -> dict:
        params = params or {}
        url = BASE_URL + path
        # Build signed query string and send as raw body
        body = self._sign(params)
        logger.debug("POST %s (signed)", url)
        resp = self.session.post(url, data=body)
        return self._handle(resp)

    def _delete(self, path: str, params: dict = None) -> dict:
        params = params or {}
        url = BASE_URL + path
        query_string = self._sign(params)
        resp = self.session.delete(url, params=query_string)
        return self._handle(resp)

    @staticmethod
    def _handle(resp: requests.Response) -> dict | list:
        logger.debug("RESPONSE %s: %s", resp.status_code, resp.text[:500])
        if not resp.ok:
            raise BinanceAPIException(resp, resp.status_code, resp.text)
        return resp.json()
    # Market data
    def get_mark_price(self, symbol: str) -> float:
        logger.debug("Fetching mark price for %s", symbol)
        data = self._get("/fapi/v1/premiumIndex", {"symbol": symbol})
        price = float(data["markPrice"])
        logger.debug("Mark price %s = %s", symbol, price)
        return price

    def get_exchange_info(self, symbol: str) -> dict:
        logger.debug("Fetching exchange info for %s", symbol)
        data = self._get("/fapi/v1/exchangeInfo")
        for s in data.get("symbols", []):
            if s["symbol"] == symbol:
                return s
        raise ValueError(f"Symbol '{symbol}' not found in exchange info.")

    # Account (signed)
    def get_account_balance(self) -> list[dict]:
        logger.debug("Fetching account balance")
        return self._get("/fapi/v2/balance", signed=True)

    def get_position(self, symbol: str) -> dict | None:
        logger.debug("Fetching position for %s", symbol)
        positions = self._get("/fapi/v2/positionRisk", {"symbol": symbol}, signed=True)
        for p in positions:
            if float(p.get("positionAmt", 0)) != 0:
                return p
        return None

    # Orders (signed)
    def create_order(self, **kwargs) -> dict:
        logger.debug("ORDER REQUEST → %s", kwargs)
        result = self._post("/fapi/v1/order", dict(kwargs))
        logger.debug("ORDER RESPONSE ← %s", result)
        return result

    def cancel_order(self, symbol: str, order_id: int) -> dict:
        logger.debug("Cancelling order %s for %s", order_id, symbol)
        return self._delete("/fapi/v1/order", {"symbol": symbol, "orderId": order_id})

    def get_open_orders(self, symbol: str) -> list[dict]:
        return self._get("/fapi/v1/openOrders", {"symbol": symbol}, signed=True)