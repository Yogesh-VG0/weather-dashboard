"""
Weather API interaction module
Handles all communication with OpenWeatherMap API
"""

import requests
from datetime import datetime
from config import API_KEY, BASE_URL, TIMEOUT


class WeatherAPI:
    """Class to handle weather API interactions"""
    
    def __init__(self, api_key=API_KEY):
        """
        Initialize WeatherAPI with API key
        
        Args:
            api_key (str): OpenWeatherMap API key
        """
        self.api_key = api_key
        self.base_url = BASE_URL
        
    def fetch_current_weather(self, city):
        """
        Fetch current weather for a city
        
        Args:
            city (str): City name
            
        Returns:
            dict: Parsed weather data
            
        Raises:
            ValueError: If city not found or API error
            requests.RequestException: If network error
        """
        if not self.api_key:
            raise ValueError("API key not configured")
        
        params = {
            'q': city,
            'appid': self.api_key,
            'units': 'metric'  # Get data in Celsius
        }
        
        try:
            response = requests.get(
                self.base_url,
                params=params,
                timeout=TIMEOUT
            )
            
            if response.status_code == 404:
                raise ValueError(f"City '{city}' not found")
            elif response.status_code == 401:
                raise ValueError("Invalid API key")
            
            response.raise_for_status()
            
            return self._parse_weather_data(response.json())
            
        except requests.HTTPError as e:
            if e.response.status_code == 404:
                raise ValueError(f"City '{city}' not found")
            elif e.response.status_code == 401:
                raise ValueError("Invalid API key")
            else:
                raise ValueError(f"API error: {e}")
        
    def _parse_weather_data(self, raw_data):
        """
        Parse raw API response into usable format
        
        Args:
            raw_data (dict): Raw JSON response from API
            
        Returns:
            dict: Parsed weather data
        """
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
    
    def get_weather_emoji(self, description):
        """
        Get appropriate emoji for weather condition
        
        Args:
            description (str): Weather description
            
        Returns:
            str: Weather emoji
        """
        description = description.lower()
        
        if 'clear' in description:
            return '☀️'
        elif 'cloud' in description:
            return '☁️'
        elif 'rain' in description:
            return '🌧️'
        elif 'thunder' in description:
            return '⛈️'
        elif 'snow' in description:
            return '❄️'
        elif 'mist' in description or 'fog' in description:
            return '🌫️'
        else:
            return '🌤️'

