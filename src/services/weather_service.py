from typing import Any

import requests
from geopy.exc import GeocoderUnavailable
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder

from src.constants.messages import (
    MESSAGE_ERROR_API_KEY_NOT_FOUND,
    MESSAGE_ERROR_GEOCODING_SERVICE_UNAVAILABLE,
    MESSAGE_ERROR_LOCATION_NOT_FOUND,
    MESSAGE_ERROR_NOT_VALID_LATITUDE_AND_LONGITUDE,
)


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
            raise ValueError(MESSAGE_ERROR_GEOCODING_SERVICE_UNAVAILABLE)

        if not location:
            raise ValueError(MESSAGE_ERROR_LOCATION_NOT_FOUND)

        timezone = self.timezone_finder.timezone_at(lng=location.longitude, lat=location.latitude)

        return {
            "timezone": timezone,
            "longitude": location.longitude,
            "latitude": location.latitude,
        }

    def get_weather_by_location(self, longitude: float, latitude: float) -> dict[str, Any]:
        if not longitude or not latitude:
            raise ValueError(MESSAGE_ERROR_NOT_VALID_LATITUDE_AND_LONGITUDE)

        if not self.api_key:
            raise ValueError(MESSAGE_ERROR_API_KEY_NOT_FOUND)

        url = f"{self.api_url}/weather?lat={latitude}&lon={longitude}&appid={self.api_key}"

        response = requests.get(url=url)

        return response.json()
