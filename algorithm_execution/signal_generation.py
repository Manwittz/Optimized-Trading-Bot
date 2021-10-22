
def generate_signals(model, df, features):
    """
    Generate trading signals (buy, sell, hold) using a trained model.
    
    Parameters:
    - model: Trained machine learning model
    - df: DataFrame containing feature data
    - features: List of feature columns in df
    
    Returns:
    - List of trading signals
    """
    # Validate input parameters
    if not features:
        raise ValueError("Feature list cannot be empty.")
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input data must be a DataFrame.")
    
    # Generate predictions using the model
    predictions = model.predict(df[features])
    
    # Map predictions to trading signals
    signal_mapping = {1: 'Buy', -1: 'Sell', 0: 'Hold'}
    signals = [signal_mapping.get(p, 'Unknown') for p in predictions]
    
    return signals
