from unittest.mock import MagicMock, patch

import pytest
import pytz

from src.constants.messages import MESSAGE_NOT_VALID_LOCATION
from src.ui.interface_app import InterfaceApp
from src.ui.styles import Styles


@pytest.fixture
def interface_app(mock_root: MagicMock, mock_styles: MagicMock) -> InterfaceApp:
    with (
        patch("src.ui.interface_app.MainView") as mock_main_view_class,
        patch("src.ui.interface_app.WeatherService"),
        patch("src.ui.interface_app.PhotoImage"),
        patch("src.ui.interface_app.PATH_SEARCH", "search.png"),
        patch("src.ui.interface_app.PATH_SEARCH_ICON", "icon.png"),
        patch("src.ui.interface_app.PATH_LOGO", "logo.png"),
        patch("src.ui.interface_app.PATH_BOX", "box.png"),
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
        mock_config.API_URL = "https://api.example.com"

        with (
            patch("src.ui.interface_app.MainView") as mock_main_view_class,
            patch("src.ui.interface_app.WeatherService"),
            patch("src.ui.interface_app.PhotoImage"),
            patch("src.ui.interface_app.PATH_SEARCH", "search.png"),
            patch("src.ui.interface_app.PATH_SEARCH_ICON", "icon.png"),
            patch("src.ui.interface_app.PATH_LOGO", "logo.png"),
            patch("src.ui.interface_app.PATH_BOX", "box.png"),
        ):
            mock_main_view_class.return_value.place = MagicMock()
            InterfaceApp(root=mock_root, config=mock_config, styles=mock_styles)

        mock_root.title.assert_called_once_with("Weather APP")

    def test_geometry_is_set(self, mock_root: MagicMock, mock_styles: MagicMock) -> None:
        mock_config: MagicMock = MagicMock()
        mock_config.API_KEY = "key"
        mock_config.API_URL = "https://api.example.com"

        with (
            patch("src.ui.interface_app.MainView") as mock_main_view_class,
            patch("src.ui.interface_app.WeatherService"),
            patch("src.ui.interface_app.PhotoImage"),
            patch("src.ui.interface_app.PATH_SEARCH", "search.png"),
            patch("src.ui.interface_app.PATH_SEARCH_ICON", "icon.png"),
            patch("src.ui.interface_app.PATH_LOGO", "logo.png"),
            patch("src.ui.interface_app.PATH_BOX", "box.png"),
        ):
            mock_main_view_class.return_value.place = MagicMock()
            InterfaceApp(root=mock_root, config=mock_config, styles=mock_styles)

        mock_root.geometry.assert_called_once_with("900x500+300+200")

    def test_is_not_resizable(self, mock_root: MagicMock, mock_styles: MagicMock) -> None:
        mock_config: MagicMock = MagicMock()
        mock_config.API_KEY = "key"
        mock_config.API_URL = "https://api.example.com"

        with (
            patch("src.ui.interface_app.MainView") as mock_main_view_class,
            patch("src.ui.interface_app.WeatherService"),
            patch("src.ui.interface_app.PhotoImage"),
            patch("src.ui.interface_app.PATH_SEARCH", "search.png"),
            patch("src.ui.interface_app.PATH_SEARCH_ICON", "icon.png"),
            patch("src.ui.interface_app.PATH_LOGO", "logo.png"),
            patch("src.ui.interface_app.PATH_BOX", "box.png"),
        ):
            mock_main_view_class.return_value.place = MagicMock()
            InterfaceApp(root=mock_root, config=mock_config, styles=mock_styles)

        mock_root.resizable.assert_called_once_with(False, False)

    def test_default_styles_is_styles_instance(self, mock_root: MagicMock) -> None:
        mock_config: MagicMock = MagicMock()
        mock_config.API_KEY = "key"
        mock_config.API_URL = "https://api.example.com"

        with (
            patch("src.ui.interface_app.MainView") as mock_main_view_class,
            patch("src.ui.interface_app.WeatherService"),
            patch("src.ui.interface_app.PhotoImage"),
            patch("src.ui.interface_app.PATH_SEARCH", "search.png"),
            patch("src.ui.interface_app.PATH_SEARCH_ICON", "icon.png"),
            patch("src.ui.interface_app.PATH_LOGO", "logo.png"),
            patch("src.ui.interface_app.PATH_BOX", "box.png"),
        ):
            mock_main_view_class.return_value.place = MagicMock()
            app: InterfaceApp = InterfaceApp(root=mock_root, config=mock_config)

        assert isinstance(app._styles, Styles)


class TestInterfaceAppGetWeather:
    def test_validation_dialog_called_when_place_is_empty(self, interface_app: InterfaceApp) -> None:
        interface_app._main_view.get_place.return_value = ""

        with patch("src.ui.interface_app.ValidationDialogError") as mock_dialog_class:
            mock_dialog_class.return_value = MagicMock()
            interface_app._get_weather()

        mock_dialog_class.assert_called_once_with(message=MESSAGE_NOT_VALID_LOCATION)
        mock_dialog_class.return_value.dialog.assert_called_once()

    def test_weather_service_not_called_when_place_is_empty(self, interface_app: InterfaceApp) -> None:
        interface_app._main_view.get_place.return_value = ""

        with patch("src.ui.interface_app.ValidationDialogError") as mock_dialog_class:
            mock_dialog_class.return_value = MagicMock()
            interface_app._get_weather()

        interface_app._weather_service.get_place_information.assert_not_called()

    def test_set_static_labels_called_when_place_is_valid(self, interface_app: InterfaceApp) -> None:
        interface_app._main_view.get_place.return_value = "Buenos Aires"
        interface_app._weather_service.get_place_information.return_value = {
            "timezone": "America/Argentina/Buenos_Aires",
            "longitude": -58.38,
            "latitude": -34.60,
        }
        interface_app._weather_service.get_weather_by_location.return_value = {}

        with (
            patch("src.ui.interface_app.pytz.timezone"),
            patch.object(interface_app, "_set_datetime"),
            patch("src.ui.interface_app.parse_weather_data", return_value={}),
        ):
            interface_app._get_weather()

        interface_app._main_view.set_static_labels.assert_called_once()

    def test_get_place_information_called_with_entry_value(self, interface_app: InterfaceApp) -> None:
        interface_app._main_view.get_place.return_value = "Buenos Aires"
        interface_app._weather_service.get_place_information.return_value = {
            "timezone": "America/Argentina/Buenos_Aires",
            "longitude": -58.38,
            "latitude": -34.60,
        }
        interface_app._weather_service.get_weather_by_location.return_value = {}

        with (
            patch("src.ui.interface_app.pytz.timezone"),
            patch.object(interface_app, "_set_datetime"),
            patch("src.ui.interface_app.parse_weather_data", return_value={}),
        ):
            interface_app._get_weather()

        interface_app._weather_service.get_place_information.assert_called_once_with("Buenos Aires")

    def test_get_weather_by_location_called_with_rounded_coords(self, interface_app: InterfaceApp) -> None:
        interface_app._main_view.get_place.return_value = "Buenos Aires"
        interface_app._weather_service.get_place_information.return_value = {
            "timezone": "America/Argentina/Buenos_Aires",
            "longitude": -58.38,
            "latitude": -34.60,
        }
        interface_app._weather_service.get_weather_by_location.return_value = {}

        with (
            patch("src.ui.interface_app.pytz.timezone"),
            patch.object(interface_app, "_set_datetime"),
            patch("src.ui.interface_app.parse_weather_data", return_value={}),
        ):
            interface_app._get_weather()

        interface_app._weather_service.get_weather_by_location.assert_called_once_with(
            longitude=round(-58.38),
            latitude=round(-34.60),
        )

    def test_set_weather_called_with_parsed_data(self, interface_app: InterfaceApp) -> None:
        interface_app._main_view.get_place.return_value = "Buenos Aires"
        interface_app._weather_service.get_place_information.return_value = {
            "timezone": "America/Argentina/Buenos_Aires",
            "longitude": -58.38,
            "latitude": -34.60,
        }
        interface_app._weather_service.get_weather_by_location.return_value = {"raw": "data"}
        parsed: dict[str, str] = {"temp": "25°C", "humidity": "60%"}

        with (
            patch("src.ui.interface_app.pytz.timezone"),
            patch.object(interface_app, "_set_datetime"),
            patch("src.ui.interface_app.parse_weather_data", return_value=parsed),
        ):
            interface_app._get_weather()

        interface_app._main_view.set_weather.assert_called_once_with(parsed)

    def test_set_datetime_called_with_timezone(self, interface_app: InterfaceApp) -> None:
        interface_app._main_view.get_place.return_value = "Buenos Aires"
        interface_app._weather_service.get_place_information.return_value = {
            "timezone": "America/Argentina/Buenos_Aires",
            "longitude": -58.38,
            "latitude": -34.60,
        }
        interface_app._weather_service.get_weather_by_location.return_value = {}
        mock_tz: MagicMock = MagicMock()

        with (
            patch("src.ui.interface_app.pytz.timezone", return_value=mock_tz),
            patch.object(interface_app, "_set_datetime") as mock_set_datetime,
            patch("src.ui.interface_app.parse_weather_data", return_value={}),
        ):
            interface_app._get_weather()

        mock_set_datetime.assert_called_once_with(timezone=mock_tz)


class TestInterfaceAppSetDatetime:
    def test_set_time_called_with_am_suffix_in_morning(self, interface_app: InterfaceApp) -> None:
        tz: pytz.BaseTzInfo = pytz.timezone("America/Argentina/Buenos_Aires")

        with patch("src.ui.interface_app.datetime") as mock_dt:
            mock_now: MagicMock = MagicMock()
            mock_now.hour = 9
            mock_now.minute = 5
            mock_dt.now.return_value = mock_now
            interface_app._set_datetime(timezone=tz)

        call_arg: str = interface_app._main_view.set_time.call_args[0][0]
        assert "AM" in call_arg

    def test_set_time_called_with_pm_suffix_in_afternoon(self, interface_app: InterfaceApp) -> None:
        tz: pytz.BaseTzInfo = pytz.timezone("America/Argentina/Buenos_Aires")

        with patch("src.ui.interface_app.datetime") as mock_dt:
            mock_now: MagicMock = MagicMock()
            mock_now.hour = 15
            mock_now.minute = 30
            mock_dt.now.return_value = mock_now
            interface_app._set_datetime(timezone=tz)

        call_arg: str = interface_app._main_view.set_time.call_args[0][0]
        assert "PM" in call_arg

    def test_set_time_format_includes_colon(self, interface_app: InterfaceApp) -> None:
        tz: pytz.BaseTzInfo = pytz.timezone("America/Argentina/Buenos_Aires")

        with patch("src.ui.interface_app.datetime") as mock_dt:
            mock_now: MagicMock = MagicMock()
            mock_now.hour = 10
            mock_now.minute = 20
            mock_dt.now.return_value = mock_now
            interface_app._set_datetime(timezone=tz)

        call_arg: str = interface_app._main_view.set_time.call_args[0][0]
        assert ":" in call_arg
