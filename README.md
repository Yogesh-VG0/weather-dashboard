# WeatherWise

#### Video Demo: https://youtu.be/Nr_Xahy8WAQ

#### Description:

WeatherWise is a command-line weather application I built for my CS50P final project. It fetches real-time weather data from the OpenWeatherMap API and displays it in a clean, formatted output in the terminal. You can also generate styled HTML reports that automatically open in your browser.

I chose this project because I wanted to learn how to work with external APIs and handle real-world data. The OpenWeatherMap API provides current weather conditions for any city in the world, including temperature, humidity, wind speed, and atmospheric pressure.

The program validates user input using regular expressions to ensure city names only contain valid characters like letters, spaces, hyphens, and apostrophes. This prevents bad requests from being sent to the API and gives users clear error messages when they enter invalid input.

When you run the program, it prompts you for a city name. After fetching the data, it displays the weather information with the temperature, what it feels like, current conditions, humidity percentage, wind speed, and pressure. You can then choose to generate an HTML report which creates a nicely styled webpage with all the weather details.

The main functions in project.py are:

- `get_weather_data(city)` - This function takes a city name as input, makes an API request to OpenWeatherMap, and returns a dictionary containing all the weather information. It handles errors like invalid cities (404) and bad API keys (401).

- `format_temperature(temp, unit)` - Converts temperature between Celsius, Fahrenheit, and Kelvin. The API returns temperatures in Kelvin by default, so this function is useful for displaying temperatures in a more familiar format.

- `validate_city_name(city)` - Uses a regex pattern to check if the city name contains only valid characters. Returns True if valid, False otherwise. This prevents users from entering city names with numbers or special characters that would fail the API request.

The test file uses unittest.mock to simulate API responses. This means the tests can run without an internet connection or a valid API key, which makes them reliable and fast. Each of the three main functions has corresponding test cases that check both normal operation and edge cases.

I also created additional modules to keep the code organized. The config.py file stores the API key and settings, weather_api.py contains a WeatherAPI class as an alternative way to fetch data, and report_generator.py handles creating the HTML reports with inline CSS styling.

The HTML reports feature a dark theme with a gradient background and display all the weather information in a card layout. The report includes an SVG weather icon that changes based on conditions and whether it's day or night at the location.

This project taught me a lot about working with APIs, handling JSON data, error handling, input validation with regex, and writing testable code with mocking.
