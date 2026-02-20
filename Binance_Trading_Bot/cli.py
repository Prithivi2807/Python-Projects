"""
Command-line interface for the Binance Futures Trading Bot.
Parses user arguments, validates them, and dispatches orders.

Usage examples:
    # Market BUY
    python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002

    # Limit SELL
    python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.002 --price 68000

    # Stop-Limit BUY
    python cli.py --symbol BTCUSDT --side BUY --type STOP_LIMIT --quantity 0.002 \
                  --price 67000 --stop-price 67500

    # Check account balance
    python cli.py --balance

    # Check open position
    python cli.py --position --symbol BTCUSDT
"""

import argparse
import json
import sys

from bot.client import BinanceFuturesClient
from bot.orders import dispatch_order
from bot.validators import validate_all
from bot.logging_config import setup_logger

logger = setup_logger("cli")

# Argument parser

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="trading_bot",
        description="Binance Futures Testnet Trading Bot",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )

    # --- Order arguments ---
    order_group = parser.add_argument_group("Order options")
    order_group.add_argument(
        "--symbol", "-s",
        type=str,
        help="Trading pair symbol, e.g. BTCUSDT",
    )
    order_group.add_argument(
        "--side",
        type=str,
        choices=["BUY", "SELL"],
        help="Order side: BUY or SELL",
    )
    order_group.add_argument(
        "--type", "-t",
        dest="order_type",
        type=str,
        choices=["MARKET", "LIMIT", "STOP_LIMIT"],
        help="Order type",
    )
    order_group.add_argument(
        "--quantity", "-q",
        type=float,
        help="Order quantity in base asset (e.g. 0.002 BTC)",
    )
    order_group.add_argument(
        "--price", "-p",
        type=float,
        default=None,
        help="Limit price (required for LIMIT and STOP_LIMIT orders)",
    )
    order_group.add_argument(
        "--stop-price",
        type=float,
        default=None,
        dest="stop_price",
        help="Stop trigger price (required for STOP_LIMIT orders)",
    )

    # --- Utility arguments ---
    util_group = parser.add_argument_group("Utility options")
    util_group.add_argument(
        "--balance",
        action="store_true",
        help="Print account balance and exit",
    )
    util_group.add_argument(
        "--position",
        action="store_true",
        help="Print current position for --symbol and exit",
    )
    util_group.add_argument(
        "--open-orders",
        action="store_true",
        help="List open orders for --symbol and exit",
    )
    util_group.add_argument(
        "--price-only",
        action="store_true",
        help="Print current mark price for --symbol and exit",
    )

    return parser

# Pretty printers
def _print_banner(title: str):
    print("\n" + "=" * 55)
    print(f"  {title}")
    print("=" * 55)


def _print_json(data):
    print(json.dumps(data, indent=2, default=str))


def _print_order_summary(validated: dict):
    _print_banner("ORDER REQUEST SUMMARY")
    print(f"  Symbol    : {validated['symbol']}")
    print(f"  Side      : {validated['side']}")
    print(f"  Type      : {validated['order_type']}")
    print(f"  Quantity  : {validated['quantity']}")
    if validated.get("price"):
        print(f"  Price     : {validated['price']}")
    if validated.get("stop_price"):
        print(f"  Stop Price: {validated['stop_price']}")
    print("=" * 55)


def _print_order_result(result: dict):
    _print_banner("ORDER RESPONSE")
    print(f"  Order ID    : {result.get('orderId')}")
    print(f"  Status      : {result.get('status')}")
    print(f"  Executed Qty: {result.get('executedQty')}")
    print(f"  Avg Price   : {result.get('avgPrice', 'N/A')}")
    print(f"  Limit Price : {result.get('price', 'N/A')}")
    print(f"  Stop Price  : {result.get('stopPrice', 'N/A')}")
    print("=" * 55)
    print("  ✅  Order placed successfully!")
    print("=" * 55 + "\n")


# Utility handlers
def handle_balance(client: BinanceFuturesClient):
    _print_banner("ACCOUNT BALANCE")
    balances = client.get_account_balance()
    for b in balances:
        if float(b.get("balance", 0)) > 0:
            print(f"  {b['asset']}: {b['balance']} (available: {b['availableBalance']})")
    print("=" * 55 + "\n")


def handle_position(client: BinanceFuturesClient, symbol: str):
    _print_banner(f"OPEN POSITION — {symbol}")
    position = client.get_position(symbol)
    if position:
        _print_json(position)
    else:
        print(f"  No open position for {symbol}.")
    print("=" * 55 + "\n")


def handle_open_orders(client: BinanceFuturesClient, symbol: str):
    _print_banner(f"OPEN ORDERS — {symbol}")
    orders = client.get_open_orders(symbol)
    if orders:
        _print_json(orders)
    else:
        print(f"  No open orders for {symbol}.")
    print("=" * 55 + "\n")


def handle_price(client: BinanceFuturesClient, symbol: str):
    price = client.get_mark_price(symbol)
    print(f"\n  Mark Price [{symbol}]: {price} USDT\n")


# Main entrypoint
def main():
    parser = build_parser()
    args = parser.parse_args()

    logger.info("CLI invoked with args: %s", vars(args))

    # Initialise client (reads env vars)
    try:
        client = BinanceFuturesClient()
    except EnvironmentError as exc:
        print(f"\n❌  Configuration error: {exc}\n")
        logger.critical("Client init failed: %s", exc)
        sys.exit(1)

    # --- Utility commands (no order needed) ---

    if args.balance:
        handle_balance(client)
        sys.exit(0)

    if args.position:
        if not args.symbol:
            print("❌  --symbol is required for --position")
            sys.exit(1)
        handle_position(client, args.symbol.upper())
        sys.exit(0)

    if args.open_orders:
        if not args.symbol:
            print("❌  --symbol is required for --open-orders")
            sys.exit(1)
        handle_open_orders(client, args.symbol.upper())
        sys.exit(0)

    if args.price_only:
        if not args.symbol:
            print("❌  --symbol is required for --price-only")
            sys.exit(1)
        handle_price(client, args.symbol.upper())
        sys.exit(0)

    #Order flow

    # Check all required order args are present
    missing = [
        f for f, v in [
            ("--symbol", args.symbol),
            ("--side", args.side),
            ("--type", args.order_type),
            ("--quantity", args.quantity),
        ]
        if v is None
    ]
    if missing:
        print(f"\n❌  Missing required argument(s): {', '.join(missing)}\n")
        parser.print_help()
        sys.exit(1)

    # Validate inputs
    try:
        validated = validate_all(
            symbol=args.symbol,
            side=args.side,
            order_type=args.order_type,
            quantity=args.quantity,
            price=args.price,
            stop_price=args.stop_price,
        )
    except ValueError as exc:
        print(f"\n❌  Validation error: {exc}\n")
        logger.warning("Validation failed: %s", exc)
        sys.exit(1)

    # Print request summary
    _print_order_summary(validated)

    # Place order
    try:
        result = dispatch_order(client, validated)
    except Exception as exc:
        print(f"\n❌  Order failed: {exc}\n")
        logger.error("Order placement failed: %s", exc)
        sys.exit(1)

    # Print result
    _print_order_result(result)


if __name__ == "__main__":
    main()
