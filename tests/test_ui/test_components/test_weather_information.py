import tkinter as tk
from typing import Any

from src.ui.components.weather_information import WeatherInformation
from src.ui.styles import Styles


class TestWeatherInformation:
    def _make_parsed(self) -> dict[str, Any]:
        return {
            "wind": 10.5,
            "humidity": 80,
            "description": "light rain",
            "pressure": 1012,
        }

    def test_instantiation(self, root: tk.Tk, blank_photo: tk.PhotoImage) -> None:
        widget: WeatherInformation = WeatherInformation(parent=root, styles=Styles(), img_box=blank_photo)
        assert widget is not None

    def test_is_frame(self, root: tk.Tk, blank_photo: tk.PhotoImage) -> None:
        widget: WeatherInformation = WeatherInformation(parent=root, styles=Styles(), img_box=blank_photo)
        assert isinstance(widget, tk.Frame)

    def test_wind_text_initialized_empty(self, root: tk.Tk, blank_photo: tk.PhotoImage) -> None:
        widget: WeatherInformation = WeatherInformation(parent=root, styles=Styles(), img_box=blank_photo)
        assert widget._wind_text.get() == ""

    def test_wind_value_initialized_empty(self, root: tk.Tk, blank_photo: tk.PhotoImage) -> None:
        widget: WeatherInformation = WeatherInformation(parent=root, styles=Styles(), img_box=blank_photo)
        assert widget._wind_value.get() == ""

    def test_humidity_text_initialized_empty(self, root: tk.Tk, blank_photo: tk.PhotoImage) -> None:
        widget: WeatherInformation = WeatherInformation(parent=root, styles=Styles(), img_box=blank_photo)
        assert widget._humidity_text.get() == ""

    def test_description_text_initialized_empty(self, root: tk.Tk, blank_photo: tk.PhotoImage) -> None:
        widget: WeatherInformation = WeatherInformation(parent=root, styles=Styles(), img_box=blank_photo)
        assert widget._description_text.get() == ""

    def test_pressure_text_initialized_empty(self, root: tk.Tk, blank_photo: tk.PhotoImage) -> None:
        widget: WeatherInformation = WeatherInformation(parent=root, styles=Styles(), img_box=blank_photo)
        assert widget._pressure_text.get() == ""

    def test_set_values_sets_wind_label(self, root: tk.Tk, blank_photo: tk.PhotoImage) -> None:
        widget: WeatherInformation = WeatherInformation(parent=root, styles=Styles(), img_box=blank_photo)
        widget.set_values(self._make_parsed())
        assert widget._wind_text.get() == "WIND"

    def test_set_values_sets_humidity_label(self, root: tk.Tk, blank_photo: tk.PhotoImage) -> None:
        widget: WeatherInformation = WeatherInformation(parent=root, styles=Styles(), img_box=blank_photo)
        widget.set_values(self._make_parsed())
        assert widget._humidity_text.get() == "HUMIDITY"

    def test_set_values_sets_description_label(self, root: tk.Tk, blank_photo: tk.PhotoImage) -> None:
        widget: WeatherInformation = WeatherInformation(parent=root, styles=Styles(), img_box=blank_photo)
        widget.set_values(self._make_parsed())
        assert widget._description_text.get() == "DESCRIPTION"

    def test_set_values_sets_pressure_label(self, root: tk.Tk, blank_photo: tk.PhotoImage) -> None:
        widget: WeatherInformation = WeatherInformation(parent=root, styles=Styles(), img_box=blank_photo)
        widget.set_values(self._make_parsed())
        assert widget._pressure_text.get() == "PRESSURE"

    def test_set_values_updates_wind_value(self, root: tk.Tk, blank_photo: tk.PhotoImage) -> None:
        widget: WeatherInformation = WeatherInformation(parent=root, styles=Styles(), img_box=blank_photo)
        widget.set_values(self._make_parsed())
        assert widget._wind_value.get() == "10.5"

    def test_set_values_updates_humidity_value(self, root: tk.Tk, blank_photo: tk.PhotoImage) -> None:
        widget: WeatherInformation = WeatherInformation(parent=root, styles=Styles(), img_box=blank_photo)
        widget.set_values(self._make_parsed())
        assert widget._humidity_value.get() == "80"

    def test_set_values_updates_description_value(self, root: tk.Tk, blank_photo: tk.PhotoImage) -> None:
        widget: WeatherInformation = WeatherInformation(parent=root, styles=Styles(), img_box=blank_photo)
        widget.set_values(self._make_parsed())
        assert widget._description_value.get() == "light rain"

    def test_set_values_updates_pressure_value(self, root: tk.Tk, blank_photo: tk.PhotoImage) -> None:
        widget: WeatherInformation = WeatherInformation(parent=root, styles=Styles(), img_box=blank_photo)
        widget.set_values(self._make_parsed())
        assert widget._pressure_value.get() == "1012"
