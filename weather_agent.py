import requests


class WeatherAgent:
    def __init__(self):
        self.session = requests.Session()

        self.geocoding_url = "https://geocoding-api.open-meteo.com/v1/search"
        self.weather_url = "https://api.open-meteo.com/v1/forecast"

    def get_coordinates(self, city):
        params = {
            "name": city,
            "count": 1,
            "language": "en",
            "format": "json"
        }

        response = self.session.get(
            self.geocoding_url,
            params=params,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        if "results" not in data or not data["results"]:
            raise ValueError(f"City '{city}' was not found.")

        location = data["results"][0]

        return (
            location["latitude"],
            location["longitude"],
            location.get("name", city),
            location.get("country", "")
        )

    def get_weather(self, city):
        latitude, longitude, location_name, country = self.get_coordinates(city)

        params = {
            "latitude": latitude,
            "longitude": longitude,
            "current": (
                "temperature_2m,"
                "relative_humidity_2m,"
                "apparent_temperature,"
                "is_day,"
                "precipitation,"
                "weather_code,"
                "wind_speed_10m"
            ),
            "timezone": "auto"
        }

        response = self.session.get(
            self.weather_url,
            params=params,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        current = data["current"]

        return {
            "location": location_name,
            "country": country,
            "temperature": current["temperature_2m"],
            "humidity": current["relative_humidity_2m"],
            "feels_like": current["apparent_temperature"],
            "precipitation": current["precipitation"],
            "wind_speed": current["wind_speed_10m"],
            "weather": self.get_weather_description(
                current["weather_code"]
            ),
            "is_day": current["is_day"]
        }

    @staticmethod
    def get_weather_description(code):
        weather_codes = {
            0: "Clear sky",
            1: "Mainly clear",
            2: "Partly cloudy",
            3: "Overcast",
            45: "Fog",
            48: "Depositing rime fog",
            51: "Light drizzle",
            53: "Moderate drizzle",
            55: "Dense drizzle",
            61: "Slight rain",
            63: "Moderate rain",
            65: "Heavy rain",
            71: "Slight snowfall",
            73: "Moderate snowfall",
            75: "Heavy snowfall",
            80: "Slight rain showers",
            81: "Moderate rain showers",
            82: "Violent rain showers",
            95: "Thunderstorm",
            96: "Thunderstorm with slight hail",
            99: "Thunderstorm with heavy hail"
        }

        return weather_codes.get(code, "Unknown weather")


if __name__ == "__main__":
    agent = WeatherAgent()

    try:
        weather = agent.get_weather("Pune")

        print("\nWeather Information")
        print("-------------------")
        print(f"Location: {weather['location']}, {weather['country']}")
        print(f"Temperature: {weather['temperature']} °C")
        print(f"Feels like: {weather['feels_like']} °C")
        print(f"Humidity: {weather['humidity']}%")
        print(f"Precipitation: {weather['precipitation']} mm")
        print(f"Wind Speed: {weather['wind_speed']} km/h")
        print(f"Condition: {weather['weather']}")

    except requests.RequestException as error:
        print(f"Network error: {error}")

    except ValueError as error:
        print(f"Error: {error}")