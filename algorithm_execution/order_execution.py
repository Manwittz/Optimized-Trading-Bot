
# Import necessary libraries
import requests

def execute_order(api_endpoint, order_details):
    """
    Use an API to execute trading orders.
    """
    response = requests.post(api_endpoint, json=order_details)
    if response.status_code == 200:
        print('Order Executed Successfully')
    else:
        print('Order Execution Failed')

# Simulate order execution
api_endpoint = "https://fictional-api.com/execute_order"
order_details = {
    'symbol': 'AAPL',
    'quantity': 10,
    'order_type': 'Buy'
}

execute_order(api_endpoint, order_details)
