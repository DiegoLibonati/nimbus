import os
import sys
from typing import Any
from unittest.mock import patch

from src.utils.helpers import add_zero, parse_weather_data, resource_path


class TestAddZero:
    def test_returns_string_with_leading_zero_for_single_digit(self) -> None:
        result: str = add_zero(5)
        assert result == "05"

    def test_returns_string_with_leading_zero_for_zero(self) -> None:
        result: str = add_zero(0)
        assert result == "00"

    def test_returns_string_without_leading_zero_for_ten(self) -> None:
        result: str = add_zero(10)
        assert result == "10"

    def test_returns_string_without_leading_zero_for_two_digits(self) -> None:
        result: str = add_zero(23)
        assert result == "23"

    def test_returns_string_with_leading_zero_for_nine(self) -> None:
        result: str = add_zero(9)
        assert result == "09"

    def test_returns_string_type(self) -> None:
        result: str = add_zero(3)
        assert isinstance(result, str)


class TestParseWeatherData:
    def _build_data(
        self,
        temp: float = 300.15,
        feels_like: float = 298.15,
        wind_speed: float = 5.5,
        description: str = "clear sky",
        humidity: int = 60,
        pressure: int = 1013,
    ) -> dict[str, Any]:
        return {
            "main": {
                "temp": temp,
                "feels_like": feels_like,
                "humidity": humidity,
                "pressure": pressure,
            },
            "wind": {"speed": wind_speed},
            "weather": [{"description": description}],
        }

    def test_temp_is_converted_from_kelvin_to_celsius(self) -> None:
        data: dict[str, Any] = self._build_data(temp=300.15)
        result: dict[str, Any] = parse_weather_data(data)
        assert result["temp"] == 27

    def test_feels_like_is_converted_from_kelvin_to_celsius(self) -> None:
        data: dict[str, Any] = self._build_data(feels_like=298.15)
        result: dict[str, Any] = parse_weather_data(data)
        assert result["feels_like"] == 25

    def test_temp_is_integer(self) -> None:
        data: dict[str, Any] = self._build_data(temp=300.99)
        result: dict[str, Any] = parse_weather_data(data)
        assert isinstance(result["temp"], int)

    def test_feels_like_is_integer(self) -> None:
        data: dict[str, Any] = self._build_data(feels_like=299.99)
        result: dict[str, Any] = parse_weather_data(data)
        assert isinstance(result["feels_like"], int)

    def test_wind_speed_is_returned(self) -> None:
        data: dict[str, Any] = self._build_data(wind_speed=7.2)
        result: dict[str, Any] = parse_weather_data(data)
        assert result["wind"] == 7.2

    def test_description_is_returned(self) -> None:
        data: dict[str, Any] = self._build_data(description="light rain")
        result: dict[str, Any] = parse_weather_data(data)
        assert result["description"] == "light rain"

    def test_humidity_is_returned(self) -> None:
        data: dict[str, Any] = self._build_data(humidity=80)
        result: dict[str, Any] = parse_weather_data(data)
        assert result["humidity"] == 80

    def test_pressure_is_returned(self) -> None:
        data: dict[str, Any] = self._build_data(pressure=1020)
        result: dict[str, Any] = parse_weather_data(data)
        assert result["pressure"] == 1020

    def test_result_contains_all_expected_keys(self) -> None:
        data: dict[str, Any] = self._build_data()
        result: dict[str, Any] = parse_weather_data(data)
        assert set(result.keys()) == {"temp", "feels_like", "wind", "description", "humidity", "pressure"}


class TestResourcePath:
    def test_returns_string(self) -> None:
        result: str = resource_path("some/path.png")
        assert isinstance(result, str)

    def test_path_contains_relative_path(self) -> None:
        result: str = resource_path("some/path.png")
        assert result.endswith("some/path.png")

    def test_uses_meipass_when_available(self) -> None:
        with patch.object(sys, "_MEIPASS", "/frozen/base", create=True):
            result: str = resource_path("assets/image.png")
        assert result == os.path.join("/frozen/base", "assets/image.png")

    def test_uses_abspath_when_meipass_not_available(self) -> None:
        result: str = resource_path("assets/image.png")
        expected: str = os.path.join(os.path.abspath("."), "assets/image.png")
        assert result == expected
