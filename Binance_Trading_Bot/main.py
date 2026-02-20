"""
BUY  logic : price is within [BUY_THRESHOLD - BUY_RANGE, BUY_THRESHOLD]
SELL logic : price is >= SELL_THRESHOLD  (sell as high as possible)

Configure via environment variables:
    $env:BOT_SYMBOL="BTCUSDT"
    $env:BOT_BUY_THRESHOLD="67800"   # upper bound of buy zone
    $env:BOT_BUY_RANGE="100"         # how far below threshold to trigger buy
    $env:BOT_SELL_THRESHOLD="67900"  # price at or above which we sell
    $env:BOT_QUANTITY="0.002"
    $env:BOT_POLL_INTERVAL="3"

Example with the above settings:
    BUY  zone : 67700 <= price <= 67800   (67800 - 100 to 67800)
    SELL zone : price >= 67900

Run:
    python main.py

Stop:
    Ctrl+C
"""

import os
import time

from bot.client import BinanceFuturesClient
from bot.orders import place_market_order
from bot.logging_config import setup_logger

logger = setup_logger("main")

SYMBOL         = os.environ.get("BOT_SYMBOL", "BTCUSDT")
BUY_THRESHOLD  = float(os.environ.get("BOT_BUY_THRESHOLD", "67800"))
BUY_RANGE      = float(os.environ.get("BOT_BUY_RANGE", "100"))
SELL_THRESHOLD = float(os.environ.get("BOT_SELL_THRESHOLD", "67900"))
TRADE_QUANTITY = float(os.environ.get("BOT_QUANTITY", "0.002"))
POLL_INTERVAL  = int(os.environ.get("BOT_POLL_INTERVAL", "3"))

BUY_LOWER = BUY_THRESHOLD - BUY_RANGE   # lower bound of buy zone


def trading_bot(client: BinanceFuturesClient):
    logger.info(
        "Bot started | symbol=%s | buy_zone=[%.2f-%.2f] | sell_at>=%.2f | qty=%s | interval=%ss",
        SYMBOL, BUY_LOWER, BUY_THRESHOLD, SELL_THRESHOLD, TRADE_QUANTITY, POLL_INTERVAL,
    )
    print(f"\n{'='*57}")
    print(f"  🤖  Trading Bot Started  (Range Mode)")
    print(f"{'='*57}")
    print(f"  Symbol         : {SYMBOL}")
    print(f"  Buy  zone      : {BUY_LOWER:,.2f}  to  {BUY_THRESHOLD:,.2f}  (range: {BUY_RANGE})")
    print(f"  Sell at / above: {SELL_THRESHOLD:,.2f}")
    print(f"  Quantity       : {TRADE_QUANTITY}")
    print(f"  Poll interval  : {POLL_INTERVAL}s")
    print(f"  Press Ctrl+C to stop")
    print(f"{'='*57}\n")

    while True:
        try:
            price = client.get_mark_price(SYMBOL)
            position = client.get_position(SYMBOL)
            in_position = position is not None

            # Determine zone label for display
            if BUY_LOWER <= price <= BUY_THRESHOLD:
                zone = "🟢 BUY ZONE"
            elif price >= SELL_THRESHOLD:
                zone = "🔴 SELL ZONE"
            else:
                zone = "⚪ WAITING"

            status = "IN POSITION" if in_position else "FLAT"
            print(f"  Price: {price:>12,.2f}  |  {status:12s}  |  {zone}")
            logger.info("Price=%.2f | in_position=%s | zone=%s", price, in_position, zone)

            # ── BUY logic ──────────────────────────────────────────────
            if not in_position and BUY_LOWER <= price <= BUY_THRESHOLD:
                print(f"\n  📈  BUY signal! Price {price:,.2f} is in buy zone [{BUY_LOWER:,.2f} – {BUY_THRESHOLD:,.2f}]")
                logger.info("BUY signal | price=%.2f | buy_zone=[%.2f-%.2f]", price, BUY_LOWER, BUY_THRESHOLD)
                result = place_market_order(client, SYMBOL, "BUY", TRADE_QUANTITY)
                print(f"  ✅  Bought! orderId={result['orderId']}  @ ~{price:,.2f}\n")
                time.sleep(2)

            # ── SELL logic ─────────────────────────────────────────────
            elif in_position and price >= SELL_THRESHOLD:
                print(f"\n  📉  SELL signal! Price {price:,.2f} >= sell threshold {SELL_THRESHOLD:,.2f}")
                logger.info("SELL signal | price=%.2f | sell_threshold=%.2f", price, SELL_THRESHOLD)
                result = place_market_order(client, SYMBOL, "SELL", TRADE_QUANTITY, reduce_only=True)
                print(f"  ✅  Sold!   orderId={result['orderId']}  @ ~{price:,.2f}\n")
                time.sleep(2)

        except KeyboardInterrupt:
            print("\n\n  🛑  Bot stopped by user.\n")
            logger.info("Bot stopped by user")
            break

        except Exception as exc:
            logger.error("Bot loop error: %s", exc, exc_info=True)
            print(f"  ⚠️  Error: {exc} — retrying in {POLL_INTERVAL}s...")

        time.sleep(POLL_INTERVAL)


if __name__ == "__main__":
    try:
        client = BinanceFuturesClient()
        trading_bot(client)
    except EnvironmentError as e:
        print(f"\n❌  {e}\n")
        raise SystemExit(1)