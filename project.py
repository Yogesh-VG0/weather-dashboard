"""
WeatherWise CLI Dashboard
A comprehensive weather information tool using OpenWeatherMap API

CS50P Final Project
"""

import sys
import requests
from datetime import datetime
import re


def main():
    """
    Main function - handles user interaction and program flow
    """
    print("=" * 50)
    print("🌤️  WeatherWise CLI Dashboard")
    print("=" * 50)
    print()
    print("Tip: Enter any city name (e.g., London, Tokyo, New York)")
    print("     Type 'quit' to exit\n")
    
    while True:
        # Get city input from user
        city = input("Enter city name (or 'quit' to exit): ").strip()
        
        if city.lower() == 'quit':
            print("\nThank you for using WeatherWise! Goodbye! 👋")
            sys.exit(0)
        
        # Validate city name
        if not validate_city_name(city):
            print("❌ Error: Invalid city name. Please use only letters, spaces, and hyphens.")
            print()
            continue
        
        # Fetch weather data
        try:
            weather_data = get_weather_data(city)
            display_weather(weather_data)
            
            # Ask if user wants HTML report
            generate = input("\nGenerate HTML report? (y/n): ").strip().lower()
            if generate in ('yes', 'y'):
                from report_generator import create_html_report
                report_path = create_html_report(weather_data)
                print(f"✅ Report generated: {report_path}")
            
            print()
                
        except ValueError as e:
            print(f"❌ Error: {e}")
            print()
        except requests.RequestException as e:
            print(f"❌ Network error: {e}")
            print()


def get_weather_data(city):
    """
    Fetch weather data from OpenWeatherMap API
    
    Args:
        city (str): Name of the city
        
    Returns:
        dict: Weather data including temperature, conditions, humidity, etc.
        
    Raises:
        ValueError: If city not found or API error
        requests.RequestException: If network error
    """
    from config import API_KEY, BASE_URL, TIMEOUT
    
    if not API_KEY:
        raise ValueError("API key not configured. Please set OPENWEATHER_API_KEY in .env file")
    
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  # Get data in Celsius
    }
    
    try:
        response = requests.get(BASE_URL, params=params, timeout=TIMEOUT)
        
        if response.status_code == 404:
            raise ValueError(f"City '{city}' not found")
        elif response.status_code == 401:
            raise ValueError("Invalid API key")
        
        response.raise_for_status()
        raw_data = response.json()
        
        # Parse and return weather data
        return {
            'city': raw_data['name'],
            'country': raw_data['sys']['country'],
            'temperature': f"{raw_data['main']['temp']:.1f}°C",
            'feels_like': f"{raw_data['main']['feels_like']:.1f}°C",
            'temp_kelvin': raw_data['main']['temp'] + 273.15,
            'description': raw_data['weather'][0]['description'],
            'icon': raw_data['weather'][0]['icon'],  # e.g., '01d' (day) or '01n' (night)
            'humidity': raw_data['main']['humidity'],
            'pressure': raw_data['main']['pressure'],
            'wind_speed': raw_data['wind']['speed'],
            'timestamp': datetime.fromtimestamp(raw_data['dt']).strftime('%Y-%m-%d %H:%M:%S')
        }
        
    except requests.HTTPError as e:
        if e.response.status_code == 404:
            raise ValueError(f"City '{city}' not found")
        elif e.response.status_code == 401:
            raise ValueError("Invalid API key")
        else:
            raise ValueError(f"API error: {e}")


def format_temperature(temp, unit="celsius"):
    """
    Convert and format temperature values
    
    Args:
        temp (float): Temperature in Kelvin
        unit (str): Target unit - 'celsius', 'fahrenheit', or 'kelvin'
        
    Returns:
        str: Formatted temperature string (e.g., "25°C")
        
    Raises:
        ValueError: If invalid unit specified
    """
    if unit not in ["celsius", "fahrenheit", "kelvin"]:
        raise ValueError(f"Invalid unit: {unit}")
    
    if unit == "celsius":
        converted = temp - 273.15
        return f"{converted:.1f}°C"
    elif unit == "fahrenheit":
        converted = (temp - 273.15) * 9/5 + 32
        return f"{converted:.1f}°F"
    else:
        return f"{temp:.1f}K"


def validate_city_name(city):
    """
    Validate city name format
    
    Args:
        city (str): City name to validate
        
    Returns:
        bool: True if valid, False otherwise
    """
    # City names can contain letters, spaces, hyphens, and apostrophes
    # Examples: "New York", "Saint-Denis", "O'Fallon"
    pattern = r"^[a-zA-Z\s\-']+$"
    
    if not city or len(city.strip()) < 2:
        return False
    
    # Check if it's only whitespace
    if city.isspace():
        return False
    
    return bool(re.match(pattern, city))


def display_weather(data):
    """
    Display weather data in formatted CLI output
    
    Args:
        data (dict): Weather data dictionary
    """
    print()
    print("=" * 50)
    print(f"☁️  Weather for {data['city']}, {data['country']}")
    print("=" * 50)
    print(f"🌡️  Temperature: {data['temperature']}")
    print(f"🤗 Feels Like:  {data['feels_like']}")
    print(f"📋 Conditions:  {data['description'].title()}")
    print(f"💧 Humidity:    {data['humidity']}%")
    print(f"💨 Wind Speed:  {data['wind_speed']} m/s")
    print(f"📊 Pressure:    {data['pressure']} hPa")
    print(f"🕐 Updated:     {data['timestamp']}")
    print("=" * 50)


if __name__ == "__main__":
    main()
