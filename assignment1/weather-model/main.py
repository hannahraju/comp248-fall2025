from OpenMeteo import OpenMeteo
from DataIngestion import DataIngestion
from DataTransform import DataTransform
from ModelLoader import ModelLoader
from Predictor import Predictor

PATH = "F:/Hannah-PCBackup/02 AREAS/school/COMP248/comp248-fall2025/assignment1/weather_data.csv"

def main():

    # READ DATA
    raw_data = DataIngestion.read_data(PATH) # returns dataframe from historical data provided by url
    forecast_data = DataIngestion.get_forecast() #returns dataframe from forecast API
      
    # PROCESS DATA 
    X, y = DataTransform.transform(raw_data, forecast_data)
    
    # LOAD DATA TO EXTERNAL PREDICTOR MODEL
    model = ModelLoader.train_model(X,y)

    # PREDICT weather 24 hours from now
    X_test = X.loc[X['date'] == 1]
    predict = Predictor(model)
    prediction = predict.get_forecast(X_test)
    print("Tomorrow's predicted temperature: " +str(prediction))

    
    

if __name__ == '__main__':
   main()