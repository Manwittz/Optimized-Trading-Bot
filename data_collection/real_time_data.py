
# Real-time market data collection using Alpha Vantage API
from alpha_vantage.timeseries import TimeSeries

def fetch_real_time_data(symbol):
    # Replace 'YOUR_ALPHA_VANTAGE_API_KEY' with your actual Alpha Vantage API key
    api_key = 'YOUR_ALPHA_VANTAGE_API_KEY'
    ts = TimeSeries(key=api_key)
    data, meta_data = ts.get_quote_endpoint(symbol=symbol)
    return data

# News data collection using News API
import requests

def fetch_news_data(keyword):
    # Replace 'YOUR_NEWS_API_KEY' with your actual News API key
    api_key = 'YOUR_NEWS_API_KEY'
    url = f'https://newsapi.org/v2/everything?q={keyword}&apiKey={api_key}'
    response = requests.get(url)
    data = response.json()
    return data['articles']
