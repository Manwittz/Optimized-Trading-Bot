
# Import necessary libraries
from sklearn.preprocessing import MinMaxScaler
import pandas as pd

def normalize_data(df):
    """
    Scale the features so they have similar ranges.
    """
    scaler = MinMaxScaler()
    scaled_df = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)
    
    return scaled_df

# Simulate normalization
# Create a DataFrame with some example data (In reality, you'd load your trading data here)
df = pd.DataFrame({
    'price': [1, 2, 3, 4, 5],
    'volume': [100, 200, 300, 400, 500]
})

normalized_df = normalize_data(df)
print(f"Normalized Data: {normalized_df}")
