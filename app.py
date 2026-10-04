from flask import Flask, render_template, jsonify, request
from weather_agent import WeatherAgent


app = Flask(__name__)
agent = WeatherAgent()


WEATHER_ICONS = {
    "Clear sky": "☀️",
    "Mainly clear": "🌤️",
    "Partly cloudy": "⛅",
    "Overcast": "☁️",
    "Fog": "🌫️",
    "Depositing rime fog": "🌫️",
    "Light drizzle": "🌦️",
    "Moderate drizzle": "🌦️",
    "Dense drizzle": "🌧️",
    "Slight rain": "🌦️",
    "Moderate rain": "🌧️",
    "Heavy rain": "🌧️",
    "Slight rain showers": "🌦️",
    "Moderate rain showers": "🌧️",
    "Violent rain showers": "⛈️",
    "Slight snowfall": "🌨️",
    "Moderate snowfall": "❄️",
    "Heavy snowfall": "❄️",
    "Thunderstorm": "⛈️",
    "Thunderstorm with slight hail": "⛈️",
    "Thunderstorm with heavy hail": "⛈️"
}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/weather")
def weather():
    city = request.args.get("city", "").strip()

    if not city:
        return jsonify({
            "error": "Please enter a city name."
        }), 400

    try:
        data = agent.get_weather(city)

        condition = data["weather"]

        result = {
            "city": data["location"],
            "country": data["country"],
            "temperature": data["temperature"],
            "feels_like": data["feels_like"],
            "humidity": data["humidity"],
            "precipitation": data["precipitation"],
            "wind_speed": data["wind_speed"],
            "condition": condition,
            "icon": WEATHER_ICONS.get(condition, "🌤️")
        }

        return jsonify(result)

    except ValueError as error:
        return jsonify({
            "error": str(error)
        }), 404

    except Exception:
        return jsonify({
            "error": "Unable to retrieve weather information. Please try again."
        }), 500


if __name__ == "__main__":
    app.run(debug=True)