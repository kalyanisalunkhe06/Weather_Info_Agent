# Weather Info Agent 🌤️

A desktop-based weather information application built with Python and Tkinter. The application allows users to enter a city name and view its current weather information using the Open-Meteo APIs.

## Features

* Search weather by city name
* Displays location and country
* Shows temperature
* Shows feels-like temperature
* Displays humidity
* Displays precipitation
* Displays wind speed
* Shows current weather condition
* Weather condition icons
* Clean and modern graphical user interface
* Error handling for invalid locations and API failures
* Press **Enter** to search for weather

## Technologies Used

* Python 3.12
* Tkinter
* Requests
* Open-Meteo Geocoding API
* Open-Meteo Weather API

## Project Structure

```text
Weather_Info_Agent/
│
├── .venv/
├── main.py
├── weather_agent.py
├── requirements.txt
├── README.md
└── .gitignore
```

## How the Application Works

1. The user enters a city name.
2. The application sends the city name to the Open-Meteo Geocoding API.
3. The API returns the city's latitude and longitude.
4. The application uses these coordinates to request weather data.
5. The weather information is displayed in the graphical interface.

## Installation

### 1. Clone or download the project

Open the project folder in VS Code.

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

On Windows PowerShell:

```powershell
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## Running the Application

Make sure the virtual environment is activated, then run:

```bash
python main.py
```

The Weather Info Agent window will open.

## Testing the Weather Agent

The weather API logic can also be tested separately by running:

```bash
python weather_agent.py
```

## APIs Used

### Open-Meteo Geocoding API

Used to find the geographical coordinates of a city.

### Open-Meteo Weather API

Used to retrieve weather information based on geographical coordinates.

## Requirements

* Python 3.10 or newer
* Internet connection
* Windows/macOS/Linux
* Required Python packages listed in `requirements.txt`

## Privacy

The application does not require user registration or store personal information. City names are sent to the Open-Meteo APIs to retrieve weather information.

## License

This project is created for educational and portfolio purposes.

## Author

Kalyani Salunkhe
