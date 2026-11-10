from pathlib import Path
import sys
from Location import Location

print(sys.executable)

import requests
from Location import LocationManager
from forecasts import WeatherForecast

try:

    location = Location(1, "London", "UK", "GBR", 51.52, -0.127)

    weather = WeatherForecast()
    forecast = weather.get_forecast(location)

    times = forecast["hourly"]["time"]
    temperatures = forecast["hourly"]["temperature_2m"]
    unit = forecast["hourly_units"]["temperature_2m"]


    print(f"Today's hourly forecast for {location.name}:")

    for time, temperature in zip(times, temperatures):
        print(f"{time}: {temperature} {unit}")


except requests.RequestException as error:
    print(f"could not retrieve the forecast: {error}")

except ValueError as error:
    print(error)