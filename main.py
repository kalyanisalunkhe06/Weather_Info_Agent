import tkinter as tk
from tkinter import messagebox
from weather_agent import WeatherAgent


# --------------------------------------------------
# Weather Agent
# --------------------------------------------------

agent = WeatherAgent()


# --------------------------------------------------
# Weather Icons
# --------------------------------------------------

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
    "Slight rain": "🌧️",
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
    "Thunderstorm with heavy hail": "⛈️",
    "Unknown weather": "🌍"
}


# --------------------------------------------------
# Main Functions
# --------------------------------------------------

def show_weather():
    city = city_entry.get().strip()

    if not city:
        messagebox.showwarning(
            "Missing City",
            "Please enter a city name."
        )
        return

    # Show loading message
    status_label.config(
        text="Fetching weather information..."
    )

    search_button.config(
        state="disabled"
    )

    root.update_idletasks()

    try:
        weather = agent.get_weather(city)

        condition = weather["weather"]

        icon = WEATHER_ICONS.get(
            condition,
            "🌍"
        )

        # Update location
        location_label.config(
            text=f"📍 {weather['location']}, {weather['country']}"
        )

        # Update main temperature
        temperature_label.config(
            text=f"{weather['temperature']} °C"
        )

        # Update weather icon
        weather_icon_label.config(
            text=icon
        )

        # Update condition
        condition_label.config(
            text=condition
        )

        # Update details
        feels_like_value.config(
            text=f"{weather['feels_like']} °C"
        )

        humidity_value.config(
            text=f"{weather['humidity']}%"
        )

        precipitation_value.config(
            text=f"{weather['precipitation']} mm"
        )

        wind_value.config(
            text=f"{weather['wind_speed']} km/h"
        )

        status_label.config(
            text="Weather information updated successfully."
        )

    except ValueError as error:

        status_label.config(
            text="Unable to find the requested city."
        )

        messagebox.showerror(
            "City Not Found",
            str(error)
        )

    except Exception as error:

        status_label.config(
            text="Unable to retrieve weather information."
        )

        messagebox.showerror(
            "Error",
            f"Something went wrong:\n\n{error}"
        )

    finally:

        search_button.config(
            state="normal"
        )


def search_on_enter(event):
    show_weather()


# --------------------------------------------------
# Main Window
# --------------------------------------------------

root = tk.Tk()

root.title("Weather Info Agent")

root.geometry("760x650")

root.resizable(False, False)

root.configure(
    bg="#F4F7FB"
)


# --------------------------------------------------
# Header
# --------------------------------------------------

header_frame = tk.Frame(
    root,
    bg="#1F6FEB",
    height=150
)

header_frame.pack(
    fill="x"
)

header_frame.pack_propagate(False)


title_label = tk.Label(
    header_frame,
    text="Weather Info Agent",
    font=("Segoe UI", 26, "bold"),
    bg="#1F6FEB",
    fg="white"
)

title_label.pack(
    pady=(25, 4)
)


subtitle_label = tk.Label(
    header_frame,
    text="Get live weather information for any city",
    font=("Segoe UI", 11),
    bg="#1F6FEB",
    fg="white"
)

subtitle_label.pack()


# --------------------------------------------------
# Search Section
# --------------------------------------------------

search_frame = tk.Frame(
    root,
    bg="#F4F7FB"
)

search_frame.pack(
    pady=(25, 15)
)


city_label = tk.Label(
    search_frame,
    text="Search City",
    font=("Segoe UI", 11, "bold"),
    bg="#F4F7FB",
    fg="#263238"
)

city_label.grid(
    row=0,
    column=0,
    columnspan=2,
    sticky="w",
    pady=(0, 7)
)


city_entry = tk.Entry(
    search_frame,
    font=("Segoe UI", 13),
    width=30,
    relief="solid",
    bd=1
)

city_entry.grid(
    row=1,
    column=0,
    padx=(0, 10)
)


search_button = tk.Button(
    search_frame,
    text="Get Weather",
    font=("Segoe UI", 11, "bold"),
    bg="#1F6FEB",
    fg="white",
    activebackground="#1558B0",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    padx=18,
    pady=8,
    command=show_weather
)

search_button.grid(
    row=1,
    column=1
)


# --------------------------------------------------
# Weather Main Card
# --------------------------------------------------

weather_card = tk.Frame(
    root,
    bg="white",
    highlightbackground="#DDE3EA",
    highlightthickness=1
)

weather_card.pack(
    padx=45,
    fill="x"
)


location_label = tk.Label(
    weather_card,
    text="📍 Enter a city to view weather",
    font=("Segoe UI", 15, "bold"),
    bg="white",
    fg="#263238"
)

location_label.pack(
    pady=(22, 8)
)


weather_icon_label = tk.Label(
    weather_card,
    text="🌤️",
    font=("Segoe UI Emoji", 50),
    bg="white"
)

weather_icon_label.pack()


temperature_label = tk.Label(
    weather_card,
    text="-- °C",
    font=("Segoe UI", 38, "bold"),
    bg="white",
    fg="#1F6FEB"
)

temperature_label.pack(
    pady=(0, 2)
)


condition_label = tk.Label(
    weather_card,
    text="No weather data",
    font=("Segoe UI", 14),
    bg="white",
    fg="#607D8B"
)

condition_label.pack(
    pady=(0, 22)
)


# --------------------------------------------------
# Weather Details
# --------------------------------------------------

details_frame = tk.Frame(
    root,
    bg="#F4F7FB"
)

details_frame.pack(
    padx=45,
    pady=20,
    fill="x"
)


def create_detail_card(parent, title, value, row, column):

    card = tk.Frame(
        parent,
        bg="white",
        highlightbackground="#DDE3EA",
        highlightthickness=1,
        width=150,
        height=85
    )

    card.grid(
        row=row,
        column=column,
        padx=6,
        pady=6,
        sticky="nsew"
    )

    card.grid_propagate(False)

    title_label = tk.Label(
        card,
        text=title,
        font=("Segoe UI", 9),
        bg="white",
        fg="#78909C"
    )

    title_label.pack(
        pady=(12, 2)
    )

    value_label = tk.Label(
        card,
        text=value,
        font=("Segoe UI", 13, "bold"),
        bg="white",
        fg="#263238"
    )

    value_label.pack()

    return value_label


details_frame.columnconfigure(0, weight=1)
details_frame.columnconfigure(1, weight=1)
details_frame.columnconfigure(2, weight=1)
details_frame.columnconfigure(3, weight=1)


feels_like_value = create_detail_card(
    details_frame,
    "Feels Like",
    "-- °C",
    0,
    0
)

humidity_value = create_detail_card(
    details_frame,
    "Humidity",
    "--%",
    0,
    1
)

precipitation_value = create_detail_card(
    details_frame,
    "Precipitation",
    "-- mm",
    0,
    2
)

wind_value = create_detail_card(
    details_frame,
    "Wind Speed",
    "-- km/h",
    0,
    3
)


# --------------------------------------------------
# Status
# --------------------------------------------------

status_label = tk.Label(
    root,
    text="Enter a city and click 'Get Weather'",
    font=("Segoe UI", 9),
    bg="#F4F7FB",
    fg="#78909C"
)

status_label.pack(
    pady=(0, 15)
)


# --------------------------------------------------
# Keyboard Shortcut
# --------------------------------------------------

city_entry.bind(
    "<Return>",
    search_on_enter
)


# Put cursor inside city box
city_entry.focus()


# --------------------------------------------------
# Start Application
# --------------------------------------------------

root.mainloop()