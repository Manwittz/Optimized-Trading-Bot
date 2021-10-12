
# Import necessary libraries
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pandas as pd

def train_model(df, features, target):
    """
    Train a Random Forest model on the data.
    """
    X = df[features]
    y = df[target]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    score = model.score(X_test, y_test)
    print(f'Model Accuracy: {score}')
    
    return model

# Simulate model training
# Create a DataFrame with some example data (In reality, you'd load your trading data here)
df = pd.DataFrame({
    'feature_1': [1, 2, 3, 4, 5],
    'feature_2': [5, 4, 3, 2, 1],
    'target': [0, 1, 0, 1, 0]
})

features = ['feature_1', 'feature_2']
target = 'target'

trained_model = train_model(df, features, target)
