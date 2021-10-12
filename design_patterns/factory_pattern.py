# factory pattern

from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

class ModelFactory:
    def create_model(self, model_type):
        if model_type == 'RandomForest':
            return RandomForestClassifier()
        elif model_type == 'SVM':
            return SVC()
        else:
            raise ValueError('Invalid model type')

# Usage:
# factory = ModelFactory()
# model = factory.create_model('RandomForest')
