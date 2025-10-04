import requests
import pandas as pd

class OpenMeteo:
    def extract_forecast_data():
        """
        Extracts weather forecast data from the Open-Meteo API.
        
        """
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": 45.53,   # Algonquin east gate coordinates
            "longitude": -78.27,
            "daily": ["temperature_2m_max", "temperature_2m_min", "wind_gusts_10m_max", "precipitation_sum"],	
            "timezone": "America/Toronto",
            "forecast_days": 16  # Get the next 16 days
        }
        
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()  # Raises an error for bad status codes (4xx or 5xx)
            data = response.json()
            
            # Parse the JSON response into a DataFrame
            forecast_df = pd.DataFrame({
                'date': pd.to_datetime(data['daily']['time']),
                'temp_max': data['daily']['temperature_2m_max'],
                'temp_min': data['daily']['temperature_2m_min'],
                'max_gusts': data['daily']['wind_gusts_10m_max'],
                'total_precip': data['daily']['precipitation_sum'],
            })
            return forecast_df
            
        except requests.exceptions.RequestException as e:
            print(f"Error fetching forecast data: {e}")
            return pd.DataFrame()  # Return empty DataFrame on error