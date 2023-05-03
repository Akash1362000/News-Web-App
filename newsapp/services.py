from django.conf import settings
from newsapi import NewsApiClient


def get_news(country: str, category: str):
    newsapi = NewsApiClient(api_key=settings.NEWS_API_KEY)
    top_headlines = newsapi.get_top_headlines(
        country=country,
        category=category,
    )

    top_articles = top_headlines["articles"]
    description = []
    title = []
    image = []
    url = []

    for article in range(len(top_articles)):
        f = top_articles[article]
        title.append(f["title"])
        description.append(f["description"])
        image.append(f["urlToImage"])
        url.append(f["url"])
    return zip(title, description, image, url)
