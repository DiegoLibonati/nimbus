from typing import Any
from unittest.mock import MagicMock, patch

import pytest
from geopy.exc import GeocoderUnavailable

from src.services.weather_service import WeatherService
from src.utils.dialogs import InternalDialogError, NotFoundDialogError, ValidationDialogError


class TestWeatherService:
    def test_initialization_stores_api_key(self) -> None:
        service: WeatherService = WeatherService(api_key="my_key", api_url="http://api.example.com")
        assert service.api_key == "my_key"

    def test_initialization_stores_api_url(self) -> None:
        service: WeatherService = WeatherService(api_key="my_key", api_url="http://api.example.com")
        assert service.api_url == "http://api.example.com"

    def test_get_place_information_returns_timezone(self) -> None:
        service: WeatherService = WeatherService(api_key="key", api_url="http://api.example.com")
        service.timezone_finder = MagicMock()
        service.timezone_finder.timezone_at.return_value = "America/Argentina/Buenos_Aires"
        mock_location: MagicMock = MagicMock()
        mock_location.latitude = -34.6
        mock_location.longitude = -58.4
        with patch.object(service.geolocator, "geocode", return_value=mock_location):
            result: dict[str, Any] = service.get_place_information("Buenos Aires")
            assert result["timezone"] == "America/Argentina/Buenos_Aires"

    def test_get_place_information_returns_latitude(self) -> None:
        service: WeatherService = WeatherService(api_key="key", api_url="http://api.example.com")
        service.timezone_finder = MagicMock()
        service.timezone_finder.timezone_at.return_value = "America/Argentina/Buenos_Aires"
        mock_location: MagicMock = MagicMock()
        mock_location.latitude = -34.6
        mock_location.longitude = -58.4
        with patch.object(service.geolocator, "geocode", return_value=mock_location):
            result: dict[str, Any] = service.get_place_information("Buenos Aires")
            assert result["latitude"] == -34.6

    def test_get_place_information_returns_longitude(self) -> None:
        service: WeatherService = WeatherService(api_key="key", api_url="http://api.example.com")
        service.timezone_finder = MagicMock()
        service.timezone_finder.timezone_at.return_value = "America/Argentina/Buenos_Aires"
        mock_location: MagicMock = MagicMock()
        mock_location.latitude = -34.6
        mock_location.longitude = -58.4
        with patch.object(service.geolocator, "geocode", return_value=mock_location):
            result: dict[str, Any] = service.get_place_information("Buenos Aires")
            assert result["longitude"] == -58.4

    def test_get_place_information_raises_not_found_when_no_location(self) -> None:
        service: WeatherService = WeatherService(api_key="key", api_url="http://api.example.com")
        with patch.object(service.geolocator, "geocode", return_value=None):
            with pytest.raises(NotFoundDialogError):
                service.get_place_information("nonexistent_xyz_place")

    def test_get_place_information_raises_internal_on_geocoder_unavailable(self) -> None:
        service: WeatherService = WeatherService(api_key="key", api_url="http://api.example.com")
        with patch.object(service.geolocator, "geocode", side_effect=GeocoderUnavailable()):
            with pytest.raises(InternalDialogError):
                service.get_place_information("Buenos Aires")

    def test_get_weather_by_location_returns_json(self) -> None:
        service: WeatherService = WeatherService(api_key="key", api_url="http://api.example.com")
        mock_response: MagicMock = MagicMock()
        mock_response.json.return_value = {"weather": [{"description": "clear sky"}]}
        with patch("src.services.weather_service.requests.get", return_value=mock_response):
            result: dict[str, Any] = service.get_weather_by_location(longitude=-58.4, latitude=-34.6)
            assert result == {"weather": [{"description": "clear sky"}]}

    def test_get_weather_by_location_raises_validation_on_zero_coords(self) -> None:
        service: WeatherService = WeatherService(api_key="key", api_url="http://api.example.com")
        with pytest.raises(ValidationDialogError):
            service.get_weather_by_location(longitude=0.0, latitude=0.0)

    def test_get_weather_by_location_raises_validation_on_zero_longitude(self) -> None:
        service: WeatherService = WeatherService(api_key="key", api_url="http://api.example.com")
        with pytest.raises(ValidationDialogError):
            service.get_weather_by_location(longitude=0.0, latitude=-34.6)

    def test_get_weather_by_location_raises_internal_on_empty_api_key(self) -> None:
        service: WeatherService = WeatherService(api_key="", api_url="http://api.example.com")
        with pytest.raises(InternalDialogError):
            service.get_weather_by_location(longitude=-58.4, latitude=-34.6)

    def test_get_weather_url_contains_latitude(self) -> None:
        service: WeatherService = WeatherService(api_key="my_key", api_url="http://api.example.com")
        mock_response: MagicMock = MagicMock()
        mock_response.json.return_value = {}
        with patch("src.services.weather_service.requests.get", return_value=mock_response) as mock_get:
            service.get_weather_by_location(longitude=-58.4, latitude=-34.6)
            called_url: str = mock_get.call_args.kwargs["url"]
            assert "lat=-34.6" in called_url

    def test_get_weather_url_contains_longitude(self) -> None:
        service: WeatherService = WeatherService(api_key="my_key", api_url="http://api.example.com")
        mock_response: MagicMock = MagicMock()
        mock_response.json.return_value = {}
        with patch("src.services.weather_service.requests.get", return_value=mock_response) as mock_get:
            service.get_weather_by_location(longitude=-58.4, latitude=-34.6)
            called_url: str = mock_get.call_args.kwargs["url"]
            assert "lon=-58.4" in called_url

    def test_get_weather_url_contains_api_key(self) -> None:
        service: WeatherService = WeatherService(api_key="my_key", api_url="http://api.example.com")
        mock_response: MagicMock = MagicMock()
        mock_response.json.return_value = {}
        with patch("src.services.weather_service.requests.get", return_value=mock_response) as mock_get:
            service.get_weather_by_location(longitude=-58.4, latitude=-34.6)
            called_url: str = mock_get.call_args.kwargs["url"]
            assert "appid=my_key" in called_url
