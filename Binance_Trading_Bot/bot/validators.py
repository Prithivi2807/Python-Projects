"""
Validates all user-supplied inputs BEFORE they reach the Binance API.
Raises ValueError with a clear message on failure.
"""

VALID_SIDES = {"BUY", "SELL"}
VALID_ORDER_TYPES = {"MARKET", "LIMIT", "STOP_MARKET", "STOP_LIMIT"}


def validate_symbol(symbol: str) -> str:

    # Ensure symbol is a non-empty uppercase string (e.g. BTCUSDT).
    symbol = symbol.strip().upper()
    if not symbol or not symbol.isalpha():
        raise ValueError(
            f"Invalid symbol '{symbol}'. Expected an alphabetic string like BTCUSDT."
        )
    return symbol


def validate_side(side: str) -> str:
    # Ensure side is BUY or SELL (case-insensitive).
    side = side.strip().upper()
    if side not in VALID_SIDES:
        raise ValueError(
            f"Invalid side '{side}'. Must be one of: {', '.join(VALID_SIDES)}."
        )
    return side


def validate_order_type(order_type: str) -> str:
    # Ensure order type is supported.
    order_type = order_type.strip().upper()
    if order_type not in VALID_ORDER_TYPES:
        raise ValueError(
            f"Invalid order type '{order_type}'. "
            f"Must be one of: {', '.join(VALID_ORDER_TYPES)}."
        )
    return order_type


def validate_quantity(quantity: str | float) -> float:
    # Ensure quantity is a positive float.
    try:
        qty = float(quantity)
    except (ValueError, TypeError):
        raise ValueError(f"Invalid quantity '{quantity}'. Must be a positive number.")
    if qty <= 0:
        raise ValueError(f"Quantity must be greater than 0. Got: {qty}")
    return qty


def validate_price(price: str | float | None, order_type: str) -> float | None:
    # Price is required for LIMIT and STOP_LIMIT orders; ignored for MARKET/STOP_MARKET.
    if order_type in {"LIMIT", "STOP_LIMIT"}:
        if price is None:
            raise ValueError(f"Price is required for {order_type} orders.")
        try:
            p = float(price)
        except (ValueError, TypeError):
            raise ValueError(f"Invalid price '{price}'. Must be a positive number.")
        if p <= 0:
            raise ValueError(f"Price must be greater than 0. Got: {p}")
        return p
    return None  # not needed for MARKET orders


def validate_stop_price(stop_price: str | float | None, order_type: str) -> float | None:
    # Stop price is required for STOP_LIMIT orders.
    if order_type == "STOP_LIMIT":
        if stop_price is None:
            raise ValueError("Stop price is required for STOP_LIMIT orders.")
        try:
            sp = float(stop_price)
        except (ValueError, TypeError):
            raise ValueError(f"Invalid stop price '{stop_price}'. Must be a positive number.")
        if sp <= 0:
            raise ValueError(f"Stop price must be > 0. Got: {sp}")
        return sp
    return None


def validate_all(
    symbol: str,
    side: str,
    order_type: str,
    quantity: str | float,
    price: str | float | None = None,
    stop_price: str | float | None = None,
) -> dict:
    # Run all validations and return a clean dict of validated values. Raises ValueError on the first failure encountered.
    sym = validate_symbol(symbol)
    s = validate_side(side)
    ot = validate_order_type(order_type)
    qty = validate_quantity(quantity)
    p = validate_price(price, ot)
    sp = validate_stop_price(stop_price, ot)

    return {
        "symbol": sym,
        "side": s,
        "order_type": ot,
        "quantity": qty,
        "price": p,
        "stop_price": sp,
    }
