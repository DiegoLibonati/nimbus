import os
import sys
from typing import Any
from unittest.mock import patch

from src.utils.helpers import add_zero, parse_weather_data, resource_path


class TestAddZero:
    def test_single_digit_gets_leading_zero(self) -> None:
        assert add_zero(5) == "05"

    def test_zero_gets_leading_zero(self) -> None:
        assert add_zero(0) == "00"

    def test_nine_gets_leading_zero(self) -> None:
        assert add_zero(9) == "09"

    def test_ten_has_no_leading_zero(self) -> None:
        assert add_zero(10) == "10"

    def test_large_number_has_no_leading_zero(self) -> None:
        assert add_zero(59) == "59"

    def test_negative_number_has_no_leading_zero(self) -> None:
        assert add_zero(-1) == "-1"

    def test_returns_string(self) -> None:
        result: str = add_zero(3)
        assert isinstance(result, str)


class TestParseWeatherData:
    def _sample_data(self) -> dict[str, Any]:
        return {
            "main": {
                "temp": 300.15,
                "feels_like": 298.15,
                "humidity": 65,
                "pressure": 1013,
            },
            "wind": {"speed": 5.2},
            "weather": [{"description": "clear sky"}],
        }

    def test_temp_converted_from_kelvin(self) -> None:
        result: dict[str, Any] = parse_weather_data(self._sample_data())
        assert result["temp"] == 27

    def test_feels_like_converted_from_kelvin(self) -> None:
        result: dict[str, Any] = parse_weather_data(self._sample_data())
        assert result["feels_like"] == 25

    def test_wind_speed_value(self) -> None:
        result: dict[str, Any] = parse_weather_data(self._sample_data())
        assert result["wind"] == 5.2

    def test_description_value(self) -> None:
        result: dict[str, Any] = parse_weather_data(self._sample_data())
        assert result["description"] == "clear sky"

    def test_humidity_value(self) -> None:
        result: dict[str, Any] = parse_weather_data(self._sample_data())
        assert result["humidity"] == 65

    def test_pressure_value(self) -> None:
        result: dict[str, Any] = parse_weather_data(self._sample_data())
        assert result["pressure"] == 1013

    def test_temp_is_int(self) -> None:
        result: dict[str, Any] = parse_weather_data(self._sample_data())
        assert isinstance(result["temp"], int)

    def test_feels_like_is_int(self) -> None:
        result: dict[str, Any] = parse_weather_data(self._sample_data())
        assert isinstance(result["feels_like"], int)

    def test_temp_truncates_decimal(self) -> None:
        data: dict[str, Any] = self._sample_data()
        data["main"]["temp"] = 300.99
        result: dict[str, Any] = parse_weather_data(data)
        assert result["temp"] == 27

    def test_output_has_all_expected_keys(self) -> None:
        result: dict[str, Any] = parse_weather_data(self._sample_data())
        expected_keys: list[str] = ["temp", "feels_like", "wind", "description", "humidity", "pressure"]
        for key in expected_keys:
            assert key in result


class TestResourcePath:
    def test_returns_string(self) -> None:
        result: str = resource_path("some/path.png")
        assert isinstance(result, str)

    def test_path_ends_with_filename(self) -> None:
        result: str = resource_path("assets/image.png")
        assert result.endswith("image.png")

    def test_uses_cwd_as_base_without_meipass(self) -> None:
        result: str = resource_path("assets/image.png")
        expected: str = os.path.join(os.path.abspath("."), "assets/image.png")
        assert result == expected

    def test_uses_meipass_when_attribute_exists(self) -> None:
        with patch.object(sys, "_MEIPASS", "/frozen/base", create=True):
            result: str = resource_path("assets/image.png")
            assert result.startswith("/frozen/base")
