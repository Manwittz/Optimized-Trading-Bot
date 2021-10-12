
# Import necessary libraries
import requests
import pandas as pd

def fetch_real_time_data(symbol, api_key='YOUR_ALPHA_VANTAGE_API_KEY'):
    """
    Fetch real-time stock market data using the Alpha Vantage API.
    """
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=1min&apikey={api_key}'
    response = requests.get(url)
    data = response.json()
    
    df = pd.DataFrame(data['Time Series (1min)']).T
    df = df.rename(columns={'1. open': 'Open', '2. high': 'High', '3. low': 'Low', '4. close': 'Close', '5. volume': 'Volume'})
    
    return df

# Example usage
# real_time_data = fetch_real_time_data('AAPL')
