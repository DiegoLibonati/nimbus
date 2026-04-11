import tkinter as tk
from typing import Any

from src.ui.styles import Styles
from src.ui.views.main_view import MainView


class TestMainView:
    def _make_view(self, root: tk.Tk, blank_photo: tk.PhotoImage) -> MainView:
        return MainView(
            root=root,
            styles=Styles(),
            on_search=lambda: None,
            img_search=blank_photo,
            img_search_icon=blank_photo,
            img_logo=blank_photo,
            img_box=blank_photo,
        )

    def _make_parsed(self) -> dict[str, Any]:
        return {
            "temp": 22,
            "description": "clear sky",
            "feels_like": 20,
            "wind": 5.0,
            "humidity": 60,
            "pressure": 1015,
        }

    def test_instantiation(self, root: tk.Tk, blank_photo: tk.PhotoImage) -> None:
        view: MainView = self._make_view(root, blank_photo)
        assert view is not None

    def test_is_frame(self, root: tk.Tk, blank_photo: tk.PhotoImage) -> None:
        view: MainView = self._make_view(root, blank_photo)
        assert isinstance(view, tk.Frame)

    def test_label_current_weather_initialized_empty(self, root: tk.Tk, blank_photo: tk.PhotoImage) -> None:
        view: MainView = self._make_view(root, blank_photo)
        assert view._label_current_weather.get() == ""

    def test_label_time_initialized_empty(self, root: tk.Tk, blank_photo: tk.PhotoImage) -> None:
        view: MainView = self._make_view(root, blank_photo)
        assert view._label_time.get() == ""

    def test_label_degrees_initialized_empty(self, root: tk.Tk, blank_photo: tk.PhotoImage) -> None:
        view: MainView = self._make_view(root, blank_photo)
        assert view._label_degrees.get() == ""

    def test_label_thermal_sensation_initialized_empty(self, root: tk.Tk, blank_photo: tk.PhotoImage) -> None:
        view: MainView = self._make_view(root, blank_photo)
        assert view._label_thermal_sensation.get() == ""

    def test_get_place_returns_empty_by_default(self, root: tk.Tk, blank_photo: tk.PhotoImage) -> None:
        view: MainView = self._make_view(root, blank_photo)
        assert view.get_place() == ""

    def test_get_place_returns_value_from_search_bar(self, root: tk.Tk, blank_photo: tk.PhotoImage) -> None:
        view: MainView = self._make_view(root, blank_photo)
        view._search_bar._entry_place.set("Paris")
        assert view.get_place() == "Paris"

    def test_set_static_labels_sets_current_weather(self, root: tk.Tk, blank_photo: tk.PhotoImage) -> None:
        view: MainView = self._make_view(root, blank_photo)
        view.set_static_labels()
        assert view._label_current_weather.get() == "CURRENT WEATHER"

    def test_set_time_updates_label(self, root: tk.Tk, blank_photo: tk.PhotoImage) -> None:
        view: MainView = self._make_view(root, blank_photo)
        view.set_time("10:30 AM")
        assert view._label_time.get() == "10:30 AM"

    def test_set_time_updates_to_pm(self, root: tk.Tk, blank_photo: tk.PhotoImage) -> None:
        view: MainView = self._make_view(root, blank_photo)
        view.set_time("14:45 PM")
        assert view._label_time.get() == "14:45 PM"

    def test_set_weather_updates_degrees(self, root: tk.Tk, blank_photo: tk.PhotoImage) -> None:
        view: MainView = self._make_view(root, blank_photo)
        view.set_weather(self._make_parsed())
        assert view._label_degrees.get() == "22°"

    def test_set_weather_updates_thermal_sensation(self, root: tk.Tk, blank_photo: tk.PhotoImage) -> None:
        view: MainView = self._make_view(root, blank_photo)
        view.set_weather(self._make_parsed())
        assert view._label_thermal_sensation.get() == "clear sky | FEELS LIKE 20°"

    def test_set_weather_delegates_to_weather_information(self, root: tk.Tk, blank_photo: tk.PhotoImage) -> None:
        view: MainView = self._make_view(root, blank_photo)
        parsed: dict[str, Any] = self._make_parsed()
        view.set_weather(parsed)
        assert view._weather_information._wind_value.get() == "5.0"
