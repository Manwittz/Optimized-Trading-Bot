
# Import necessary libraries
import pandas as pd

def store_to_parquet(df, file_name):
    """
    Store data to a Parquet file for efficient storage.
    """
    df.to_parquet(file_name)

# Example usage
# df = pd.DataFrame({'price': [1, 2, 3, 4, 5], 'volume': [100, 200, 300, 400, 500]})
# store_to_parquet(df, 'stock_data.parquet')
