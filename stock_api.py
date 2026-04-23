import yfinance as yf

# ----------- GET STOCK PRICE -----------
def get_price(symbol):
    symbol = symbol.strip().upper()

    stock = yf.Ticker(symbol + ".NS")
    data = stock.history(period="1d")

    if data.empty:
        stock = yf.Ticker(symbol)
        data = stock.history(period="1d")

    if data.empty:
        return None

    return round(data["Close"].iloc[-1], 2)


# ----------- GET STOCK HISTORY -----------
def get_history(symbol):
    import yfinance as yf

    symbol = symbol.strip().upper()

    # Handle NIFTY
    if symbol == "NIFTY 50":
        symbol = "^NSEI"

    stock = yf.Ticker(symbol + ".NS")
    data = stock.history(period="6mo")

    if data.empty:
        stock = yf.Ticker(symbol)
        data = stock.history(period="6mo")

    if data.empty:
        return None

    # ✅ RESET INDEX PROPERLY
    data = data.reset_index()

    # ✅ ENSURE DATE COLUMN NAME
    if "Date" not in data.columns:
        data.rename(columns={data.columns[0]: "Date"}, inplace=True)

    # ✅ SORT
    data = data.sort_values("Date")

    # ✅ ADD MOVING AVERAGES (like TradingView)
    data["MA20"] = data["Close"].rolling(20).mean()
    data["MA50"] = data["Close"].rolling(50).mean()
    data["MA200"] = data["Close"].rolling(200).mean()

    return data


# ----------- GET STOCK DETAILS -----------
def get_details(symbol):
    symbol = symbol.strip().upper()

    stock = yf.Ticker(symbol + ".NS")
    data = stock.history(period="1d")

    if data.empty:
        stock = yf.Ticker(symbol)
        data = stock.history(period="1d")

    if data.empty:
        return None

    row = data.iloc[-1]

    return {
        "Open": round(row["Open"], 2),
        "High": round(row["High"], 2),
        "Low": round(row["Low"], 2),
        "Close": round(row["Close"], 2),
        "Volume": int(row["Volume"])
    }