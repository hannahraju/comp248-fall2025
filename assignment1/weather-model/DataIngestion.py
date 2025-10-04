from OpenMeteo import OpenMeteo
import pandas as pd

class DataIngestion:

    def read_data(url):
        historical_df = pd.read_csv(url) ## read csv defined in PATH
        return historical_df
        
    def get_forecast():
        forecast_df = OpenMeteo.extract_forecast_data() ## extract data from OpenMeteo API
        return forecast_df
