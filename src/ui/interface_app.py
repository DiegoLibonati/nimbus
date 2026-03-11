from datetime import datetime
from tkinter import PhotoImage, Tk

import pytz

from src.configs.default_config import DefaultConfig
from src.constants.messages import MESSAGE_ERROR_NOT_VALID_LOCATION
from src.constants.paths import PATH_BOX, PATH_LOGO, PATH_SEARCH, PATH_SEARCH_ICON
from src.services.weather_service import WeatherService
from src.ui.styles import Styles
from src.ui.views.main_view import MainView
from src.utils.helpers import add_zero, parse_weather_data


class InterfaceApp:
    def __init__(self, root: Tk, config: DefaultConfig, styles: Styles = Styles()) -> None:
        self._styles = styles
        self._config = config
        self._root = root
        self._root.title("Weather APP")
        self._root.geometry("900x500+300+200")
        self._root.resizable(False, False)
        self._root.config(background=self._styles.PRIMARY_COLOR)

        self._weather_service = WeatherService(api_key=config.API_KEY, api_url=config.API_URL)

        self._img_search = PhotoImage(file=PATH_SEARCH)
        self._img_search_icon = PhotoImage(file=PATH_SEARCH_ICON)
        self._img_logo = PhotoImage(file=PATH_LOGO)
        self._img_box = PhotoImage(file=PATH_BOX)

        self._main_view = MainView(
            root=self._root,
            styles=self._styles,
            on_search=self._get_weather,
            img_search=self._img_search,
            img_search_icon=self._img_search_icon,
            img_logo=self._img_logo,
            img_box=self._img_box,
        )
        self._main_view.place(x=0, y=0, width=900, height=500)

    def _get_weather(self) -> None:
        entry_place_value = self._main_view.get_place()
        if not entry_place_value:
            raise ValueError(MESSAGE_ERROR_NOT_VALID_LOCATION)

        self._main_view.set_static_labels()

        location = self._weather_service.get_place_information(entry_place_value)
        timezone = pytz.timezone(location["timezone"])

        self._set_datetime(timezone=timezone)

        weather_data = self._weather_service.get_weather_by_location(
            longitude=round(location["longitude"]),
            latitude=round(location["latitude"]),
        )
        parsed = parse_weather_data(weather_data)

        self._main_view.set_weather(parsed)

    def _set_datetime(self, timezone) -> None:
        time_now_by_timezone = datetime.now(timezone)
        hours = time_now_by_timezone.hour
        minutes = time_now_by_timezone.minute

        suffix = "PM" if 12 <= hours <= 23 else "AM"
        self._main_view.set_time(f"{add_zero(hours)}:{add_zero(minutes)} {suffix}")
