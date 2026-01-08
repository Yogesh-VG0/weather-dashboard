# WeatherWise

#### Video Demo: https://youtu.be/Nr_Xahy8WAQ

#### Description:

A CLI weather app that fetches real-time data from OpenWeatherMap and generates HTML reports.

Enter any city name, get current weather (temperature, humidity, wind, etc.), and optionally generate a styled report that opens in your browser.

The script uses `requests` to call the API and `python-dotenv` to load the API key from a `.env` file. City names are validated with regex before making requests.

Three main functions:
- `get_weather_data(city)` - fetches weather from API
- `format_temperature(temp, unit)` - converts between Celsius/Fahrenheit/Kelvin  
- `validate_city_name(city)` - checks input is valid

Tests use `unittest.mock` to fake API responses so they work offline.

## Usage

```
pip install -r requirements.txt
```

Get a free API key from [openweathermap.org](https://openweathermap.org/api), add it to `.env`:
```
OPENWEATHER_API_KEY=your_key
```

Run:
```
python project.py
```
