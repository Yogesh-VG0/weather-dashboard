# WeatherWise CLI Dashboard

#### Video Demo: [URL HERE]

#### Description:

A command-line weather application that fetches real-time weather data from OpenWeatherMap API and generates HTML reports.

I built this as my CS50P final project because I wanted to work with APIs and create something practical. The app lets you check weather for any city, displays it nicely in the terminal, and can generate a styled HTML report that opens in your browser.

## How It Works

The program has three main functions that do the heavy lifting:

**get_weather_data(city)** - Takes a city name, calls the OpenWeatherMap API, and returns weather info like temperature, humidity, and conditions. I used the `requests` library for this.

**format_temperature(temp, unit)** - Converts temperature between Celsius, Fahrenheit, and Kelvin. The API returns Kelvin by default, so this was necessary.

**validate_city_name(city)** - Uses regex to make sure the city name only contains valid characters (letters, spaces, hyphens). Prevents bad input from hitting the API.

## Files

- `project.py` - Main program with all the core functions
- `test_project.py` - Tests using pytest with mocked API calls
- `config.py` - Stores API key and settings
- `weather_api.py` - WeatherAPI class (alternative way to fetch data)
- `report_generator.py` - Creates the HTML reports
- `requirements.txt` - Dependencies (requests, pytest, python-dotenv)

## Setup

1. Install dependencies:
```
pip install -r requirements.txt
```

2. Get a free API key from [OpenWeatherMap](https://openweathermap.org/api)

3. Create a `.env` file:
```
OPENWEATHER_API_KEY=your_key_here
```

4. Run it:
```
python project.py
```

## Testing

```
pytest test_project.py -v
```

The tests use `unittest.mock` to fake API responses so they run without needing an actual API key or internet connection.

## Design Choices

I separated the API logic into its own module (`weather_api.py`) to keep things organized, but the main functions in `project.py` work independently for CS50P requirements.

The HTML reports use inline CSS with a dark theme - no external dependencies needed. They auto-open in your default browser after generation.

For error handling, I catch specific HTTP status codes (404 for city not found, 401 for bad API key) and give clear error messages instead of crashing.

---

This was CS50P!
