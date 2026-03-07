from typing import Any
from unittest.mock import MagicMock, patch

import pytest
from geopy.exc import GeocoderUnavailable

from src.services.weather_service import WeatherService


@pytest.fixture
def weather_service() -> WeatherService:
    with (
        patch("src.services.weather_service.Nominatim"),
        patch("src.services.weather_service.TimezoneFinder"),
    ):
        service: WeatherService = WeatherService(api_key="test_key", api_url="http://test.api")
        return service


class TestWeatherServiceInit:
    def test_stores_api_key(self, weather_service: WeatherService) -> None:
        assert weather_service.api_key == "test_key"

    def test_stores_api_url(self, weather_service: WeatherService) -> None:
        assert weather_service.api_url == "http://test.api"


class TestGetPlaceInformation:
    def test_returns_dict_with_timezone_longitude_latitude(self, weather_service: WeatherService) -> None:
        mock_location: MagicMock = MagicMock()
        mock_location.longitude = -58.3816
        mock_location.latitude = -34.6037

        weather_service.geolocator.geocode.return_value = mock_location
        weather_service.timezone_finder.timezone_at.return_value = "America/Argentina/Buenos_Aires"

        result: dict[str, Any] = weather_service.get_place_information("Buenos Aires")

        assert result["timezone"] == "America/Argentina/Buenos_Aires"
        assert result["longitude"] == -58.3816
        assert result["latitude"] == -34.6037

    def test_raises_value_error_when_location_not_found(self, weather_service: WeatherService) -> None:
        weather_service.geolocator.geocode.return_value = None

        with pytest.raises(ValueError, match="Location not found."):
            weather_service.get_place_information("nonexistent place xyz")

    def test_raises_value_error_when_geocoder_unavailable(self, weather_service: WeatherService) -> None:
        weather_service.geolocator.geocode.side_effect = GeocoderUnavailable()

        with pytest.raises(ValueError, match="Geocoding service unavailable"):
            weather_service.get_place_information("Buenos Aires")

    def test_geocode_called_with_place_and_timeout(self, weather_service: WeatherService) -> None:
        mock_location: MagicMock = MagicMock()
        mock_location.longitude = -58.3816
        mock_location.latitude = -34.6037

        weather_service.geolocator.geocode.return_value = mock_location
        weather_service.timezone_finder.timezone_at.return_value = "America/Argentina/Buenos_Aires"

        weather_service.get_place_information("Buenos Aires")

        weather_service.geolocator.geocode.assert_called_once_with("Buenos Aires", timeout=30)

    def test_timezone_finder_called_with_correct_coords(self, weather_service: WeatherService) -> None:
        mock_location: MagicMock = MagicMock()
        mock_location.longitude = -58.3816
        mock_location.latitude = -34.6037

        weather_service.geolocator.geocode.return_value = mock_location
        weather_service.timezone_finder.timezone_at.return_value = "America/Argentina/Buenos_Aires"

        weather_service.get_place_information("Buenos Aires")

        weather_service.timezone_finder.timezone_at.assert_called_once_with(lng=-58.3816, lat=-34.6037)


class TestGetWeatherByLocation:
    def test_returns_json_response(self, weather_service: WeatherService) -> None:
        mock_response: MagicMock = MagicMock()
        mock_response.json.return_value = {"weather": "data"}

        with patch("src.services.weather_service.requests.get", return_value=mock_response):
            result: dict[str, Any] = weather_service.get_weather_by_location(longitude=-58.0, latitude=-34.0)

        assert result == {"weather": "data"}

    def test_raises_value_error_when_longitude_is_zero(self, weather_service: WeatherService) -> None:
        with pytest.raises(ValueError, match="valid longitude and latitude"):
            weather_service.get_weather_by_location(longitude=0, latitude=-34.0)

    def test_raises_value_error_when_latitude_is_zero(self, weather_service: WeatherService) -> None:
        with pytest.raises(ValueError, match="valid longitude and latitude"):
            weather_service.get_weather_by_location(longitude=-58.0, latitude=0)

    def test_raises_value_error_when_api_key_is_empty(self, weather_service: WeatherService) -> None:
        weather_service.api_key = ""

        with pytest.raises(ValueError, match="Missing API_KEY"):
            weather_service.get_weather_by_location(longitude=-58.0, latitude=-34.0)

    def test_requests_get_called_with_correct_url(self, weather_service: WeatherService) -> None:
        mock_response: MagicMock = MagicMock()
        mock_response.json.return_value = {}

        with patch("src.services.weather_service.requests.get", return_value=mock_response) as mock_get:
            weather_service.get_weather_by_location(longitude=-58.0, latitude=-34.0)

        expected_url: str = "http://test.api/weather?lat=-34.0&lon=-58.0&appid=test_key"
        mock_get.assert_called_once_with(url=expected_url)
