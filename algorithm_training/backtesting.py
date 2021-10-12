
# Import necessary libraries
import pandas as pd

def backtest_strategy(df, model, features, target):
    """
    Backtest a trading strategy using historical data and a trained model.
    """
    predictions = model.predict(df[features])
    
    # Here, we'll simply compare our predictions to the actual target values
    # A real backtest would involve simulating trades and calculating performance metrics
    correct_predictions = (predictions == df[target]).sum()
    total_predictions = len(predictions)
    
    accuracy = correct_predictions / total_predictions
    print(f'Backtest Accuracy: {accuracy}')
    
    return accuracy

# Simulate backtesting
# Create a DataFrame with some example data (In reality, you'd load your trading data here)
df = pd.DataFrame({
    'feature_1': [1, 2, 3, 4, 5],
    'feature_2': [5, 4, 3, 2, 1],
    'target': [0, 1, 0, 1, 0]
})

# Mock a trained model (In reality, you'd use your actual trained model)
class MockModel:
    def predict(self, X):
        return [0, 1, 0, 1, 0]

model = MockModel()
features = ['feature_1', 'feature_2']
target = 'target'

backtest_accuracy = backtest_strategy(df, model, features, target)
