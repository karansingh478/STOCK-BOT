# 📈 AI Financial Stock Assistant

A **Streamlit-based stock market assistant** that provides real-time stock data, basic financial insights, and interactive visualizations using Python.

---

## 🚀 Features

### 📊 Stock Market Charts
- Candlestick charts using Plotly  
- Moving averages (MA20, MA50, MA200)  
- Volume visualization  
- Data fetched using Yahoo Finance (yfinance)  

---

### 💬 Chatbot (Rule-Based)
- Answers predefined stock-related queries  
- Supports queries like:
  - `price of TCS`
  - `what is SIP`
  - `what is NIFTY 50`
- Uses keyword matching (not AI/LLM-based)

---

### 💰 Investment Simulator
- Calculates future value using compound interest  
- Helps users understand basic investment growth  

---

### 📰 News + Sentiment Analysis
- Fetches latest news using NewsAPI  
- Performs simple sentiment analysis using TextBlob  
- Displays:
  - Title  
  - Source  
  - Sentiment (Positive / Negative / Neutral)  

---

### 🌍 Stock Support
- Indian Stocks (NSE): `TCS`, `RELIANCE`  
- Global Stocks: `AAPL`, `TSLA`  
- Indices: `^NSEI` (NIFTY 50)  

---

## ⚠️ Limitations

- Chatbot is **not AI-powered** (rule-based only)  
- No real-time streaming (data is delayed from API)  
- Limited understanding of complex queries  
- News depends on external API key  
- Not intended for real financial decision-making  

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit  
- **Backend:** Python  
- **Stock Data:** yfinance  
- **Charts:** Plotly  
- **Data Handling:** Pandas  
- **News API:** NewsAPI  
- **Sentiment Analysis:** TextBlob  

---

## 📸 Preview
<img width="1867" height="708" alt="image" src="https://github.com/user-attachments/assets/31a49a1a-af14-40dc-bb6b-ff188c4eb8ca" />

<img width="1013" height="737" alt="image" src="https://github.com/user-attachments/assets/b4337695-7dba-4c33-a7dd-ffd2bc1234c0" />

<img width="1810" height="768" alt="image" src="https://github.com/user-attachments/assets/5df7a15c-af47-47ba-a65c-1e140c06d6d8" />

<img width="810" height="575" alt="image" src="https://github.com/user-attachments/assets/6ccc25ba-7184-4ecf-9254-2f38a8d5962a" />

<img width="1772" height="788" alt="image" src="https://github.com/user-attachments/assets/4d772a51-f6c4-43ba-8b72-c4eeb2d1bd25" />

<img width="1748" height="895" alt="image" src="https://github.com/user-attachments/assets/a0408309-bf14-4a7c-b319-c015286315a0" />

---

## ▶️ Run Locally

```bash
git clone https://github.com/your-username/STOCK-BOT.git
cd STOCK-BOT
pip install -r requirements.txt
python -m streamlit run main.py
```

---

## 📂 Project Structure

```
STOCK-BOT/
│── main.py
│── chatbot.py
│── stock_api.py
│── news.py
│── sentiment.py
│── simulator.py
│── README.md
│── requirements.txt
```

---

## 🎯 Future Improvements

- Add real AI chatbot (OpenAI / LLM)
- Improve NLP understanding
- Add portfolio tracking
- Deploy as live web app

---

## 👨‍💻 Author

Karan Singh

---

## 📜 License

MIT License
