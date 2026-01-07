"""
Configuration file for WeatherWise
Contains API keys, constants, and settings
"""

import os

# Try to load environment variables from .env file
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # dotenv not installed, will use environment variables directly

# API Configuration
API_KEY = os.getenv("OPENWEATHER_API_KEY", "")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"

# Validate API key on import (helpful warning for users)
if not API_KEY:
    print("WARNING: OPENWEATHER_API_KEY not set in .env file")
    print("Get your free API key at: https://openweathermap.org/api")
    print()

# Default Settings
DEFAULT_UNIT = "celsius"
TIMEOUT = 10  # API request timeout in seconds

# Temperature thresholds for recommendations (in Celsius)
COLD_THRESHOLD = 10
HOT_THRESHOLD = 30

# Report Settings
REPORTS_DIR = "reports"
TEMPLATE_DIR = "templates"
