
# Define your risk management rules here
def manage_risk(position, current_price, entry_price):
    """
    Implement risk management rules such as setting stop-loss levels.
    """
    stop_loss_level = entry_price * 0.95  # 5% stop loss
    
    if current_price <= stop_loss_level:
        print('Stop Loss Triggered. Sell Position.')
        return 'Sell'
    
    return position  # Keep the current position (Buy/Hold/Sell)

# Simulate risk management
position = 'Buy'
current_price = 95
entry_price = 100

new_position = manage_risk(position, current_price, entry_price)
print(f"New Position: {new_position}")
