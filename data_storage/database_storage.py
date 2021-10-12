
# Import necessary libraries
import sqlite3
import pandas as pd

def store_to_database(df, table_name):
    """
    Store the data to an SQLite database.
    """    
    conn = sqlite3.connect('trading_data.db')
    df.to_sql(table_name, conn, if_exists='replace')
    conn.close()

# Simulate database storage
# Create a DataFrame with some example data (In reality, you'd load your trading data here)
df = pd.DataFrame({
    'price': [1, 2, 3, 4, 5],
    'volume': [100, 200, 300, 400, 500]
})

store_to_database(df, 'historical_data')
