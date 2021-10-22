
def store_data_to_csv(df, file_path):
    """
    Store market data in a CSV file.
    
    Parameters:
    - df: DataFrame containing the market data
    - file_path: The path where the CSV file will be stored
    
    Returns:
    - None
    """
    # Validate input parameters
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input data must be a DataFrame.")
    if not file_path.lower().endswith('.csv'):
        raise ValueError("File path must end with '.csv'.")
    
    # Store data in CSV
    try:
        df.to_csv(file_path, index=False)
    except Exception as e:
        raise Exception(f"Failed to store data: {e}")
