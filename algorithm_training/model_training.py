
# Import necessary libraries
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import pandas as pd

def train_svm_model(df, features, target):
    """
    Train a Support Vector Machine (SVM) model.
    """
    X = df[features]
    y = df[target]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = SVC()
    model.fit(X_train, y_train)
    
    return model

# Example usage
# df = pd.DataFrame({'feature_1': [1, 2, 3, 4, 5], 'feature_2': [5, 4, 3, 2, 1], 'target': [1, 0, 1, 0, 1]})
# features = ['feature_1', 'feature_2']
# target = 'target'
# model = train_svm_model(df, features, target)
