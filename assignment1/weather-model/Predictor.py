import pandas as pd

class Predictor:

    def __init__(self, model):
        self.model = model

    def get_forecast(self, X_test):
              
        y_pred = self.model.predict(X_test)
        return y_pred
        