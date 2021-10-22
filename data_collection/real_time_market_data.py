
def fetch_real_time_data(symbol, api_key='YOUR_ALPHA_VANTAGE_API_KEY'):
    """
    Fetch real-time market data for a given stock symbol using the Alpha Vantage API.
    
    Parameters:
    - symbol: Stock symbol for which data is to be fetched
    - api_key: API key for accessing the Alpha Vantage service
    
    Returns:
    - DataFrame containing the fetched market data
    """
    # Validate input parameters
    if not isinstance(symbol, str) or not symbol:
        raise ValueError("Stock symbol must be a non-empty string.")
    
    # Construct the API URL
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=1min&apikey={api_key}'
    
    # Fetch the data
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
    except requests.RequestException as e:
        raise Exception(f"Failed to fetch data: {e}")
    
    # Parse and validate the data
    data = response.json()
    if 'Time Series (1min)' not in data:
        raise Exception("Invalid data format received.")
    
    df = pd.DataFrame(data['Time Series (1min)']).T
    df = df.rename(columns={'1. open': 'Open', '2. high': 'High', '3. low': 'Low', '4. close': 'Close', '5. volume': 'Volume'})
    
    return df
