from typing import Any

import requests
from geopy.exc import GeocoderUnavailable
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder

from src.constants.messages import (
    MESSAGE_ERROR_GEOCODING_SERVICE_UNAVAILABLE,
    MESSAGE_NOT_FOUND_API_KEY,
    MESSAGE_NOT_FOUND_LOCATION,
    MESSAGE_NOT_VALID_LATITUDE_AND_LONGITUDE,
)
from src.utils.dialogs import InternalDialogError, NotFoundDialogError, ValidationDialogError


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
            raise InternalDialogError(message=MESSAGE_ERROR_GEOCODING_SERVICE_UNAVAILABLE)

        if not location:
            raise NotFoundDialogError(message=MESSAGE_NOT_FOUND_LOCATION)

        timezone = self.timezone_finder.timezone_at(lng=location.longitude, lat=location.latitude)

        return {
            "timezone": timezone,
            "longitude": location.longitude,
            "latitude": location.latitude,
        }

    def get_weather_by_location(self, longitude: float, latitude: float) -> dict[str, Any]:
        if not longitude or not latitude:
            raise ValidationDialogError(message=MESSAGE_NOT_VALID_LATITUDE_AND_LONGITUDE)

        if not self.api_key:
            raise InternalDialogError(message=MESSAGE_NOT_FOUND_API_KEY)

        url = f"{self.api_url}/weather?lat={latitude}&lon={longitude}&appid={self.api_key}"

        response = requests.get(url=url)

        return response.json()
