
# Import necessary libraries
import csv
import requests
import json

def fetch_historical_data(api_endpoint):
    """
    Fetch historical data from a fictional API endpoint.
    """
    response = requests.get(api_endpoint)
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        return None

def store_to_csv(data, file_path):
    """
    Store the historical data to a CSV file.
    """
    with open(file_path, 'w', newline='') as csvfile:
        fieldnames = ['timestamp', 'open', 'high', 'low', 'close', 'volume']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for row in data:
            writer.writerow(row)

# Simulate fetching and storing historical data
api_endpoint = "https://fictional-api.com/historical_data"
historical_data = fetch_historical_data(api_endpoint)
if historical_data:
    store_to_csv(historical_data, 'historical_data.csv')
