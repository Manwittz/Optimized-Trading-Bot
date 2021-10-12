
# Import necessary libraries
import requests
import json

def fetch_news(api_endpoint):
    """
    Fetch news data from a fictional API endpoint.
    """
    response = requests.get(api_endpoint)
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        return None

def fetch_social_media(api_endpoint):
    """
    Fetch social media data from a fictional API endpoint.
    """
    response = requests.get(api_endpoint)
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        return None

# Simulate fetching news and social media feeds
news_api_endpoint = "https://fictional-api.com/news"
social_media_api_endpoint = "https://fictional-api.com/social_media"

news_data = fetch_news(news_api_endpoint)
social_media_data = fetch_social_media(social_media_api_endpoint)

if news_data:
    print(f"Received News Data: {news_data}")

if social_media_data:
    print(f"Received Social Media Data: {social_media_data}")
