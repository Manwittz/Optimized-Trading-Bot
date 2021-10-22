
def calculate_sma(data, window):
    """
    Calculate the Simple Moving Average (SMA) for a given data series and window size.
    
    Parameters:
    - data: Pandas Series containing the price data
    - window: Integer specifying the window size for SMA calculation
    
    Returns:
    - Pandas Series containing the calculated SMA values
    """
    # Validate input parameters
    if not isinstance(data, pd.Series):
        raise TypeError("Input data must be a Pandas Series.")
    if window <= 0:
        raise ValueError("Window size must be greater than zero.")
    
    # Calculate the SMA
    return data.rolling(window=window).mean()
