
# Import necessary libraries
import requests

def fetch_news(api_key='YOUR_NEWS_API_KEY'):
    """
    Fetch news data using the News API.
    """
    url = f'https://newsapi.org/v2/everything?q=stocks&apiKey={api_key}'
    response = requests.get(url)
    news_data = response.json()['articles']
    
    return news_data

# Example usage
# news = fetch_news()
