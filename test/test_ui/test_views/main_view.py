from tkinter import StringVar
from typing import Any
from unittest.mock import MagicMock, patch

import pytest

from src.ui.views.main_view import MainView


@pytest.fixture
def main_view(mock_root: MagicMock, mock_styles: MagicMock, mock_on_search: MagicMock, mock_img: MagicMock) -> MainView:
    with (
        patch("src.ui.views.main_view.Frame.__init__", return_value=None),
        patch("src.ui.views.main_view.SearchBar"),
        patch("src.ui.views.main_view.WeatherInformation"),
        patch("src.ui.views.main_view.Label"),
        patch("src.ui.views.main_view.StringVar"),
    ):
        instance: MainView = MainView.__new__(MainView)
        instance._styles = mock_styles
        instance._on_search = mock_on_search
        instance._img_search = mock_img
        instance._img_search_icon = mock_img
        instance._img_logo = mock_img
        instance._img_box = mock_img
        instance._label_current_weather = MagicMock(spec=StringVar)
        instance._label_time = MagicMock(spec=StringVar)
        instance._label_degrees = MagicMock(spec=StringVar)
        instance._label_thermal_sensation = MagicMock(spec=StringVar)
        instance._search_bar = MagicMock()
        instance._weather_information = MagicMock()
        return instance


class TestMainViewInit:
    def test_stores_styles(self, main_view: MainView, mock_styles: MagicMock) -> None:
        assert main_view._styles == mock_styles

    def test_stores_on_search(self, main_view: MainView, mock_on_search: MagicMock) -> None:
        assert main_view._on_search == mock_on_search

    def test_four_string_vars_are_created(self, mock_root: MagicMock, mock_styles: MagicMock, mock_on_search: MagicMock, mock_img: MagicMock) -> None:
        with (
            patch("src.ui.views.main_view.Frame.__init__", return_value=None),
            patch("src.ui.views.main_view.SearchBar") as mock_search_bar,
            patch("src.ui.views.main_view.WeatherInformation") as mock_weather_info,
            patch("src.ui.views.main_view.Label") as mock_label,
            patch("src.ui.views.main_view.StringVar") as mock_string_var,
        ):
            mock_search_bar.return_value.place = MagicMock()
            mock_weather_info.return_value.place = MagicMock()
            mock_label.return_value.place = MagicMock()
            instance: MainView = MainView.__new__(MainView)
            instance._styles = mock_styles
            MainView.__init__(
                instance,
                root=mock_root,
                styles=mock_styles,
                on_search=mock_on_search,
                img_search=mock_img,
                img_search_icon=mock_img,
                img_logo=mock_img,
                img_box=mock_img,
            )

        assert mock_string_var.call_count == 4

    def test_search_bar_receives_on_search(self, mock_root: MagicMock, mock_styles: MagicMock, mock_on_search: MagicMock, mock_img: MagicMock) -> None:
        with (
            patch("src.ui.views.main_view.Frame.__init__", return_value=None),
            patch("src.ui.views.main_view.SearchBar") as mock_search_bar,
            patch("src.ui.views.main_view.WeatherInformation") as mock_weather_info,
            patch("src.ui.views.main_view.Label") as mock_label,
            patch("src.ui.views.main_view.StringVar"),
        ):
            mock_search_bar.return_value.place = MagicMock()
            mock_weather_info.return_value.place = MagicMock()
            mock_label.return_value.place = MagicMock()
            instance: MainView = MainView.__new__(MainView)
            instance._styles = mock_styles
            MainView.__init__(
                instance,
                root=mock_root,
                styles=mock_styles,
                on_search=mock_on_search,
                img_search=mock_img,
                img_search_icon=mock_img,
                img_logo=mock_img,
                img_box=mock_img,
            )

        _, kwargs = mock_search_bar.call_args
        assert kwargs.get("on_search") == mock_on_search


class TestMainViewGetPlace:
    def test_get_place_delegates_to_search_bar(self, main_view: MainView) -> None:
        main_view._search_bar.get_place.return_value = "London"
        result: str = main_view.get_place()
        assert result == "London"

    def test_get_place_calls_search_bar_get_place(self, main_view: MainView) -> None:
        main_view._search_bar.get_place.return_value = "Paris"
        main_view.get_place()
        main_view._search_bar.get_place.assert_called_once()


class TestMainViewSetStaticLabels:
    def test_sets_current_weather_label(self, main_view: MainView) -> None:
        main_view.set_static_labels()
        main_view._label_current_weather.set.assert_called_once_with("CURRENT WEATHER")


class TestMainViewSetTime:
    def test_sets_time_label(self, main_view: MainView) -> None:
        main_view.set_time("10:30 AM")
        main_view._label_time.set.assert_called_once_with("10:30 AM")

    def test_sets_time_with_pm_suffix(self, main_view: MainView) -> None:
        main_view.set_time("14:00 PM")
        main_view._label_time.set.assert_called_once_with("14:00 PM")


class TestMainViewSetWeather:
    def _build_parsed(self) -> dict[str, Any]:
        return {
            "temp": 25,
            "feels_like": 23,
            "description": "clear sky",
            "wind": 5.5,
            "humidity": 60,
            "pressure": 1013,
        }

    def test_sets_degrees_label(self, main_view: MainView) -> None:
        main_view.set_weather(self._build_parsed())
        main_view._label_degrees.set.assert_called_once_with("25°")

    def test_sets_thermal_sensation_label(self, main_view: MainView) -> None:
        main_view.set_weather(self._build_parsed())
        main_view._label_thermal_sensation.set.assert_called_once_with("clear sky | FEELS LIKE 23°")

    def test_delegates_set_values_to_weather_information(self, main_view: MainView) -> None:
        parsed: dict[str, Any] = self._build_parsed()
        main_view.set_weather(parsed)
        main_view._weather_information.set_values.assert_called_once_with(parsed)
