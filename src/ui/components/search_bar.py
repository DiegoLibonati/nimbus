from tkinter import Button, Entry, Frame, Label, Misc, PhotoImage, StringVar

from src.ui.styles import Styles


class SearchBar(Frame):
    def __init__(
        self,
        parent: Misc,
        styles: Styles,
        img_search: PhotoImage,
        img_search_icon: PhotoImage,
        on_search: callable,
    ) -> None:
        super().__init__(parent, bg=styles.PRIMARY_COLOR)
        self._styles = styles
        self._img_search = img_search
        self._img_search_icon = img_search_icon
        self._on_search = on_search

        self._entry_place = StringVar()

        Label(
            self,
            image=self._img_search,
            border=0,
        ).place(x=0, y=0)

        Entry(
            self,
            bg=self._styles.WHITE_COLOR,
            width=20,
            font=self._styles.FONT_POPPINS_BOLD_25,
            fg=self._styles.PRIMARY_COLOR,
            justify=self._styles.JUSTIFY_CENTER,
            border=0,
            textvariable=self._entry_place,
        ).place(x=35, y=20)

        Button(
            self,
            image=self._img_search_icon,
            border=0,
            bg=self._styles.WHITE_COLOR,
            width=50,
            height=50,
            relief=self._styles.RELIEF_FLAT,
            cursor=self._styles.CURSOR_HAND2,
            command=self._on_search,
        ).place(x=390, y=12)

    def get_place(self) -> str:
        return self._entry_place.get()
