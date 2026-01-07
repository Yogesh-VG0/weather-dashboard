"""
HTML Report Generator
Creates beautiful weather reports with visualizations
"""

import os
import webbrowser
from datetime import datetime
from config import REPORTS_DIR


def get_weather_icon(description, icon_code='01d'):
    """
    Get SVG weather icon based on description and time of day
    
    Args:
        description (str): Weather description
        icon_code (str): OpenWeatherMap icon code (e.g., '01d' for day, '01n' for night)
        
    Returns:
        str: SVG icon HTML
    """
    description = description.lower()
    is_night = icon_code.endswith('n')
    
    if 'clear' in description:
        if is_night:
            # Moon icon for clear night
            return '''<svg xmlns="http://www.w3.org/2000/svg" width="80" height="80" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path>
            </svg>'''
        else:
            # Sun icon for clear day
            return '''<svg xmlns="http://www.w3.org/2000/svg" width="80" height="80" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <circle cx="12" cy="12" r="5"></circle>
                <line x1="12" y1="1" x2="12" y2="3"></line>
                <line x1="12" y1="21" x2="12" y2="23"></line>
                <line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line>
                <line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line>
                <line x1="1" y1="12" x2="3" y2="12"></line>
                <line x1="21" y1="12" x2="23" y2="12"></line>
                <line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line>
                <line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line>
            </svg>'''
    elif 'cloud' in description:
        return '''<svg xmlns="http://www.w3.org/2000/svg" width="80" height="80" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M18 10h-1.26A8 8 0 1 0 9 20h9a5 5 0 0 0 0-10z"></path>
        </svg>'''
    elif 'rain' in description:
        return '''<svg xmlns="http://www.w3.org/2000/svg" width="80" height="80" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <line x1="16" y1="13" x2="16" y2="21"></line>
            <line x1="8" y1="13" x2="8" y2="21"></line>
            <line x1="12" y1="15" x2="12" y2="23"></line>
            <path d="M20 16.58A5 5 0 0 0 18 7h-1.26A8 8 0 1 0 4 15.25"></path>
        </svg>'''
    elif 'snow' in description:
        return '''<svg xmlns="http://www.w3.org/2000/svg" width="80" height="80" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M20 17.58A5 5 0 0 0 18 8h-1.26A8 8 0 1 0 4 16.25"></path>
            <line x1="8" y1="16" x2="8.01" y2="16"></line>
            <line x1="8" y1="20" x2="8.01" y2="20"></line>
            <line x1="12" y1="18" x2="12.01" y2="18"></line>
            <line x1="12" y1="22" x2="12.01" y2="22"></line>
            <line x1="16" y1="16" x2="16.01" y2="16"></line>
            <line x1="16" y1="20" x2="16.01" y2="20"></line>
        </svg>'''
    else:
        return '''<svg xmlns="http://www.w3.org/2000/svg" width="80" height="80" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M17.5 19H9a7 7 0 1 1 6.71-9h1.79a4.5 4.5 0 1 1 0 9Z"></path>
        </svg>'''


def create_html_report(weather_data):
    """
    Generate HTML weather report
    
    Args:
        weather_data (dict): Weather data dictionary
        
    Returns:
        str: Path to generated HTML file
    """
    # Ensure reports directory exists
    os.makedirs(REPORTS_DIR, exist_ok=True)
    
    # Generate filename with timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"weather_report_{weather_data['city']}_{timestamp}.html"
    filepath = os.path.join(REPORTS_DIR, filename)
    
    # Get weather icon (pass icon code for day/night detection)
    icon_code = weather_data.get('icon', '01d')
    weather_icon = get_weather_icon(weather_data['description'], icon_code)
    
    # Generate HTML content
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Weather Report - {weather_data['city']}</title>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root {{
            --primary: #0ea5e9;
            --primary-dark: #0284c7;
            --secondary: #f97316;
            --bg-gradient-start: #0f172a;
            --bg-gradient-end: #1e3a5f;
            --card-bg: rgba(255, 255, 255, 0.1);
            --text-primary: #f8fafc;
            --text-secondary: #94a3b8;
        }}
        
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Outfit', sans-serif;
            background: linear-gradient(135deg, var(--bg-gradient-start) 0%, var(--bg-gradient-end) 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
            color: var(--text-primary);
        }}
        
        .container {{
            background: var(--card-bg);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 24px;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
            max-width: 900px;
            width: 100%;
            padding: 48px;
            animation: fadeIn 0.6s ease-out;
        }}
        
        @keyframes fadeIn {{
            from {{
                opacity: 0;
                transform: translateY(20px);
            }}
            to {{
                opacity: 1;
                transform: translateY(0);
            }}
        }}
        
        .header {{
            text-align: center;
            margin-bottom: 40px;
        }}
        
        .header h1 {{
            font-size: 2.5rem;
            font-weight: 700;
            background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 8px;
        }}
        
        .location {{
            font-size: 1.25rem;
            color: var(--text-secondary);
            font-weight: 300;
        }}
        
        .main-weather {{
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 48px;
            margin: 48px 0;
            padding: 40px;
            background: linear-gradient(135deg, var(--primary) 0%, var(--primary-dark) 100%);
            border-radius: 20px;
            flex-wrap: wrap;
        }}
        
        .weather-icon {{
            color: white;
            opacity: 0.9;
            animation: pulse 2s ease-in-out infinite;
        }}
        
        @keyframes pulse {{
            0%, 100% {{ transform: scale(1); }}
            50% {{ transform: scale(1.05); }}
        }}
        
        .temperature-container {{
            text-align: center;
        }}
        
        .temperature {{
            font-size: 5rem;
            font-weight: 700;
            line-height: 1;
        }}
        
        .description {{
            font-size: 1.5rem;
            text-transform: capitalize;
            opacity: 0.9;
            margin-top: 8px;
            font-weight: 300;
        }}
        
        .details-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
            gap: 20px;
            margin-top: 32px;
        }}
        
        .detail-card {{
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.1);
            padding: 24px;
            border-radius: 16px;
            text-align: center;
            transition: transform 0.3s ease, background 0.3s ease;
        }}
        
        .detail-card:hover {{
            transform: translateY(-4px);
            background: rgba(255, 255, 255, 0.1);
        }}
        
        .detail-card .label {{
            color: var(--text-secondary);
            font-size: 0.875rem;
            margin-bottom: 8px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }}
        
        .detail-card .value {{
            font-size: 1.75rem;
            font-weight: 600;
            color: var(--text-primary);
        }}
        
        .detail-card .unit {{
            font-size: 0.875rem;
            color: var(--text-secondary);
            font-weight: 400;
        }}
        
        .timestamp-card {{
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.1);
            padding: 16px 24px;
            border-radius: 12px;
            margin-top: 32px;
            text-align: center;
        }}
        
        .timestamp-card .label {{
            color: var(--text-secondary);
            font-size: 0.875rem;
        }}
        
        .timestamp-card .value {{
            color: var(--text-primary);
            font-weight: 500;
        }}
        
        .footer {{
            text-align: center;
            margin-top: 40px;
            padding-top: 24px;
            border-top: 1px solid rgba(255, 255, 255, 0.1);
        }}
        
        .footer p {{
            color: var(--text-secondary);
            font-size: 0.875rem;
            margin: 4px 0;
        }}
        
        .footer .brand {{
            color: var(--primary);
            font-weight: 600;
        }}
        
        @media (max-width: 600px) {{
            .container {{
                padding: 24px;
            }}
            
            .header h1 {{
                font-size: 1.75rem;
            }}
            
            .temperature {{
                font-size: 3.5rem;
            }}
            
            .main-weather {{
                padding: 24px;
                gap: 24px;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🌤️ Weather Report</h1>
            <div class="location">{weather_data['city']}, {weather_data['country']}</div>
        </div>
        
        <div class="main-weather">
            <div class="weather-icon">
                {weather_icon}
            </div>
            <div class="temperature-container">
                <div class="temperature">{weather_data['temperature']}</div>
                <div class="description">{weather_data['description']}</div>
            </div>
        </div>
        
        <div class="details-grid">
            <div class="detail-card">
                <div class="label">Feels Like</div>
                <div class="value">{weather_data['feels_like']}</div>
            </div>
            
            <div class="detail-card">
                <div class="label">Humidity</div>
                <div class="value">{weather_data['humidity']}<span class="unit">%</span></div>
            </div>
            
            <div class="detail-card">
                <div class="label">Wind Speed</div>
                <div class="value">{weather_data['wind_speed']}<span class="unit"> m/s</span></div>
            </div>
            
            <div class="detail-card">
                <div class="label">Pressure</div>
                <div class="value">{weather_data['pressure']}<span class="unit"> hPa</span></div>
            </div>
        </div>
        
        <div class="timestamp-card">
            <span class="label">Last Updated: </span>
            <span class="value">{weather_data['timestamp']}</span>
        </div>
        
        <div class="footer">
            <p>Created with <span class="brand">WeatherWise CLI Dashboard</span></p>
            <p>Data provided by OpenWeatherMap API</p>
        </div>
    </div>
</body>
</html>"""
    
    # Write HTML file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    # Open the report in the default web browser
    webbrowser.open('file://' + os.path.realpath(filepath))
    
    return filepath

