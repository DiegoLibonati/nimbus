from tkinter import Frame, Label, PhotoImage, StringVar, Tk
from typing import Any

from src.ui.components.search_bar import SearchBar
from src.ui.components.weather_information import WeatherInformation
from src.ui.styles import Styles


class MainView(Frame):
    def __init__(
        self,
        root: Tk,
        styles: Styles,
        on_search: callable,
        img_search: PhotoImage,
        img_search_icon: PhotoImage,
        img_logo: PhotoImage,
        img_box: PhotoImage,
    ) -> None:
        super().__init__(root, bg=styles.PRIMARY_COLOR)
        self._styles = styles
        self._on_search = on_search
        self._img_search = img_search
        self._img_search_icon = img_search_icon
        self._img_logo = img_logo
        self._img_box = img_box

        self._label_current_weather = StringVar()
        self._label_time = StringVar()
        self._label_degrees = StringVar()
        self._label_thermal_sensation = StringVar()

        self._create_widgets()

    def _create_widgets(self) -> None:
        self._search_bar = SearchBar(
            parent=self,
            styles=self._styles,
            img_search=self._img_search,
            img_search_icon=self._img_search_icon,
            on_search=self._on_search,
        )
        self._search_bar.place(x=20, y=20, width=460, height=70)

        Label(
            self,
            image=self._img_logo,
            border=0,
            bg=self._styles.PRIMARY_COLOR,
        ).place(x=150, y=100)

        Label(
            self,
            font=self._styles.FONT_POPPINS_15,
            textvariable=self._label_current_weather,
            bg=self._styles.PRIMARY_COLOR,
            fg=self._styles.BLACK_COLOR,
            border=0,
        ).place(x=35, y=95)

        Label(
            self,
            font=self._styles.FONT_POPPINS_16,
            textvariable=self._label_time,
            bg=self._styles.PRIMARY_COLOR,
            fg=self._styles.BLACK_COLOR,
            border=0,
        ).place(x=35, y=120)

        Label(
            self,
            font=self._styles.FONT_POPPINS_40,
            textvariable=self._label_degrees,
            bg=self._styles.PRIMARY_COLOR,
            fg=self._styles.SECONDARY_COLOR,
            border=0,
        ).place(x=410, y=190)

        Label(
            self,
            font=self._styles.FONT_POPPINS_20,
            textvariable=self._label_thermal_sensation,
            bg=self._styles.PRIMARY_COLOR,
            fg=self._styles.SECONDARY_COLOR,
            border=0,
        ).place(x=410, y=250)

        self._weather_information = WeatherInformation(
            parent=self,
            styles=self._styles,
            img_box=self._img_box,
        )
        self._weather_information.place(x=0, y=390, width=900, height=110)

    def get_place(self) -> str:
        return self._search_bar.get_place()

    def set_static_labels(self) -> None:
        self._label_current_weather.set("CURRENT WEATHER")

    def set_time(self, time: str) -> None:
        self._label_time.set(time)

    def set_weather(self, parsed: dict[str, Any]) -> None:
        self._label_degrees.set(f"{parsed['temp']}°")
        self._label_thermal_sensation.set(f"{parsed['description']} | FEELS LIKE {parsed['feels_like']}°")
        self._weather_information.set_values(parsed)
