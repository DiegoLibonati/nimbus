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


@pytest.fixture
def weather_service() -> WeatherService:
    with (
        patch("src.services.weather_service.Nominatim"),
        patch("src.services.weather_service.TimezoneFinder"),
    ):
        return WeatherService(api_key="test_api_key", api_url="https://api.example.com")


@pytest.fixture
def weather_service_no_key() -> WeatherService:
    with (
        patch("src.services.weather_service.Nominatim"),
        patch("src.services.weather_service.TimezoneFinder"),
    ):
        return WeatherService(api_key="", api_url="https://api.example.com")


class TestWeatherServiceInit:
    def test_stores_api_key(self, weather_service: WeatherService) -> None:
        assert weather_service.api_key == "test_api_key"

    def test_stores_api_url(self, weather_service: WeatherService) -> None:
        assert weather_service.api_url == "https://api.example.com"

    def test_geolocator_is_set(self, weather_service: WeatherService) -> None:
        assert weather_service.geolocator is not None

    def test_timezone_finder_is_set(self, weather_service: WeatherService) -> None:
        assert weather_service.timezone_finder is not None


class TestWeatherServiceGetPlaceInformation:
    def test_returns_dict_with_timezone_longitude_latitude(self, weather_service: WeatherService) -> None:
        mock_location: MagicMock = MagicMock()
        mock_location.longitude = -58.38
        mock_location.latitude = -34.60
        weather_service.geolocator.geocode.return_value = mock_location
        weather_service.timezone_finder.timezone_at.return_value = "America/Argentina/Buenos_Aires"

        result: dict[str, Any] = weather_service.get_place_information("Buenos Aires")

        assert result["timezone"] == "America/Argentina/Buenos_Aires"
        assert result["longitude"] == -58.38
        assert result["latitude"] == -34.60

    def test_returns_none_when_geocoder_unavailable(self, weather_service: WeatherService) -> None:
        weather_service.geolocator.geocode.side_effect = GeocoderUnavailable()

        with patch("src.services.weather_service.InternalDialogError") as mock_dialog_class:
            mock_dialog_class.return_value = MagicMock()
            result = weather_service.get_place_information("Buenos Aires")

        assert result is None

    def test_internal_dialog_called_when_geocoder_unavailable(self, weather_service: WeatherService) -> None:
        weather_service.geolocator.geocode.side_effect = GeocoderUnavailable()

        with patch("src.services.weather_service.InternalDialogError") as mock_dialog_class:
            mock_dialog: MagicMock = MagicMock()
            mock_dialog_class.return_value = mock_dialog
            weather_service.get_place_information("Buenos Aires")

        mock_dialog_class.assert_called_once_with(message=MESSAGE_ERROR_GEOCODING_SERVICE_UNAVAILABLE)
        mock_dialog.dialog.assert_called_once()

    def test_returns_none_when_location_not_found(self, weather_service: WeatherService) -> None:
        weather_service.geolocator.geocode.return_value = None

        with patch("src.services.weather_service.NotFoundDialogError") as mock_dialog_class:
            mock_dialog_class.return_value = MagicMock()
            result = weather_service.get_place_information("nonexistent place xyz")

        assert result is None

    def test_not_found_dialog_called_when_location_is_none(self, weather_service: WeatherService) -> None:
        weather_service.geolocator.geocode.return_value = None

        with patch("src.services.weather_service.NotFoundDialogError") as mock_dialog_class:
            mock_dialog: MagicMock = MagicMock()
            mock_dialog_class.return_value = mock_dialog
            weather_service.get_place_information("nonexistent place xyz")

        mock_dialog_class.assert_called_once_with(message=MESSAGE_NOT_FOUND_LOCATION)
        mock_dialog.dialog.assert_called_once()

    def test_timezone_finder_called_with_correct_coords(self, weather_service: WeatherService) -> None:
        mock_location: MagicMock = MagicMock()
        mock_location.longitude = -58.38
        mock_location.latitude = -34.60
        weather_service.geolocator.geocode.return_value = mock_location
        weather_service.timezone_finder.timezone_at.return_value = "America/Argentina/Buenos_Aires"

        weather_service.get_place_information("Buenos Aires")

        weather_service.timezone_finder.timezone_at.assert_called_once_with(lng=-58.38, lat=-34.60)

    def test_geocode_called_with_place_and_timeout(self, weather_service: WeatherService) -> None:
        mock_location: MagicMock = MagicMock()
        mock_location.longitude = -58.38
        mock_location.latitude = -34.60
        weather_service.geolocator.geocode.return_value = mock_location
        weather_service.timezone_finder.timezone_at.return_value = "America/Argentina/Buenos_Aires"

        weather_service.get_place_information("Buenos Aires")

        weather_service.geolocator.geocode.assert_called_once_with("Buenos Aires", timeout=30)


class TestWeatherServiceGetWeatherByLocation:
    def test_returns_none_when_longitude_is_zero(self, weather_service: WeatherService) -> None:
        with patch("src.services.weather_service.ValidationDialogError") as mock_dialog_class:
            mock_dialog_class.return_value = MagicMock()
            result = weather_service.get_weather_by_location(longitude=0, latitude=-34.60)

        assert result is None

    def test_returns_none_when_latitude_is_zero(self, weather_service: WeatherService) -> None:
        with patch("src.services.weather_service.ValidationDialogError") as mock_dialog_class:
            mock_dialog_class.return_value = MagicMock()
            result = weather_service.get_weather_by_location(longitude=-58.38, latitude=0)

        assert result is None

    def test_validation_dialog_called_when_coords_are_zero(self, weather_service: WeatherService) -> None:
        with patch("src.services.weather_service.ValidationDialogError") as mock_dialog_class:
            mock_dialog: MagicMock = MagicMock()
            mock_dialog_class.return_value = mock_dialog
            weather_service.get_weather_by_location(longitude=0, latitude=0)

        mock_dialog_class.assert_called_once_with(message=MESSAGE_NOT_VALID_LATITUDE_AND_LONGITUDE)
        mock_dialog.dialog.assert_called_once()

    def test_returns_none_when_api_key_is_empty(self, weather_service_no_key: WeatherService) -> None:
        with patch("src.services.weather_service.InternalDialogError") as mock_dialog_class:
            mock_dialog_class.return_value = MagicMock()
            result = weather_service_no_key.get_weather_by_location(longitude=-58.38, latitude=-34.60)

        assert result is None

    def test_internal_dialog_called_when_api_key_missing(self, weather_service_no_key: WeatherService) -> None:
        with patch("src.services.weather_service.InternalDialogError") as mock_dialog_class:
            mock_dialog: MagicMock = MagicMock()
            mock_dialog_class.return_value = mock_dialog
            weather_service_no_key.get_weather_by_location(longitude=-58.38, latitude=-34.60)

        mock_dialog_class.assert_called_once_with(message=MESSAGE_NOT_FOUND_API_KEY)
        mock_dialog.dialog.assert_called_once()

    def test_returns_json_response_on_success(self, weather_service: WeatherService) -> None:
        mock_response: MagicMock = MagicMock()
        mock_response.json.return_value = {"weather": "sunny"}

        with patch("src.services.weather_service.requests.get", return_value=mock_response):
            result: dict[str, Any] = weather_service.get_weather_by_location(longitude=-58.38, latitude=-34.60)

        assert result == {"weather": "sunny"}

    def test_requests_get_called_with_correct_url(self, weather_service: WeatherService) -> None:
        mock_response: MagicMock = MagicMock()
        mock_response.json.return_value = {}

        with patch("src.services.weather_service.requests.get", return_value=mock_response) as mock_get:
            weather_service.get_weather_by_location(longitude=-58.38, latitude=-34.60)

        expected_url: str = "https://api.example.com/weather?lat=-34.6&lon=-58.38&appid=test_api_key"
        mock_get.assert_called_once_with(url=expected_url)
