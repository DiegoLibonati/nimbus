from typing import Any
from unittest.mock import MagicMock, patch

import pytest
from geopy.exc import GeocoderUnavailable

from src.constants.messages import (
    MESSAGE_ERROR_GEOCODING_SERVICE_UNAVAILABLE,
    MESSAGE_NOT_FOUND_API_KEY,
    MESSAGE_NOT_FOUND_LOCATION,
    MESSAGE_NOT_VALID_LATITUDE_AND_LONGITUDE,
)
from src.services.weather_service import WeatherService
from src.utils.dialogs import InternalDialogError, NotFoundDialogError, ValidationDialogError


@pytest.fixture
def weather_service() -> WeatherService:
    with (
        patch("src.services.weather_service.Nominatim"),
        patch("src.services.weather_service.TimezoneFinder"),
    ):
        return WeatherService(api_key="test_api_key", api_url="https://api.example.com")


class TestWeatherServiceInit:
    def test_stores_api_key(self, weather_service: WeatherService) -> None:
        assert weather_service.api_key == "test_api_key"

    def test_stores_api_url(self, weather_service: WeatherService) -> None:
        assert weather_service.api_url == "https://api.example.com"

    def test_geolocator_is_created(self) -> None:
        with (
            patch("src.services.weather_service.Nominatim") as mock_nominatim,
            patch("src.services.weather_service.TimezoneFinder"),
        ):
            WeatherService(api_key="key", api_url="url")
        mock_nominatim.assert_called_once_with(user_agent="weather_program")

    def test_timezone_finder_is_created(self) -> None:
        with (
            patch("src.services.weather_service.Nominatim"),
            patch("src.services.weather_service.TimezoneFinder") as mock_tf,
        ):
            WeatherService(api_key="key", api_url="url")
        mock_tf.assert_called_once()


class TestWeatherServiceGetPlaceInformation:
    def test_raises_internal_error_when_geocoder_unavailable(self, weather_service: WeatherService) -> None:
        weather_service.geolocator.geocode.side_effect = GeocoderUnavailable()
        with pytest.raises(InternalDialogError) as exc_info:
            weather_service.get_place_information("London")
        assert exc_info.value.message == MESSAGE_ERROR_GEOCODING_SERVICE_UNAVAILABLE

    def test_raises_not_found_error_when_location_is_none(self, weather_service: WeatherService) -> None:
        weather_service.geolocator.geocode.return_value = None
        with pytest.raises(NotFoundDialogError) as exc_info:
            weather_service.get_place_information("unknown place")
        assert exc_info.value.message == MESSAGE_NOT_FOUND_LOCATION

    def test_returns_dict_with_timezone(self, weather_service: WeatherService) -> None:
        mock_location: MagicMock = MagicMock()
        mock_location.longitude = -0.1276
        mock_location.latitude = 51.5074
        weather_service.geolocator.geocode.return_value = mock_location
        weather_service.timezone_finder.timezone_at.return_value = "Europe/London"

        result: dict[str, Any] = weather_service.get_place_information("London")

        assert result["timezone"] == "Europe/London"

    def test_returns_dict_with_longitude(self, weather_service: WeatherService) -> None:
        mock_location: MagicMock = MagicMock()
        mock_location.longitude = -0.1276
        mock_location.latitude = 51.5074
        weather_service.geolocator.geocode.return_value = mock_location
        weather_service.timezone_finder.timezone_at.return_value = "Europe/London"

        result: dict[str, Any] = weather_service.get_place_information("London")

        assert result["longitude"] == -0.1276

    def test_returns_dict_with_latitude(self, weather_service: WeatherService) -> None:
        mock_location: MagicMock = MagicMock()
        mock_location.longitude = -0.1276
        mock_location.latitude = 51.5074
        weather_service.geolocator.geocode.return_value = mock_location
        weather_service.timezone_finder.timezone_at.return_value = "Europe/London"

        result: dict[str, Any] = weather_service.get_place_information("London")

        assert result["latitude"] == 51.5074

    def test_geocode_called_with_place_and_timeout(self, weather_service: WeatherService) -> None:
        mock_location: MagicMock = MagicMock()
        mock_location.longitude = 0.0
        mock_location.latitude = 0.0
        weather_service.geolocator.geocode.return_value = mock_location
        weather_service.timezone_finder.timezone_at.return_value = "UTC"

        weather_service.get_place_information("Paris")

        weather_service.geolocator.geocode.assert_called_once_with("Paris", timeout=30)

    def test_timezone_finder_called_with_correct_coords(self, weather_service: WeatherService) -> None:
        mock_location: MagicMock = MagicMock()
        mock_location.longitude = 2.3522
        mock_location.latitude = 48.8566
        weather_service.geolocator.geocode.return_value = mock_location
        weather_service.timezone_finder.timezone_at.return_value = "Europe/Paris"

        weather_service.get_place_information("Paris")

        weather_service.timezone_finder.timezone_at.assert_called_once_with(lng=2.3522, lat=48.8566)


class TestWeatherServiceGetWeatherByLocation:
    def test_raises_validation_error_when_longitude_is_zero(self, weather_service: WeatherService) -> None:
        with pytest.raises(ValidationDialogError) as exc_info:
            weather_service.get_weather_by_location(longitude=0, latitude=48.8566)
        assert exc_info.value.message == MESSAGE_NOT_VALID_LATITUDE_AND_LONGITUDE

    def test_raises_validation_error_when_latitude_is_zero(self, weather_service: WeatherService) -> None:
        with pytest.raises(ValidationDialogError) as exc_info:
            weather_service.get_weather_by_location(longitude=2.3522, latitude=0)
        assert exc_info.value.message == MESSAGE_NOT_VALID_LATITUDE_AND_LONGITUDE

    def test_raises_internal_error_when_api_key_is_empty(self, weather_service: WeatherService) -> None:
        weather_service.api_key = ""
        with pytest.raises(InternalDialogError) as exc_info:
            weather_service.get_weather_by_location(longitude=2.3522, latitude=48.8566)
        assert exc_info.value.message == MESSAGE_NOT_FOUND_API_KEY

    def test_returns_response_json(self, weather_service: WeatherService) -> None:
        mock_response: MagicMock = MagicMock()
        mock_response.json.return_value = {"weather": "sunny"}

        with patch("src.services.weather_service.requests.get", return_value=mock_response):
            result: dict[str, Any] = weather_service.get_weather_by_location(longitude=2.3522, latitude=48.8566)

        assert result == {"weather": "sunny"}

    def test_requests_get_called_with_correct_url(self, weather_service: WeatherService) -> None:
        mock_response: MagicMock = MagicMock()
        mock_response.json.return_value = {}

        with patch("src.services.weather_service.requests.get", return_value=mock_response) as mock_get:
            weather_service.get_weather_by_location(longitude=2.0, latitude=48.0)

        expected_url = "https://api.example.com/weather?lat=48.0&lon=2.0&appid=test_api_key"
        mock_get.assert_called_once_with(url=expected_url)
