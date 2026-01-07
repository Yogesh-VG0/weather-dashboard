"""
Test suite for WeatherWise CLI Dashboard
Tests core functionality with mock data

CS50P Final Project
"""

import pytest
from project import get_weather_data, format_temperature, validate_city_name
from unittest.mock import patch, Mock


def test_format_temperature():
    """Test temperature conversion functionality"""
    # Test Celsius conversion
    assert format_temperature(273.15, "celsius") == "0.0°C"
    assert format_temperature(293.15, "celsius") == "20.0°C"
    assert format_temperature(373.15, "celsius") == "100.0°C"
    
    # Test Fahrenheit conversion
    assert format_temperature(273.15, "fahrenheit") == "32.0°F"
    assert format_temperature(293.15, "fahrenheit") == "68.0°F"
    
    # Test Kelvin (no conversion)
    assert format_temperature(273.15, "kelvin") == "273.1K"
    assert format_temperature(300.0, "kelvin") == "300.0K"
    
    # Test invalid unit
    with pytest.raises(ValueError):
        format_temperature(273.15, "invalid")
    
    with pytest.raises(ValueError):
        format_temperature(273.15, "")


def test_validate_city_name():
    """Test city name validation"""
    # Valid city names
    assert validate_city_name("London") == True
    assert validate_city_name("New York") == True
    assert validate_city_name("Saint-Denis") == True
    assert validate_city_name("O'Fallon") == True
    assert validate_city_name("Los Angeles") == True
    assert validate_city_name("San Francisco") == True
    
    # Invalid city names
    assert validate_city_name("") == False
    assert validate_city_name("A") == False  # Too short
    assert validate_city_name("London123") == False  # Contains numbers
    assert validate_city_name("London@City") == False  # Special chars
    assert validate_city_name("   ") == False  # Only spaces
    assert validate_city_name("City!") == False  # Exclamation mark
    assert validate_city_name("123") == False  # Only numbers


@patch('project.requests.get')
@patch('config.API_KEY', 'test_api_key')
def test_get_weather_data(mock_get):
    """Test weather data fetching with mocked API response"""
    # Create mock response for successful request
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        'name': 'London',
        'sys': {'country': 'GB'},
        'main': {
            'temp': 20.0,
            'feels_like': 18.5,
            'humidity': 65,
            'pressure': 1013
        },
        'weather': [{'description': 'clear sky', 'icon': '01d'}],
        'wind': {'speed': 5.5},
        'dt': 1609459200
    }
    mock_get.return_value = mock_response
    
    # Test successful data fetch
    result = get_weather_data("London")
    
    assert result['city'] == 'London'
    assert result['country'] == 'GB'
    assert 'temperature' in result
    assert result['humidity'] == 65
    assert result['description'] == 'clear sky'


@patch('project.requests.get')
@patch('config.API_KEY', 'test_api_key')
def test_get_weather_data_city_not_found(mock_get):
    """Test weather data fetching when city is not found"""
    # Create mock response for 404 error
    mock_response = Mock()
    mock_response.status_code = 404
    mock_get.return_value = mock_response
    
    with pytest.raises(ValueError, match="not found"):
        get_weather_data("InvalidCityXYZ123")


def test_format_temperature_edge_cases():
    """Test temperature conversion edge cases"""
    # Test absolute zero
    assert format_temperature(0, "kelvin") == "0.0K"
    assert format_temperature(0, "celsius") == "-273.1°C"
    
    # Test negative temperatures
    assert format_temperature(253.15, "celsius") == "-20.0°C"  # -20°C
    
    # Test very high temperatures (1000K - 273.15 = 726.85, rounds to 726.9)
    assert format_temperature(1000, "celsius") == "726.9°C"


def test_validate_city_name_edge_cases():
    """Test city name validation edge cases"""
    # Test cities with multiple spaces
    assert validate_city_name("New York City") == True
    
    # Test cities with hyphens
    assert validate_city_name("Stratford-upon-Avon") == True
    
    # Test cities with apostrophes
    assert validate_city_name("Land's End") == True
    
    # Test minimum valid length
    assert validate_city_name("LA") == True
    assert validate_city_name("L") == False


