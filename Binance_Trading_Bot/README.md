# Binance Futures Testnet Trading Bot

A production-grade Python CLI trading bot for Binance Futures Testnet (USDT-M).

---

## Project Structure

```
trading_bot/
├── bot/
│   ├── __init__.py
│   ├── client.py          # Direct REST client with HMAC-SHA256 signing
│   ├── orders.py          # Order placement logic (MARKET, LIMIT, STOP_LIMIT)
│   ├── validators.py      # Input validation (symbol, side, type, qty, price)
│   └── logging_config.py  # Rotating file + console logger
├── cli.py                 # CLI entry point (argparse)
├── main.py                # Automated threshold bot loop
├── requirements.txt
├── README.md
└── logs/
    └── trading_bot.log    # Full session log (auto-created)
```

---

## Setup

### 1. Clone / unzip the project

```bash
cd trading_bot
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # Linux / macOS
venv\Scripts\activate           # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set API credentials as environment variables

**Never hard-code keys in source files.**

```bash
# Linux / macOS
export BINANCE_API_KEY="your_testnet_api_key"
export BINANCE_SECRET_KEY="your_testnet_secret_key"

# Windows (PowerShell)
$env:BINANCE_API_KEY="your_testnet_api_key"
$env:BINANCE_SECRET_KEY="your_testnet_secret_key"
```

Generate testnet credentials at: https://testnet.binancefuture.com → API Management → Generate Key

---

## CLI Usage

```bash
python cli.py [options]
```

### Place a MARKET order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002
python cli.py --symbol BTCUSDT --side SELL --type MARKET --quantity 0.002
```

**Sample output:**
```
=======================================================
  ORDER REQUEST SUMMARY
=======================================================
  Symbol    : BTCUSDT
  Side      : BUY
  Type      : MARKET
  Quantity  : 0.002
=======================================================
  Order ID    : 12409028771
  Status      : NEW
  Executed Qty: 0.002
=======================================================
  ✅  Order placed successfully!
=======================================================
```

### Place a LIMIT order

```bash
python cli.py --symbol BTCUSDT --side BUY  --type LIMIT --quantity 0.002 --price 67000
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.002 --price 69000
```

**Sample output:**
```
=======================================================
  ORDER RESPONSE
=======================================================
  Order ID    : 12409029022
  Status      : NEW
  Limit Price : 67000.00
=======================================================
  ✅  Order placed successfully!
=======================================================
```

### Place a STOP_LIMIT order (bonus)

```bash
# Triggers at 67500, fills at 67000
python cli.py --symbol BTCUSDT --side BUY --type STOP_LIMIT \
              --quantity 0.002 --price 67000 --stop-price 67500
```

### Utility commands

```bash
python cli.py --balance                          # Account balances
python cli.py --symbol BTCUSDT --price-only      # Current mark price
python cli.py --symbol BTCUSDT --position        # Open position details
python cli.py --symbol BTCUSDT --open-orders     # List open orders
```

**Sample balance output:**
```
  BTC  : 0.01000000
  USDT : 4997.75315266
  USDC : 5000.00000000
```

---

## Automated Bot Loop (main.py)

Continuously monitors price every N seconds and places MARKET orders when thresholds are crossed.

- **BUY** when price drops below `BOT_BUY_THRESHOLD` (and FLAT)
- **SELL** when price rises above `BOT_SELL_THRESHOLD` (and IN POSITION)

```bash
# Configure via environment variables
$env:BOT_SYMBOL="BTCUSDT"
$env:BOT_BUY_THRESHOLD="67600"
$env:BOT_SELL_THRESHOLD="67690"
$env:BOT_QUANTITY="0.002"
$env:BOT_POLL_INTERVAL="3"

python main.py
```

**Sample output:**
```
=======================================================
  🤖  Trading Bot Started
=======================================================
  Symbol         : BTCUSDT
  Buy  threshold : 67700.0
  Sell threshold : 67900.0
  Quantity       : 0.002
  Poll interval  : 3s
  Press Ctrl+C to stop
=======================================================

  Price:    67,875.05 USDT  |  IN POSITION
  📉  SELL signal at 67875.05 (threshold: 67500.0)
  ✅  Sold! orderId=12409147315

  Price:    67,857.49 USDT  |  FLAT
  Price:    67,872.80 USDT  |  FLAT
  Price:    67,906.80 USDT  |  FLAT
```

Stop with `Ctrl+C`.

---

## Logging

All activity is written to `logs/trading_bot.log` (rotating, 5 MB × 5 backups).  
Console shows INFO+; log file captures DEBUG level including full API request/response payloads.

```
2026-02-20 10:58:22 | DEBUG    | client | ORDER REQUEST → {'symbol': 'BTCUSDT', 'side': 'BUY', 'type': 'MARKET', 'quantity': 0.002}
2026-02-20 10:58:23 | DEBUG    | client | RESPONSE 200: {"orderId":12409028771,"symbol":"BTCUSDT","status":"NEW",...}
2026-02-20 10:58:23 | INFO     | orders | MARKET order SUCCESS: {'orderId': 12409028771, ...}
```

---

## Actual Orders Placed (Testnet Session — 20 Feb 2026)

| # | Type | Side | Qty | Price | Order ID | Status |
|---|------|------|-----|-------|----------|--------|
| 1 | MARKET | BUY | 0.002 | ~67,363 | 12409028771 | ✅ NEW |
| 2 | LIMIT | BUY | 0.002 | 67,000 | 12409029022 | ✅ NEW |
| 3 | LIMIT | SELL | 0.002 | 69,000 | 12409080105 | ✅ NEW |
| 4 | MARKET (bot) | SELL | 0.002 | ~67,902 | 12409147315 | ✅ NEW |
| 5 | MARKET (bot) | SELL | 0.002 | ~67,910 | 12409149175 | ✅ NEW |

---

## Design Notes

- **No `python-binance` library** — uses direct `requests` calls with custom HMAC-SHA256 signing to target the correct Futures Testnet URL (`https://testnet.binancefuture.com/fapi`)
- Quantity auto-adjusted to exchange `LOT_SIZE` step size
- Price auto-adjusted to exchange `PRICE_FILTER` tick size
- Minimum notional enforced: 100 USDT
- All credentials via environment variables only — never in source code
- `STOP_LIMIT` maps to Binance Futures `type=STOP` internally