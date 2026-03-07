from tkinter import StringVar
from unittest.mock import MagicMock, patch

import pytest

from src.ui.components.weather_information import WeatherInformation


@pytest.fixture
def weather_information(mock_styles: MagicMock, mock_img: MagicMock) -> WeatherInformation:
    with (
        patch("src.ui.components.weather_information.Frame.__init__", return_value=None),
        patch("src.ui.components.weather_information.Label"),
        patch("src.ui.components.weather_information.StringVar"),
    ):
        instance: WeatherInformation = WeatherInformation.__new__(WeatherInformation)
        instance._styles = mock_styles
        instance._img_box = mock_img
        instance._wind_text = MagicMock(spec=StringVar)
        instance._wind_value = MagicMock(spec=StringVar)
        instance._humidity_text = MagicMock(spec=StringVar)
        instance._humidity_value = MagicMock(spec=StringVar)
        instance._description_text = MagicMock(spec=StringVar)
        instance._description_value = MagicMock(spec=StringVar)
        instance._pressure_text = MagicMock(spec=StringVar)
        instance._pressure_value = MagicMock(spec=StringVar)
        return instance


class TestWeatherInformationInit:
    def test_stores_styles(self, weather_information: WeatherInformation, mock_styles: MagicMock) -> None:
        assert weather_information._styles == mock_styles

    def test_stores_img_box(self, weather_information: WeatherInformation, mock_img: MagicMock) -> None:
        assert weather_information._img_box == mock_img

    def test_eight_string_vars_are_created(self, mock_styles: MagicMock, mock_img: MagicMock) -> None:
        with (
            patch("src.ui.components.weather_information.Frame.__init__", return_value=None),
            patch("src.ui.components.weather_information.Label") as mock_label,
            patch("src.ui.components.weather_information.StringVar") as mock_string_var,
        ):
            mock_label.return_value.pack = MagicMock()
            mock_label.return_value.place = MagicMock()
            instance: WeatherInformation = WeatherInformation.__new__(WeatherInformation)
            instance._styles = mock_styles
            WeatherInformation.__init__(instance, parent=MagicMock(), styles=mock_styles, img_box=mock_img)

        assert mock_string_var.call_count == 8


class TestWeatherInformationSetValues:
    def test_wind_text_is_set(self, weather_information: WeatherInformation) -> None:
        weather_information.set_values({"wind": 5.5, "humidity": 60, "description": "clear sky", "pressure": 1013})
        weather_information._wind_text.set.assert_called_once_with("WIND")

    def test_humidity_text_is_set(self, weather_information: WeatherInformation) -> None:
        weather_information.set_values({"wind": 5.5, "humidity": 60, "description": "clear sky", "pressure": 1013})
        weather_information._humidity_text.set.assert_called_once_with("HUMIDITY")

    def test_description_text_is_set(self, weather_information: WeatherInformation) -> None:
        weather_information.set_values({"wind": 5.5, "humidity": 60, "description": "clear sky", "pressure": 1013})
        weather_information._description_text.set.assert_called_once_with("DESCRIPTION")

    def test_pressure_text_is_set(self, weather_information: WeatherInformation) -> None:
        weather_information.set_values({"wind": 5.5, "humidity": 60, "description": "clear sky", "pressure": 1013})
        weather_information._pressure_text.set.assert_called_once_with("PRESSURE")

    def test_wind_value_is_set(self, weather_information: WeatherInformation) -> None:
        weather_information.set_values({"wind": 5.5, "humidity": 60, "description": "clear sky", "pressure": 1013})
        weather_information._wind_value.set.assert_called_once_with(5.5)

    def test_humidity_value_is_set(self, weather_information: WeatherInformation) -> None:
        weather_information.set_values({"wind": 5.5, "humidity": 60, "description": "clear sky", "pressure": 1013})
        weather_information._humidity_value.set.assert_called_once_with(60)

    def test_description_value_is_set(self, weather_information: WeatherInformation) -> None:
        weather_information.set_values({"wind": 5.5, "humidity": 60, "description": "clear sky", "pressure": 1013})
        weather_information._description_value.set.assert_called_once_with("clear sky")

    def test_pressure_value_is_set(self, weather_information: WeatherInformation) -> None:
        weather_information.set_values({"wind": 5.5, "humidity": 60, "description": "clear sky", "pressure": 1013})
        weather_information._pressure_value.set.assert_called_once_with(1013)
