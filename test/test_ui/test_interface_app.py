from unittest.mock import MagicMock, patch

import pytest

from src.ui.interface_app import InterfaceApp
from src.ui.styles import Styles


@pytest.fixture
def interface_app(mock_root: MagicMock, mock_styles: MagicMock) -> InterfaceApp:
    with (
        patch("src.ui.interface_app.MainView") as mock_main_view_class,
        patch("src.ui.interface_app.WeatherService"),
        patch("src.ui.interface_app.PhotoImage"),
    ):
        mock_main_view: MagicMock = MagicMock()
        mock_main_view.place = MagicMock()
        mock_main_view_class.return_value = mock_main_view
        instance: InterfaceApp = InterfaceApp.__new__(InterfaceApp)
        instance._styles = mock_styles
        instance._root = mock_root
        instance._config = MagicMock()
        instance._main_view = mock_main_view
        instance._weather_service = MagicMock()
        return instance


class TestInterfaceAppInit:
    def test_stores_styles(self, interface_app: InterfaceApp, mock_styles: MagicMock) -> None:
        assert interface_app._styles == mock_styles

    def test_stores_root(self, interface_app: InterfaceApp, mock_root: MagicMock) -> None:
        assert interface_app._root == mock_root

    def test_title_is_set(self, mock_root: MagicMock, mock_styles: MagicMock) -> None:
        mock_config: MagicMock = MagicMock()
        mock_config.API_KEY = "key"
        mock_config.API_URL = "url"

        with (
            patch("src.ui.interface_app.MainView") as mock_main_view_class,
            patch("src.ui.interface_app.WeatherService"),
            patch("src.ui.interface_app.PhotoImage"),
        ):
            mock_main_view_class.return_value.place = MagicMock()
            InterfaceApp(root=mock_root, config=mock_config, styles=mock_styles)

        mock_root.title.assert_called_once_with("Weather APP")

    def test_geometry_is_set(self, mock_root: MagicMock, mock_styles: MagicMock) -> None:
        mock_config: MagicMock = MagicMock()
        mock_config.API_KEY = "key"
        mock_config.API_URL = "url"

        with (
            patch("src.ui.interface_app.MainView") as mock_main_view_class,
            patch("src.ui.interface_app.WeatherService"),
            patch("src.ui.interface_app.PhotoImage"),
        ):
            mock_main_view_class.return_value.place = MagicMock()
            InterfaceApp(root=mock_root, config=mock_config, styles=mock_styles)

        mock_root.geometry.assert_called_once_with("900x500+300+200")

    def test_is_not_resizable(self, mock_root: MagicMock, mock_styles: MagicMock) -> None:
        mock_config: MagicMock = MagicMock()
        mock_config.API_KEY = "key"
        mock_config.API_URL = "url"

        with (
            patch("src.ui.interface_app.MainView") as mock_main_view_class,
            patch("src.ui.interface_app.WeatherService"),
            patch("src.ui.interface_app.PhotoImage"),
        ):
            mock_main_view_class.return_value.place = MagicMock()
            InterfaceApp(root=mock_root, config=mock_config, styles=mock_styles)

        mock_root.resizable.assert_called_once_with(False, False)

    def test_default_styles_is_styles_instance(self, mock_root: MagicMock) -> None:
        mock_config: MagicMock = MagicMock()
        mock_config.API_KEY = "key"
        mock_config.API_URL = "url"

        with (
            patch("src.ui.interface_app.MainView") as mock_main_view_class,
            patch("src.ui.interface_app.WeatherService"),
            patch("src.ui.interface_app.PhotoImage"),
        ):
            mock_main_view_class.return_value.place = MagicMock()
            app: InterfaceApp = InterfaceApp(root=mock_root, config=mock_config)

        assert isinstance(app._styles, Styles)

    def test_weather_service_is_created_with_api_key_and_url(self, mock_root: MagicMock, mock_styles: MagicMock) -> None:
        mock_config: MagicMock = MagicMock()
        mock_config.API_KEY = "my_key"
        mock_config.API_URL = "http://my.api"

        with (
            patch("src.ui.interface_app.MainView") as mock_main_view_class,
            patch("src.ui.interface_app.WeatherService") as mock_weather_service_class,
            patch("src.ui.interface_app.PhotoImage"),
        ):
            mock_main_view_class.return_value.place = MagicMock()
            InterfaceApp(root=mock_root, config=mock_config, styles=mock_styles)

        mock_weather_service_class.assert_called_once_with(api_key="my_key", api_url="http://my.api")


class TestInterfaceAppGetWeather:
    def test_raises_value_error_when_place_is_empty(self, interface_app: InterfaceApp) -> None:
        interface_app._main_view.get_place.return_value = ""

        with pytest.raises(ValueError, match="valid location"):
            interface_app._get_weather()

    def test_set_static_labels_is_called(self, interface_app: InterfaceApp) -> None:
        interface_app._main_view.get_place.return_value = "London"
        interface_app._weather_service.get_place_information.return_value = {
            "timezone": "Europe/London",
            "longitude": -0.1276,
            "latitude": 51.5074,
        }
        interface_app._weather_service.get_weather_by_location.return_value = {}

        with (
            patch.object(interface_app, "_set_datetime"),
            patch("src.ui.interface_app.parse_weather_data", return_value={}),
        ):
            interface_app._get_weather()

        interface_app._main_view.set_static_labels.assert_called_once()

    def test_get_place_information_called_with_entry_value(self, interface_app: InterfaceApp) -> None:
        interface_app._main_view.get_place.return_value = "London"
        interface_app._weather_service.get_place_information.return_value = {
            "timezone": "Europe/London",
            "longitude": -0.1276,
            "latitude": 51.5074,
        }
        interface_app._weather_service.get_weather_by_location.return_value = {}

        with (
            patch.object(interface_app, "_set_datetime"),
            patch("src.ui.interface_app.parse_weather_data", return_value={}),
        ):
            interface_app._get_weather()

        interface_app._weather_service.get_place_information.assert_called_once_with("London")

    def test_set_weather_is_called_with_parsed_data(self, interface_app: InterfaceApp) -> None:
        interface_app._main_view.get_place.return_value = "London"
        interface_app._weather_service.get_place_information.return_value = {
            "timezone": "Europe/London",
            "longitude": -0.1276,
            "latitude": 51.5074,
        }
        interface_app._weather_service.get_weather_by_location.return_value = {"raw": "data"}
        parsed_data: dict = {"temp": 20, "feels_like": 18, "wind": 3.0, "description": "sunny", "humidity": 50, "pressure": 1010}

        with (
            patch.object(interface_app, "_set_datetime"),
            patch("src.ui.interface_app.parse_weather_data", return_value=parsed_data),
        ):
            interface_app._get_weather()

        interface_app._main_view.set_weather.assert_called_once_with(parsed_data)


class TestInterfaceAppSetDatetime:
    def test_set_time_called_with_formatted_am_time(self, interface_app: InterfaceApp) -> None:
        mock_timezone: MagicMock = MagicMock()
        mock_now: MagicMock = MagicMock()
        mock_now.hour = 9
        mock_now.minute = 5

        with (
            patch("src.ui.interface_app.datetime") as mock_datetime,
            patch("src.ui.interface_app.add_zero", side_effect=lambda v: f"0{v}" if v < 10 else str(v)),
        ):
            mock_datetime.now.return_value = mock_now
            interface_app._set_datetime(timezone=mock_timezone)

        interface_app._main_view.set_time.assert_called_once_with("09:05 AM")

    def test_set_time_called_with_formatted_pm_time(self, interface_app: InterfaceApp) -> None:
        mock_timezone: MagicMock = MagicMock()
        mock_now: MagicMock = MagicMock()
        mock_now.hour = 15
        mock_now.minute = 30

        with (
            patch("src.ui.interface_app.datetime") as mock_datetime,
            patch("src.ui.interface_app.add_zero", side_effect=lambda v: f"0{v}" if v < 10 else str(v)),
        ):
            mock_datetime.now.return_value = mock_now
            interface_app._set_datetime(timezone=mock_timezone)

        interface_app._main_view.set_time.assert_called_once_with("15:30 PM")
