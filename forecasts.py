import requests

class WeatherForecast:
    def get_forecast(self, location):
        """Request today's hourly temperatures for a Location object."""

        url = "https://api.open-meteo.com/v1/forecast"

        # Use the coordinates from the saved location.
        parameters = {
            "latitude": location.lat,
            "longitude": location.long,
            "hourly": "temperature_2m",
            "forecast_days": 1,
            "timezone": "auto"
        }


        response = requests.get(url, params=parameters, timeout=15)


        # Raise an error if the server returns an unsuccessful status.
        response.raise_for_status()

        # Convert the JSON response to dic
        return response.json()


