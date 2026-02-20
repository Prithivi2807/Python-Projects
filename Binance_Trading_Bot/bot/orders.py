# High-level order placement logic. Calls BinanceFuturesClient and applies business rules (minimum notional, precision rounding, response formatting).

import math
from bot.client import BinanceFuturesClient
from bot.logging_config import setup_logger

logger = setup_logger("orders")

MINIMUM_NOTIONAL_USDT = 100.0  # Binance Futures minimum


# Internal helpers

def _round_to_step(value: float, step: float) -> float:
    """Round a value DOWN to the nearest multiple of step."""
    precision = int(round(-math.log10(step))) if step < 1 else 0
    return round(math.floor(value / step) * step, precision)


def _get_lot_size_filter(exchange_info: dict) -> dict:
    """Extract LOT_SIZE filter from exchange info."""
    for f in exchange_info.get("filters", []):
        if f["filterType"] == "LOT_SIZE":
            return f
    return {}


def _get_price_filter(exchange_info: dict) -> dict:
    """Extract PRICE_FILTER from exchange info."""
    for f in exchange_info.get("filters", []):
        if f["filterType"] == "PRICE_FILTER":
            return f
    return {}


def _check_minimum_notional(quantity: float, price: float, symbol: str):
    """Raise ValueError if order value is below minimum notional."""
    notional = quantity * price
    if notional < MINIMUM_NOTIONAL_USDT:
        raise ValueError(
            f"Order notional {notional:.2f} USDT is below the minimum "
            f"{MINIMUM_NOTIONAL_USDT} USDT for {symbol}."
        )


def _format_response(order: dict) -> dict:
    """Return a clean, human-readable summary of an order response."""
    return {
        "orderId": order.get("orderId"),
        "symbol": order.get("symbol"),
        "side": order.get("side"),
        "type": order.get("type"),
        "status": order.get("status"),
        "origQty": order.get("origQty"),
        "executedQty": order.get("executedQty"),
        "avgPrice": order.get("avgPrice", "N/A"),
        "price": order.get("price", "N/A"),
        "stopPrice": order.get("stopPrice", "N/A"),
        "timeInForce": order.get("timeInForce", "N/A"),
        "updateTime": order.get("updateTime"),
    }


# Public order functions

def place_market_order(
    client: BinanceFuturesClient,
    symbol: str,
    side: str,
    quantity: float,
    reduce_only: bool = False,
) -> dict:
    """
    Place a MARKET order on Binance Futures.

    Args:
        client:      BinanceFuturesClient instance
        symbol:      e.g. 'BTCUSDT'
        side:        'BUY' or 'SELL'
        quantity:    number of contracts
        reduce_only: True to close an existing position only

    Returns:
        Formatted order response dict.
    """
    logger.info(
        "Placing MARKET %s order | %s | qty=%s | reduceOnly=%s",
        side, symbol, quantity, reduce_only,
    )

    # Validate & adjust quantity against exchange LOT_SIZE
    info = client.get_exchange_info(symbol)
    lot = _get_lot_size_filter(info)
    if lot:
        step = float(lot.get("stepSize", 0.001))
        quantity = _round_to_step(quantity, step)
        logger.debug("Quantity after step-size rounding: %s", quantity)

    # Minimum notional check
    mark_price = client.get_mark_price(symbol)
    _check_minimum_notional(quantity, mark_price, symbol)

    params: dict = {
        "symbol": symbol,
        "side": side,
        "type": "MARKET",
        "quantity": quantity,
    }
    if reduce_only:
        params["reduceOnly"] = True

    raw = client.create_order(**params)
    summary = _format_response(raw)
    logger.info("MARKET order SUCCESS: %s", summary)
    return summary


def place_limit_order(
    client: BinanceFuturesClient,
    symbol: str,
    side: str,
    quantity: float,
    price: float,
    time_in_force: str = "GTC",
    reduce_only: bool = False,
) -> dict:
    """
    Place a LIMIT order on Binance Futures.

    Args:
        client:        BinanceFuturesClient instance
        symbol:        e.g. 'BTCUSDT'
        side:          'BUY' or 'SELL'
        quantity:      number of contracts
        price:         limit price
        time_in_force: GTC (default) | IOC | FOK
        reduce_only:   True to close an existing position only

    Returns:
        Formatted order response dict.
    """
    logger.info(
        "Placing LIMIT %s order | %s | qty=%s | price=%s | TIF=%s",
        side, symbol, quantity, price, time_in_force,
    )

    info = client.get_exchange_info(symbol)

    # Round quantity
    lot = _get_lot_size_filter(info)
    if lot:
        step = float(lot.get("stepSize", 0.001))
        quantity = _round_to_step(quantity, step)

    # Round price to tick size
    price_filter = _get_price_filter(info)
    if price_filter:
        tick = float(price_filter.get("tickSize", 0.01))
        price = _round_to_step(price, tick)

    _check_minimum_notional(quantity, price, symbol)

    params: dict = {
        "symbol": symbol,
        "side": side,
        "type": "LIMIT",
        "quantity": quantity,
        "price": price,
        "timeInForce": time_in_force,
    }
    if reduce_only:
        params["reduceOnly"] = True

    raw = client.create_order(**params)
    summary = _format_response(raw)
    logger.info("LIMIT order SUCCESS: %s", summary)
    return summary


def place_stop_limit_order(
    client: BinanceFuturesClient,
    symbol: str,
    side: str,
    quantity: float,
    price: float,
    stop_price: float,
    time_in_force: str = "GTC",
) -> dict:
    """
    Place a STOP_LIMIT order — triggers at stop_price, executes at price.

    Returns:
        Formatted order response dict.
    """
    logger.info(
        "Placing STOP_LIMIT %s order | %s | qty=%s | price=%s | stopPrice=%s",
        side, symbol, quantity, price, stop_price,
    )

    info = client.get_exchange_info(symbol)

    lot = _get_lot_size_filter(info)
    if lot:
        step = float(lot.get("stepSize", 0.001))
        quantity = _round_to_step(quantity, step)

    price_filter = _get_price_filter(info)
    if price_filter:
        tick = float(price_filter.get("tickSize", 0.01))
        price = _round_to_step(price, tick)
        stop_price = _round_to_step(stop_price, tick)

    _check_minimum_notional(quantity, price, symbol)

    params: dict = {
        "symbol": symbol,
        "side": side,
        "type": "STOP",            # Binance Futures uses "STOP" for stop-limit
        "quantity": quantity,
        "price": price,
        "stopPrice": stop_price,
        "timeInForce": time_in_force,
    }

    raw = client.create_order(**params)
    summary = _format_response(raw)
    logger.info("STOP_LIMIT order SUCCESS: %s", summary)
    return summary


def dispatch_order(client: BinanceFuturesClient, validated: dict) -> dict:
    """
    Route a validated order dict to the correct placement function.
    Used by the CLI to avoid a long if/elif chain.
    """
    ot = validated["order_type"]
    if ot == "MARKET":
        return place_market_order(
            client,
            symbol=validated["symbol"],
            side=validated["side"],
            quantity=validated["quantity"],
        )
    elif ot == "LIMIT":
        return place_limit_order(
            client,
            symbol=validated["symbol"],
            side=validated["side"],
            quantity=validated["quantity"],
            price=validated["price"],
        )
    elif ot == "STOP_LIMIT":
        return place_stop_limit_order(
            client,
            symbol=validated["symbol"],
            side=validated["side"],
            quantity=validated["quantity"],
            price=validated["price"],
            stop_price=validated["stop_price"],
        )
    else:
        raise ValueError(f"Unsupported order type: {ot}")
