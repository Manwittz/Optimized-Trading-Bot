
# Import necessary libraries
import pandas as pd
import talib

def engineer_features(df):
    """
    Create new features that could be predictive of market movements.
    """
    # Calculate moving averages
    df['SMA_50'] = talib.SMA(df['price'].values, timeperiod=50)
    df['SMA_200'] = talib.SMA(df['price'].values, timeperiod=200)
    
    # Calculate RSI (Relative Strength Index)
    df['RSI'] = talib.RSI(df['price'].values, timeperiod=14)
    
    return df

# Simulate feature engineering
# Create a DataFrame with some example data (In reality, you'd load your trading data here)
df = pd.DataFrame({
    'price': range(1, 101)
})

engineered_df = engineer_features(df)
print(f"Engineered Data: {engineered_df}")
