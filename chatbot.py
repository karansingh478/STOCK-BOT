from stock_api import get_price

def reply(query):
    q = query.lower()

    words = q.replace("?", "").split()

    # ---------- DETECT STOCK ----------
    for word in words:
        if word.isalpha() and len(word) > 2:
            symbol = word.upper()
            price = get_price(symbol)

            if price:
                return (
                    f"📈 {symbol} Stock Information:\n\n"
                    f"• Current Price: ₹{price}\n"
                    f"• Market: NSE/BSE\n"
                    f"• Trend: Depends on market conditions\n\n"
                    f"💡 Tip: Always check news & fundamentals before investing."
                )

    # ---------- GENERAL QUESTIONS ----------
    if "bse" in q:
        return (
            "🏦 BSE (Bombay Stock Exchange)\n\n"
            "• Oldest stock exchange in Asia\n"
            "• Located in Mumbai\n"
            "• Index: SENSEX (Top 30 companies)\n\n"
            "Used for trading stocks in India."
        )

    if "nse" in q:
        return (
            "📊 NSE (National Stock Exchange)\n\n"
            "• Largest stock exchange in India\n"
            "• Index: NIFTY 50\n"
            "• Fully electronic trading system\n\n"
            "Most active exchange in India."
        )

    if "nifty" in q:
        return (
            "📈 NIFTY 50\n\n"
            "• Index of top 50 companies\n"
            "• Represents Indian stock market\n"
            "• Includes companies like TCS, Reliance\n\n"
            "Used to track market performance."
        )

    if "sip" in q:
        return (
            "💰 SIP (Systematic Investment Plan)\n\n"
            "• Invest small amount regularly\n"
            "• Best for beginners\n"
            "• Reduces risk over time\n\n"
            "Example: ₹1000/month in mutual fund"
        )

    if "ipo" in q:
        return (
            "🚀 IPO (Initial Public Offering)\n\n"
            "• Company sells shares to public\n"
            "• First time listing on stock market\n\n"
            "Example: LIC IPO"
        )

    if "investment" in q:
        return (
            "💡 Investment Basics\n\n"
            "• Invest in stocks, mutual funds, gold\n"
            "• Goal: grow money over time\n"
            "• Risk varies with asset\n\n"
            "Tip: Diversify your portfolio."
        )

    # ---------- DEFAULT ----------
    return (
        "🤖 I can help you with:\n\n"
        "• Stock prices → price of TCS\n"
        "• Market info → NIFTY, BSE\n"
        "• Investment → SIP, IPO\n\n"
        "Try: 'Tell me about Reliance stock'"
    )