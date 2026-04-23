import streamlit as st
from chatbot import reply
from simulator import future_value
from stock_api import get_history, get_details
from news import get_news
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.set_page_config(page_title="AI Stock Assistant", layout="wide")

# ---------- TITLE ----------
st.title("📈 AI Financial Stock Assistant")
st.markdown("### Smart insights for better investment decisions")

# ---------- LAYOUT ----------
col1, col2 = st.columns(2)

# ---------- CHATBOT ----------
with col1:
    st.subheader("💬 Chatbot")

    query = st.text_input("Ask something about stocks:")

    if st.button("Ask"):
        if query:
            st.success(reply(query))

# ---------- INVESTMENT ----------
with col2:
    st.subheader("💰 Investment Simulator")

    p = st.number_input("Amount (₹)", value=10000)
    r = st.number_input("Interest (%)", value=10)
    t = st.number_input("Years", value=5)

    if st.button("Calculate Investment"):
        result = future_value(p, r, t)
        st.success(f"Future Value = ₹{result}")

# ---------- STOCK CHART ----------
st.subheader("📊 Professional Stock Chart")

symbol = st.text_input("Enter stock (TCS, RELIANCE, APPLE, NIFTY 50)")

if st.button("Show Chart"):
    data = get_history(symbol)

    if data is not None and not data.empty:

        fig = make_subplots(
            rows=2, cols=1,
            shared_xaxes=True,
            row_heights=[0.75, 0.25],
            vertical_spacing=0.03
        )

        fig.add_trace(go.Candlestick(
            x=data["Date"],
            open=data["Open"],
            high=data["High"],
            low=data["Low"],
            close=data["Close"],
            increasing_line_color="#00ff88",
            decreasing_line_color="#ff4d4d"
        ), row=1, col=1)

        fig.add_trace(go.Scatter(x=data["Date"], y=data["MA20"], name="MA20"))
        fig.add_trace(go.Scatter(x=data["Date"], y=data["MA50"], name="MA50"))

        fig.add_trace(go.Bar(
            x=data["Date"],
            y=data["Volume"],
            name="Volume",
            opacity=0.3
        ), row=2, col=1)

        fig.update_layout(
            template="plotly_dark",
            height=700,
            title=f"{symbol.upper()} Chart",
            xaxis_rangeslider_visible=False
        )

        st.plotly_chart(fig, use_container_width=True)

    else:
        st.error("❌ Stock not found")

# ---------- STOCK DETAILS ----------
st.subheader("📋 Stock Details")

sym = st.text_input("Enter stock for details")

if st.button("Get Details"):
    details = get_details(sym)

    if details:
        st.write(details)
    else:
        st.error("Stock not found")

# ---------- NEWS ----------
st.subheader("📰 Latest Market News")

company = st.text_input("Enter company for news")

if st.button("Get News"):
    news = get_news(company)

    if news:
        for title, url, source, sentiment in news:

            st.markdown(f"### 📰 {title}")
            st.write(f"**Source:** {source}")

            if "Positive" in sentiment:
                st.success(sentiment)
            elif "Negative" in sentiment:
                st.error(sentiment)
            else:
                st.info(sentiment)

            st.markdown(f"[Read Full Article]({url})")
            st.divider()
    else:
        st.error("No news found")