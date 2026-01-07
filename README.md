# WeatherWise CLI Dashboard

#### Video Demo: [URL TO BE ADDED]

#### Description:

WeatherWise is a comprehensive command-line weather dashboard application that provides real-time weather information for any city worldwide. Built as the final project for CS50's Introduction to Programming with Python (CS50P), this application demonstrates proficiency in API integration, data processing, error handling, and test-driven development.

## 🌟 Features

- **Real-time Weather Data**: Fetches current weather conditions from OpenWeatherMap API
- **Multi-format Temperature Display**: Supports Celsius, Fahrenheit, and Kelvin
- **Comprehensive Weather Info**: Temperature, humidity, wind speed, pressure, and conditions
- **Input Validation**: Robust city name validation using regular expressions
- **HTML Report Generation**: Creates beautiful, styled HTML weather reports
- **Error Handling**: Graceful handling of network errors, invalid inputs, and API issues
- **Unit Tested**: Comprehensive test suite with pytest

## 📁 Project Structure

```
weather-dashboard/
├── project.py              # Main application file
├── test_project.py         # Test suite
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
├── config.py               # Configuration management
├── weather_api.py          # API interaction class
├── report_generator.py     # HTML report generation
├── .env.example            # Environment variable template
├── .gitignore              # Git ignore rules
└── reports/                # Generated HTML reports
```

## 🚀 Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/weather-dashboard.git
cd weather-dashboard
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Configure API Key**
   - Get a free API key from [OpenWeatherMap](https://openweathermap.org/api)
   - Copy `.env.example` to `.env`
   - Add your API key to `.env`:
```
OPENWEATHER_API_KEY=your_actual_api_key_here
```

## 💻 Usage

### Basic Usage
```bash
python project.py
```

Then follow the prompts:
- Enter a city name (e.g., "London", "New York", "Tokyo")
- View weather information in the terminal
- Optionally generate an HTML report

### Example Session
```
==================================================
🌤️  WeatherWise CLI Dashboard
==================================================

Enter city name (or 'quit' to exit): London

==================================================
☁️  Weather for London, GB
==================================================
🌡️  Temperature: 15.3°C
🤗 Feels Like:  14.1°C
📋 Conditions:  Clear Sky
💧 Humidity:    65%
💨 Wind Speed:  5.5 m/s
📊 Pressure:    1013 hPa
🕐 Updated:     2024-01-08 14:30:45
==================================================

Generate HTML report? (yes/no): yes
✅ Report generated: reports/weather_report_London_20240108_143045.html
```

## 🧪 Testing

Run the test suite with pytest:
```bash
pytest test_project.py
```

Run with verbose output:
```bash
pytest test_project.py -v
```

Run with coverage report:
```bash
pytest test_project.py --cov=project
```

## 📝 Design Decisions

### Function Organization

The project is structured around three core testable functions required by CS50P:

1. **`get_weather_data(city)`**: Handles API communication and data fetching
   - **Why separate**: Isolates API logic for easier testing with mocks
   - **Testing approach**: Uses `unittest.mock` to simulate API responses
   - **Error handling**: Validates API key, handles network errors, manages API rate limits

2. **`format_temperature(temp, unit)`**: Converts temperatures between units
   - **Why separate**: Pure function with no side effects, easily testable
   - **Testing approach**: Direct assertion testing with known values
   - **Design choice**: Returns formatted strings ready for display

3. **`validate_city_name(city)`**: Validates user input using regex
   - **Why separate**: Reusable validation logic, security best practice
   - **Testing approach**: Comprehensive test cases for valid/invalid inputs
   - **Regex pattern**: Allows letters, spaces, hyphens, apostrophes (e.g., "New York", "O'Fallon")

### API Integration Design

I chose to create a separate `WeatherAPI` class in `weather_api.py` rather than putting all API logic in `project.py` for several reasons:

- **Separation of Concerns**: Keeps API interaction logic separate from user interface
- **Testability**: Easier to mock and test API calls independently
- **Reusability**: The API class could be imported by other modules
- **Maintainability**: API changes only require updates in one file

### Error Handling Strategy

The application implements multiple layers of error handling:

1. **Input Validation**: City names are validated before API calls
2. **API Errors**: Specific error messages for different HTTP status codes
3. **Network Errors**: Timeout handling and connection error management
4. **Configuration Errors**: Clear messages when API key is missing

### HTML Report Generation

I chose to generate HTML reports rather than plain text for several reasons:

- **Visual Appeal**: Styled reports are more professional and engaging
- **Portability**: HTML files can be opened anywhere, shared easily
- **Preservation**: Weather data is saved for historical reference
- **Demonstration**: Shows ability to generate formatted output beyond terminal

The CSS uses modern gradient backgrounds, glassmorphism effects, and card layouts to create an attractive, readable report with a dark theme aesthetic.

### Temperature Display

The `format_temperature()` function supports three units (Celsius, Fahrenheit, Kelvin) because:

- **International Users**: Different regions use different temperature scales
- **Scientific Use**: Some users may need Kelvin for calculations
- **Flexibility**: Demonstrates handling of multiple output formats
- **Testing**: Provides good test cases for conversion logic

## 🔧 Technical Implementation

### API Integration
- Uses `requests` library for HTTP communication
- Implements timeout handling (10 seconds)
- Parses JSON responses with error checking
- Handles rate limiting and invalid API keys

### Testing Strategy
- **Unit Tests**: Each function tested independently
- **Mock Testing**: API calls are mocked to avoid network dependency
- **Edge Cases**: Tests cover invalid inputs, empty strings, special characters
- **Coverage**: Aims for >80% code coverage

### File I/O
- Creates `reports/` directory if it doesn't exist
- Generates timestamped filenames to prevent overwriting
- Uses UTF-8 encoding for international character support

## 🎓 CS50P Concepts Applied

This project demonstrates proficiency in concepts from throughout CS50P:

- **Functions & Variables** (Lecture 0): Modular function design
- **Conditionals** (Lecture 1): Input validation, error handling
- **Loops** (Lecture 2): Main program loop for continuous usage
- **Exceptions** (Lecture 3): Comprehensive try-except blocks
- **Libraries** (Lecture 4): requests, datetime, os, re
- **Unit Tests** (Lecture 5): Full pytest suite with mocks
- **File I/O** (Lecture 6): HTML report generation
- **Regular Expressions** (Lecture 7): City name validation
- **Object-Oriented Programming** (Lecture 8): WeatherAPI class

## 🚧 Future Enhancements

Potential features for future versions:

- **5-day Forecast**: Extended weather predictions
- **Multiple City Comparison**: Side-by-side weather comparison
- **Historical Data**: Track weather trends over time
- **Weather Alerts**: Notifications for severe weather
- **Location Detection**: Auto-detect user's location
- **Chart Generation**: Temperature/humidity graphs using matplotlib
- **Unit Preferences**: Save user's preferred temperature unit

## 📜 License

This project was created as educational material for CS50P.

## 🙏 Acknowledgments

- **CS50P Staff**: For an excellent introduction to Python programming
- **OpenWeatherMap**: For providing free weather API access
- **pytest Community**: For excellent testing framework documentation

## 👤 Author

[Your Name]  
CS50P 2024  
[Your GitHub Profile]

---

**This was CS50P!** 🎓

