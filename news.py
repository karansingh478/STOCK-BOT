from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key="2af083ea93a8450493dd318e04eca3a9")

def get_news(company):
    articles = newsapi.get_everything(
        q=company,
        language="en",
        sort_by="publishedAt",
        page_size=5
    )

    news_list = []

    for article in articles["articles"]:
        title = article["title"]
        url = article["url"]
        source = article["source"]["name"]

        # Sentiment
        sentiment = "Neutral"
        if any(word in title.lower() for word in ["gain", "rise", "profit", "up"]):
            sentiment = "Positive 📈"
        elif any(word in title.lower() for word in ["fall", "loss", "down", "crash"]):
            sentiment = "Negative 📉"

        # ✅ MUST RETURN 4 VALUES
        news_list.append((title, url, source, sentiment))

    return news_list