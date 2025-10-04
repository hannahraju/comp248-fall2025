from sklearn.linear_model import LinearRegression

class ModelLoader():
   
    def train_model(X_train, y_train):
        model = LinearRegression().fit(X_train, y_train)        
        return model
   