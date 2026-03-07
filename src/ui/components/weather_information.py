from tkinter import Frame, Label, Misc, PhotoImage, StringVar
from typing import Any

from src.ui.styles import Styles


class WeatherInformation(Frame):
    def __init__(self, parent: Misc, styles: Styles, img_box: PhotoImage) -> None:
        super().__init__(parent, bg=styles.PRIMARY_COLOR)
        self._styles = styles
        self._img_box = img_box

        self._wind_text = StringVar()
        self._wind_value = StringVar()
        self._humidity_text = StringVar()
        self._humidity_value = StringVar()
        self._description_text = StringVar()
        self._description_value = StringVar()
        self._pressure_text = StringVar()
        self._pressure_value = StringVar()

        self._create_widgets()

    def _create_widgets(self) -> None:
        Label(
            self,
            image=self._img_box,
            border=0,
            bg=self._styles.PRIMARY_COLOR,
        ).pack(padx=5, pady=5, side=self._styles.SIDE_BOTTOM)

        stats = [
            (self._wind_text, self._wind_value, 130),
            (self._humidity_text, self._humidity_value, 305),
            (self._description_text, self._description_value, 505),
            (self._pressure_text, self._pressure_value, 700),
        ]

        for text_var, value_var, x in stats:
            Label(
                self,
                font=self._styles.FONT_POPPINS_20,
                textvariable=text_var,
                bg=self._styles.WHITE_COLOR,
                fg=self._styles.PRIMARY_COLOR,
                border=0,
            ).place(x=x, y=35, anchor=self._styles.ANCHOR_CENTER)

            Label(
                self,
                font=self._styles.FONT_POPPINS_22,
                textvariable=value_var,
                bg=self._styles.WHITE_COLOR,
                fg=self._styles.PRIMARY_COLOR,
                border=0,
            ).place(x=x, y=70, anchor=self._styles.ANCHOR_CENTER)

    def set_values(self, parsed: dict[str, Any]) -> None:
        self._wind_text.set("WIND")
        self._humidity_text.set("HUMIDITY")
        self._description_text.set("DESCRIPTION")
        self._pressure_text.set("PRESSURE")

        self._wind_value.set(parsed["wind"])
        self._humidity_value.set(parsed["humidity"])
        self._description_value.set(parsed["description"])
        self._pressure_value.set(parsed["pressure"])
