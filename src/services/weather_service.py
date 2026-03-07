from typing import Any

import requests
from geopy.exc import GeocoderUnavailable
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder


class WeatherService:
    def __init__(self, api_key: str, api_url: str):
        self.api_key = api_key
        self.api_url = api_url
        self.geolocator = Nominatim(user_agent="weather_program")
        self.timezone_finder = TimezoneFinder()

    def get_place_information(self, place: str) -> dict[str, Any]:
        try:
            location = self.geolocator.geocode(place, timeout=30)
        except GeocoderUnavailable:
            raise ValueError("Geocoding service unavailable. Please try again later.")

        if not location:
            raise ValueError("Location not found.")

        timezone = self.timezone_finder.timezone_at(lng=location.longitude, lat=location.latitude)

        return {
            "timezone": timezone,
            "longitude": location.longitude,
            "latitude": location.latitude,
        }

    def get_weather_by_location(self, longitude: float, latitude: float) -> dict[str, Any]:
        if not longitude or not latitude:
            raise ValueError("You must enter a valid longitude and latitude.")

        if not self.api_key:
            raise ValueError("Missing API_KEY for weather request.")

        url = f"{self.api_url}/weather?lat={latitude}&lon={longitude}&appid={self.api_key}"

        response = requests.get(url=url)

        return response.json()
