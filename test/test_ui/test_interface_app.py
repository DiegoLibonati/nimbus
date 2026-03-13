from typing import Any
from unittest.mock import MagicMock, patch

import pytest

from src.constants.messages import MESSAGE_NOT_VALID_LOCATION
from src.ui.interface_app import InterfaceApp
from src.ui.styles import Styles
from src.utils.dialogs import ValidationDialogError


@pytest.fixture
def interface_app(mock_root: MagicMock, mock_styles: MagicMock, mock_img: MagicMock) -> InterfaceApp:
    with (
        patch("src.ui.interface_app.MainView") as mock_main_view_class,
        patch("src.ui.interface_app.WeatherService"),
        patch("src.ui.interface_app.PhotoImage", return_value=mock_img),
        patch("src.ui.interface_app.PATH_SEARCH", "search.png"),
        patch("src.ui.interface_app.PATH_SEARCH_ICON", "search_icon.png"),
        patch("src.ui.interface_app.PATH_LOGO", "logo.png"),
        patch("src.ui.interface_app.PATH_BOX", "box.png"),
    ):
        mock_main_view_class.return_value = MagicMock()
        instance: InterfaceApp = InterfaceApp.__new__(InterfaceApp)
        instance._styles = mock_styles
        instance._config = MagicMock()
        instance._root = mock_root
        instance._main_view = mock_main_view_class.return_value
        instance._weather_service = MagicMock()
        return instance


class TestInterfaceAppInit:
    def test_stores_styles(self, mock_root: MagicMock, mock_styles: MagicMock, mock_img: MagicMock) -> None:
        with (
            patch("src.ui.interface_app.MainView") as mock_main_view_class,
            patch("src.ui.interface_app.WeatherService"),
            patch("src.ui.interface_app.PhotoImage", return_value=mock_img),
            patch("src.ui.interface_app.PATH_SEARCH", "search.png"),
            patch("src.ui.interface_app.PATH_SEARCH_ICON", "search_icon.png"),
            patch("src.ui.interface_app.PATH_LOGO", "logo.png"),
            patch("src.ui.interface_app.PATH_BOX", "box.png"),
        ):
            mock_main_view_class.return_value.place = MagicMock()
            app: InterfaceApp = InterfaceApp(root=mock_root, config=MagicMock(), styles=mock_styles)
        assert app._styles is mock_styles

    def test_stores_root(self, mock_root: MagicMock, mock_styles: MagicMock, mock_img: MagicMock) -> None:
        with (
            patch("src.ui.interface_app.MainView") as mock_main_view_class,
            patch("src.ui.interface_app.WeatherService"),
            patch("src.ui.interface_app.PhotoImage", return_value=mock_img),
            patch("src.ui.interface_app.PATH_SEARCH", "search.png"),
            patch("src.ui.interface_app.PATH_SEARCH_ICON", "search_icon.png"),
            patch("src.ui.interface_app.PATH_LOGO", "logo.png"),
            patch("src.ui.interface_app.PATH_BOX", "box.png"),
        ):
            mock_main_view_class.return_value.place = MagicMock()
            app: InterfaceApp = InterfaceApp(root=mock_root, config=MagicMock(), styles=mock_styles)
        assert app._root is mock_root

    def test_title_is_set(self, mock_root: MagicMock, mock_styles: MagicMock, mock_img: MagicMock) -> None:
        with (
            patch("src.ui.interface_app.MainView") as mock_main_view_class,
            patch("src.ui.interface_app.WeatherService"),
            patch("src.ui.interface_app.PhotoImage", return_value=mock_img),
            patch("src.ui.interface_app.PATH_SEARCH", "search.png"),
            patch("src.ui.interface_app.PATH_SEARCH_ICON", "search_icon.png"),
            patch("src.ui.interface_app.PATH_LOGO", "logo.png"),
            patch("src.ui.interface_app.PATH_BOX", "box.png"),
        ):
            mock_main_view_class.return_value.place = MagicMock()
            InterfaceApp(root=mock_root, config=MagicMock(), styles=mock_styles)
        mock_root.title.assert_called_once_with("Weather APP")

    def test_geometry_is_set(self, mock_root: MagicMock, mock_styles: MagicMock, mock_img: MagicMock) -> None:
        with (
            patch("src.ui.interface_app.MainView") as mock_main_view_class,
            patch("src.ui.interface_app.WeatherService"),
            patch("src.ui.interface_app.PhotoImage", return_value=mock_img),
            patch("src.ui.interface_app.PATH_SEARCH", "search.png"),
            patch("src.ui.interface_app.PATH_SEARCH_ICON", "search_icon.png"),
            patch("src.ui.interface_app.PATH_LOGO", "logo.png"),
            patch("src.ui.interface_app.PATH_BOX", "box.png"),
        ):
            mock_main_view_class.return_value.place = MagicMock()
            InterfaceApp(root=mock_root, config=MagicMock(), styles=mock_styles)
        mock_root.geometry.assert_called_once_with("900x500+300+200")

    def test_is_not_resizable(self, mock_root: MagicMock, mock_styles: MagicMock, mock_img: MagicMock) -> None:
        with (
            patch("src.ui.interface_app.MainView") as mock_main_view_class,
            patch("src.ui.interface_app.WeatherService"),
            patch("src.ui.interface_app.PhotoImage", return_value=mock_img),
            patch("src.ui.interface_app.PATH_SEARCH", "search.png"),
            patch("src.ui.interface_app.PATH_SEARCH_ICON", "search_icon.png"),
            patch("src.ui.interface_app.PATH_LOGO", "logo.png"),
            patch("src.ui.interface_app.PATH_BOX", "box.png"),
        ):
            mock_main_view_class.return_value.place = MagicMock()
            InterfaceApp(root=mock_root, config=MagicMock(), styles=mock_styles)
        mock_root.resizable.assert_called_once_with(False, False)

    def test_background_uses_primary_color(self, mock_root: MagicMock, mock_styles: MagicMock, mock_img: MagicMock) -> None:
        with (
            patch("src.ui.interface_app.MainView") as mock_main_view_class,
            patch("src.ui.interface_app.WeatherService"),
            patch("src.ui.interface_app.PhotoImage", return_value=mock_img),
            patch("src.ui.interface_app.PATH_SEARCH", "search.png"),
            patch("src.ui.interface_app.PATH_SEARCH_ICON", "search_icon.png"),
            patch("src.ui.interface_app.PATH_LOGO", "logo.png"),
            patch("src.ui.interface_app.PATH_BOX", "box.png"),
        ):
            mock_main_view_class.return_value.place = MagicMock()
            InterfaceApp(root=mock_root, config=MagicMock(), styles=mock_styles)
        mock_root.config.assert_called_once_with(background=mock_styles.PRIMARY_COLOR)

    def test_default_styles_is_styles_instance(self, mock_root: MagicMock, mock_img: MagicMock) -> None:
        with (
            patch("src.ui.interface_app.MainView") as mock_main_view_class,
            patch("src.ui.interface_app.WeatherService"),
            patch("src.ui.interface_app.PhotoImage", return_value=mock_img),
            patch("src.ui.interface_app.PATH_SEARCH", "search.png"),
            patch("src.ui.interface_app.PATH_SEARCH_ICON", "search_icon.png"),
            patch("src.ui.interface_app.PATH_LOGO", "logo.png"),
            patch("src.ui.interface_app.PATH_BOX", "box.png"),
        ):
            mock_main_view_class.return_value.place = MagicMock()
            app: InterfaceApp = InterfaceApp(root=mock_root, config=MagicMock())
        assert isinstance(app._styles, Styles)

    def test_main_view_receives_on_search(self, mock_root: MagicMock, mock_styles: MagicMock, mock_img: MagicMock) -> None:
        with (
            patch("src.ui.interface_app.MainView") as mock_main_view_class,
            patch("src.ui.interface_app.WeatherService"),
            patch("src.ui.interface_app.PhotoImage", return_value=mock_img),
            patch("src.ui.interface_app.PATH_SEARCH", "search.png"),
            patch("src.ui.interface_app.PATH_SEARCH_ICON", "search_icon.png"),
            patch("src.ui.interface_app.PATH_LOGO", "logo.png"),
            patch("src.ui.interface_app.PATH_BOX", "box.png"),
        ):
            mock_main_view_class.return_value.place = MagicMock()
            InterfaceApp(root=mock_root, config=MagicMock(), styles=mock_styles)
        _, kwargs = mock_main_view_class.call_args
        assert callable(kwargs.get("on_search"))

    def test_main_view_place_called(self, mock_root: MagicMock, mock_styles: MagicMock, mock_img: MagicMock) -> None:
        with (
            patch("src.ui.interface_app.MainView") as mock_main_view_class,
            patch("src.ui.interface_app.WeatherService"),
            patch("src.ui.interface_app.PhotoImage", return_value=mock_img),
            patch("src.ui.interface_app.PATH_SEARCH", "search.png"),
            patch("src.ui.interface_app.PATH_SEARCH_ICON", "search_icon.png"),
            patch("src.ui.interface_app.PATH_LOGO", "logo.png"),
            patch("src.ui.interface_app.PATH_BOX", "box.png"),
        ):
            mock_main_view: MagicMock = MagicMock()
            mock_main_view_class.return_value = mock_main_view
            InterfaceApp(root=mock_root, config=MagicMock(), styles=mock_styles)
        mock_main_view.place.assert_called_once_with(x=0, y=0, width=900, height=500)


class TestInterfaceAppGetWeather:
    def test_raises_validation_error_when_place_is_empty(self, interface_app: InterfaceApp) -> None:
        interface_app._main_view.get_place.return_value = ""
        with pytest.raises(ValidationDialogError) as exc_info:
            interface_app._get_weather()
        assert exc_info.value.message == MESSAGE_NOT_VALID_LOCATION

    def test_set_static_labels_not_called_when_place_is_empty(self, interface_app: InterfaceApp) -> None:
        interface_app._main_view.get_place.return_value = ""
        with pytest.raises(ValidationDialogError):
            interface_app._get_weather()
        interface_app._main_view.set_static_labels.assert_not_called()

    def test_set_static_labels_called_when_place_is_valid(self, interface_app: InterfaceApp) -> None:
        interface_app._main_view.get_place.return_value = "London"
        interface_app._weather_service.get_place_information.return_value = None

        interface_app._get_weather()

        interface_app._main_view.set_static_labels.assert_called_once()

    def test_get_place_information_called_with_entry_value(self, interface_app: InterfaceApp) -> None:
        interface_app._main_view.get_place.return_value = "Paris"
        interface_app._weather_service.get_place_information.return_value = None

        interface_app._get_weather()

        interface_app._weather_service.get_place_information.assert_called_once_with("Paris")

    def test_returns_early_when_location_is_none(self, interface_app: InterfaceApp) -> None:
        interface_app._main_view.get_place.return_value = "Paris"
        interface_app._weather_service.get_place_information.return_value = None

        interface_app._get_weather()

        interface_app._weather_service.get_weather_by_location.assert_not_called()

    def test_get_weather_by_location_called_with_rounded_coords(self, interface_app: InterfaceApp) -> None:
        interface_app._main_view.get_place.return_value = "London"
        interface_app._weather_service.get_place_information.return_value = {
            "timezone": "Europe/London",
            "longitude": -0.1276,
            "latitude": 51.5074,
        }
        interface_app._weather_service.get_weather_by_location.return_value = None

        with patch.object(interface_app, "_set_datetime"):
            interface_app._get_weather()

        interface_app._weather_service.get_weather_by_location.assert_called_once_with(
            longitude=round(-0.1276),
            latitude=round(51.5074),
        )

    def test_set_weather_not_called_when_weather_data_is_none(self, interface_app: InterfaceApp) -> None:
        interface_app._main_view.get_place.return_value = "London"
        interface_app._weather_service.get_place_information.return_value = {
            "timezone": "Europe/London",
            "longitude": -0.1276,
            "latitude": 51.5074,
        }
        interface_app._weather_service.get_weather_by_location.return_value = None

        with patch.object(interface_app, "_set_datetime"):
            interface_app._get_weather()

        interface_app._main_view.set_weather.assert_not_called()

    def test_set_weather_called_with_parsed_data(self, interface_app: InterfaceApp) -> None:
        interface_app._main_view.get_place.return_value = "London"
        interface_app._weather_service.get_place_information.return_value = {
            "timezone": "Europe/London",
            "longitude": -0.1276,
            "latitude": 51.5074,
        }
        raw_weather: dict[str, Any] = {"main": {"temp": 280}}
        parsed_weather: dict[str, str] = {"temperature": "6.85°C"}
        interface_app._weather_service.get_weather_by_location.return_value = raw_weather

        with (
            patch.object(interface_app, "_set_datetime"),
            patch("src.ui.interface_app.parse_weather_data", return_value=parsed_weather) as mock_parse,
        ):
            interface_app._get_weather()

        mock_parse.assert_called_once_with(raw_weather)
        interface_app._main_view.set_weather.assert_called_once_with(parsed_weather)


class TestInterfaceAppSetDatetime:
    def test_set_time_called_with_am_suffix_for_morning(self, interface_app: InterfaceApp) -> None:
        mock_timezone: MagicMock = MagicMock()
        mock_now: MagicMock = MagicMock()
        mock_now.hour = 9
        mock_now.minute = 5

        with patch("src.ui.interface_app.datetime") as mock_datetime:
            mock_datetime.now.return_value = mock_now
            with patch("src.ui.interface_app.add_zero", side_effect=lambda x: str(x).zfill(2)):
                interface_app._set_datetime(timezone=mock_timezone)

        interface_app._main_view.set_time.assert_called_once_with("09:05 AM")

    def test_set_time_called_with_pm_suffix_for_afternoon(self, interface_app: InterfaceApp) -> None:
        mock_timezone: MagicMock = MagicMock()
        mock_now: MagicMock = MagicMock()
        mock_now.hour = 15
        mock_now.minute = 30

        with patch("src.ui.interface_app.datetime") as mock_datetime:
            mock_datetime.now.return_value = mock_now
            with patch("src.ui.interface_app.add_zero", side_effect=lambda x: str(x).zfill(2)):
                interface_app._set_datetime(timezone=mock_timezone)

        interface_app._main_view.set_time.assert_called_once_with("15:30 PM")

    def test_set_time_called_with_pm_suffix_at_noon(self, interface_app: InterfaceApp) -> None:
        mock_timezone: MagicMock = MagicMock()
        mock_now: MagicMock = MagicMock()
        mock_now.hour = 12
        mock_now.minute = 0

        with patch("src.ui.interface_app.datetime") as mock_datetime:
            mock_datetime.now.return_value = mock_now
            with patch("src.ui.interface_app.add_zero", side_effect=lambda x: str(x).zfill(2)):
                interface_app._set_datetime(timezone=mock_timezone)

        interface_app._main_view.set_time.assert_called_once_with("12:00 PM")

    def test_set_time_called_with_am_suffix_at_midnight(self, interface_app: InterfaceApp) -> None:
        mock_timezone: MagicMock = MagicMock()
        mock_now: MagicMock = MagicMock()
        mock_now.hour = 0
        mock_now.minute = 0

        with patch("src.ui.interface_app.datetime") as mock_datetime:
            mock_datetime.now.return_value = mock_now
            with patch("src.ui.interface_app.add_zero", side_effect=lambda x: str(x).zfill(2)):
                interface_app._set_datetime(timezone=mock_timezone)

        interface_app._main_view.set_time.assert_called_once_with("00:00 AM")

    def test_datetime_now_called_with_timezone(self, interface_app: InterfaceApp) -> None:
        mock_timezone: MagicMock = MagicMock()
        mock_now: MagicMock = MagicMock()
        mock_now.hour = 10
        mock_now.minute = 0

        with patch("src.ui.interface_app.datetime") as mock_datetime:
            mock_datetime.now.return_value = mock_now
            with patch("src.ui.interface_app.add_zero", side_effect=lambda x: str(x).zfill(2)):
                interface_app._set_datetime(timezone=mock_timezone)

        mock_datetime.now.assert_called_once_with(mock_timezone)
