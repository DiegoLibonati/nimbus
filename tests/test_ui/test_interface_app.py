import tkinter as tk
from unittest.mock import MagicMock, patch

import pytest
import pytz

from src.configs.default_config import DefaultConfig
from src.ui.interface_app import InterfaceApp
from src.utils.dialogs import ValidationDialogError


class TestInterfaceApp:
    def test_instantiation(self, root: tk.Tk) -> None:
        config: DefaultConfig = DefaultConfig()
        mock_view: MagicMock = MagicMock()
        with patch("src.ui.interface_app.PhotoImage"), patch("src.ui.interface_app.MainView", return_value=mock_view):
            app: InterfaceApp = InterfaceApp(root=root, config=config)
        assert app is not None

    def test_stores_config(self, root: tk.Tk) -> None:
        config: DefaultConfig = DefaultConfig()
        mock_view: MagicMock = MagicMock()
        with patch("src.ui.interface_app.PhotoImage"), patch("src.ui.interface_app.MainView", return_value=mock_view):
            app: InterfaceApp = InterfaceApp(root=root, config=config)
        assert app._config is config

    def test_get_weather_raises_validation_on_empty_place(self, root: tk.Tk) -> None:
        config: DefaultConfig = DefaultConfig()
        mock_view: MagicMock = MagicMock()
        mock_view.get_place.return_value = ""
        with patch("src.ui.interface_app.PhotoImage"), patch("src.ui.interface_app.MainView", return_value=mock_view):
            app: InterfaceApp = InterfaceApp(root=root, config=config)
        with pytest.raises(ValidationDialogError):
            app._get_weather()

    def test_get_weather_calls_place_information_with_input(self, root: tk.Tk) -> None:
        config: DefaultConfig = DefaultConfig()
        mock_view: MagicMock = MagicMock()
        mock_view.get_place.return_value = "Buenos Aires"
        with patch("src.ui.interface_app.PhotoImage"), patch("src.ui.interface_app.MainView", return_value=mock_view):
            app: InterfaceApp = InterfaceApp(root=root, config=config)
        with patch.object(app._weather_service, "get_place_information", return_value=None) as mock_service:
            app._get_weather()
            mock_service.assert_called_once_with("Buenos Aires")

    def test_get_weather_calls_set_static_labels(self, root: tk.Tk) -> None:
        config: DefaultConfig = DefaultConfig()
        mock_view: MagicMock = MagicMock()
        mock_view.get_place.return_value = "London"
        with patch("src.ui.interface_app.PhotoImage"), patch("src.ui.interface_app.MainView", return_value=mock_view):
            app: InterfaceApp = InterfaceApp(root=root, config=config)
        with patch.object(app._weather_service, "get_place_information", return_value=None):
            app._get_weather()
            mock_view.set_static_labels.assert_called_once()

    def test_get_weather_returns_early_when_no_location(self, root: tk.Tk) -> None:
        config: DefaultConfig = DefaultConfig()
        mock_view: MagicMock = MagicMock()
        mock_view.get_place.return_value = "London"
        with patch("src.ui.interface_app.PhotoImage"), patch("src.ui.interface_app.MainView", return_value=mock_view):
            app: InterfaceApp = InterfaceApp(root=root, config=config)
        with patch.object(app._weather_service, "get_place_information", return_value=None):
            with patch.object(app._weather_service, "get_weather_by_location") as mock_weather:
                app._get_weather()
                mock_weather.assert_not_called()

    def test_set_datetime_sets_am_suffix_for_morning_hours(self, root: tk.Tk) -> None:
        config: DefaultConfig = DefaultConfig()
        mock_view: MagicMock = MagicMock()
        with patch("src.ui.interface_app.PhotoImage"), patch("src.ui.interface_app.MainView", return_value=mock_view):
            app: InterfaceApp = InterfaceApp(root=root, config=config)

        tz = pytz.timezone("UTC")
        mock_now: MagicMock = MagicMock()
        mock_now.hour = 9
        mock_now.minute = 5
        with patch("src.ui.interface_app.datetime") as mock_dt:
            mock_dt.now.return_value = mock_now
            app._set_datetime(timezone=tz)
            mock_view.set_time.assert_called_once_with("09:05 AM")

    def test_set_datetime_sets_pm_suffix_for_afternoon_hours(self, root: tk.Tk) -> None:
        config: DefaultConfig = DefaultConfig()
        mock_view: MagicMock = MagicMock()
        with patch("src.ui.interface_app.PhotoImage"), patch("src.ui.interface_app.MainView", return_value=mock_view):
            app: InterfaceApp = InterfaceApp(root=root, config=config)

        tz = pytz.timezone("UTC")
        mock_now: MagicMock = MagicMock()
        mock_now.hour = 15
        mock_now.minute = 30
        with patch("src.ui.interface_app.datetime") as mock_dt:
            mock_dt.now.return_value = mock_now
            app._set_datetime(timezone=tz)
            mock_view.set_time.assert_called_once_with("15:30 PM")

    def test_set_datetime_boundary_hour_12_is_pm(self, root: tk.Tk) -> None:
        config: DefaultConfig = DefaultConfig()
        mock_view: MagicMock = MagicMock()
        with patch("src.ui.interface_app.PhotoImage"), patch("src.ui.interface_app.MainView", return_value=mock_view):
            app: InterfaceApp = InterfaceApp(root=root, config=config)

        tz = pytz.timezone("UTC")
        mock_now: MagicMock = MagicMock()
        mock_now.hour = 12
        mock_now.minute = 0
        with patch("src.ui.interface_app.datetime") as mock_dt:
            mock_dt.now.return_value = mock_now
            app._set_datetime(timezone=tz)
            mock_view.set_time.assert_called_once_with("12:00 PM")
