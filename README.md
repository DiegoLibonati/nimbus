# Nimbus

## Educational Purpose

This project was created primarily for **educational and learning purposes**.  
While it is well-structured and could technically be used in production, it is **not intended for commercialization**.  
The main goal is to explore and demonstrate best practices, patterns, and technologies in software development.

## Getting Started

1. Clone the repository
2. Go to the repository folder and execute: `python -m venv venv`
3. Execute in Windows: `venv\Scripts\activate`
4. Execute in Linux/Mac: `source venv/bin/activate`
5. Execute: `pip install -r requirements.txt`
6. Execute: `pip install -r requirements.dev.txt`
7. Execute: `pip install -r requirements.test.txt`
8. Use `python app.py` or `python -m src` to execute the program

### Pre-Commit for Development

1. Once you're inside the virtual environment, let's install the hooks specified in the pre-commit. Execute: `pre-commit install`
2. Now every time you try to commit, the pre-commit lint will run. If you want to do it manually, you can run the command: `pre-commit run --all-files`

## Description

**Nimbus** is a desktop weather application built with Python and Tkinter that lets you look up real-time weather conditions for any city in the world. You type a city name into the search bar, and the app resolves its coordinates using the OpenStreetMap Nominatim geocoding service, then fetches live atmospheric data from the OpenWeatherMap REST API.

The results panel displays a comprehensive snapshot of current conditions: temperature (converted from Kelvin to Celsius), wind chill/feels-like temperature, humidity percentage, atmospheric pressure, wind speed, a human-readable weather description, and the local time at the searched location — accounting for the city's own timezone rather than the system clock.

Under the hood, the app follows a clean layered architecture: a `WeatherService` handles all external HTTP communication and geocoding logic, typed dialog exceptions bubble user-facing errors up through a global Tkinter exception handler, and a configuration system driven by environment variables (`DefaultConfig` → `DevelopmentConfig` / `ProductionConfig` / `TestingConfig`) keeps environment-specific settings cleanly separated. Assets and paths are resolved to work both in normal Python execution and inside a PyInstaller-bundled executable, so the app can be shipped as a single `.exe` on Windows or a standalone binary on Linux/Mac without any Python installation required on the target machine.

## Technologies used

1. Python >= 3.11
2. Tkinter

## Libraries used

#### Requirements.txt

```
geopy==2.4.1
pytz==2025.2
requests==2.32.5
timezonefinder==8.0.0
python-dotenv==1.0.1
```

#### Requirements.dev.txt
```
pre-commit==4.3.0
pip-audit==2.7.3
ruff==0.11.12
```

#### Requirements.test.txt

```
pytest==8.4.2
pytest-env==1.1.5
pytest-cov==4.1.0
pytest-timeout==2.3.1
pytest-xdist==3.5.0
```

#### Requirements.build.txt

```
pyinstaller==6.16.0
```

## Portfolio Link

[`https://www.diegolibonati.com.ar/#/project/nimbus`](https://www.diegolibonati.com.ar/#/project/nimbus)

## Testing

1. Go to the repository folder
2. Execute: `python -m venv venv`
3. Execute in Windows: `venv\Scripts\activate`
4. Execute in Linux/Mac: `source venv/bin/activate`
5. Execute: `pip install -r requirements.txt`
6. Execute: `pip install -r requirements.test.txt`
7. Execute: `pytest --log-cli-level=INFO`

## Build

You can generate a standalone executable (`.exe` on Windows, or binary on Linux/Mac) using **PyInstaller**.

### Windows

1. Go to the repository folder
2. Activate your virtual environment: `venv\Scripts\activate`
3. Install build dependencies: `pip install -r requirements.build.txt`
4. Create the executable: `pyinstaller app.spec`

Alternatively, you can run the helper script: `build.bat`

### Linux / Mac

1. Go to the repository folder
2. Activate your virtual environment: `source venv/bin/activate`
3. Install build dependencies: `pip install -r requirements.build.txt`
4. Create the executable: `pyinstaller app.spec`

Alternatively, you can run the helper script: `./build.sh`

## Security Audit

You can check your dependencies for known vulnerabilities using **pip-audit**.

1. Go to the repository folder
2. Activate your virtual environment
3. Execute: `pip install -r requirements.dev.txt`
4. Execute: `pip-audit -r requirements.txt`

## Env Keys

1. `ENVIRONMENT`: Defines the application environment. Accepts `development`, `production`, or `testing`.
2. `API_KEY`: Your api key from api.openweathermap.
3. `API_URL`: Url from api.openweathermap.org.

```
ENVIRONMENT=development
API_KEY=YOUR_API_KEY
API_URL=https://api.openweathermap.org/data/2.5
```

## Known Issues

None at the moment.
