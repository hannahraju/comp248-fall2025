from sklearn.preprocessing import LabelEncoder
import pandas as pd


class DataTransform():
     
    def transform(raw_df, forecast_df):

        # format raw data to be consistent with api data
        historical_df = pd.DataFrame({
            'date': pd.to_datetime(raw_df['Date/Time']),
            'temp_max': raw_df['Max Temp (°C)'],
            'temp_min': raw_df['Min Temp (°C)'],
            'max_gusts': raw_df['Spd of Max Gust (km/h)'],
            'total_precip': raw_df['Total Precip (mm)'],
        })

        # handle max_gust values listed as strings
        historical_df['max_gusts'] = historical_df['max_gusts'].replace('<', '', regex=True) # remove "<" from wind gusts

        # handle NaNs
        historical_df = historical_df.fillna(0) # handle no wind

        # cast max_gust to float
        historical_df['max_gusts'] = historical_df['max_gusts'].astype(float) # cast to float

        # combine datasets
        df = pd.concat([historical_df, forecast_df], ignore_index=True)
        df.sort_values(by='date')

        # handle dates
        current_date = pd.Timestamp.now()
        df['date'] = df['date'] - current_date
        df['date'] = df['date'].dt.days

        # split data
        X_train = df.drop(columns=['temp_max'])
        y_train = df['temp_max']

        return (X_train, y_train)    
  

    
    
 


          
          
    

    
     