import tkinter as tk
from unittest.mock import MagicMock

from src.ui.components.search_bar import SearchBar
from src.ui.styles import Styles


class TestSearchBar:
    def test_instantiation(self, root: tk.Tk, blank_photo: tk.PhotoImage) -> None:
        bar: SearchBar = SearchBar(
            parent=root,
            styles=Styles(),
            img_search=blank_photo,
            img_search_icon=blank_photo,
            on_search=lambda: None,
        )
        assert bar is not None

    def test_is_frame(self, root: tk.Tk, blank_photo: tk.PhotoImage) -> None:
        bar: SearchBar = SearchBar(
            parent=root,
            styles=Styles(),
            img_search=blank_photo,
            img_search_icon=blank_photo,
            on_search=lambda: None,
        )
        assert isinstance(bar, tk.Frame)

    def test_get_place_returns_empty_by_default(self, root: tk.Tk, blank_photo: tk.PhotoImage) -> None:
        bar: SearchBar = SearchBar(
            parent=root,
            styles=Styles(),
            img_search=blank_photo,
            img_search_icon=blank_photo,
            on_search=lambda: None,
        )
        assert bar.get_place() == ""

    def test_get_place_returns_set_value(self, root: tk.Tk, blank_photo: tk.PhotoImage) -> None:
        bar: SearchBar = SearchBar(
            parent=root,
            styles=Styles(),
            img_search=blank_photo,
            img_search_icon=blank_photo,
            on_search=lambda: None,
        )
        bar._entry_place.set("Buenos Aires")
        assert bar.get_place() == "Buenos Aires"

    def test_get_place_returns_updated_value(self, root: tk.Tk, blank_photo: tk.PhotoImage) -> None:
        bar: SearchBar = SearchBar(
            parent=root,
            styles=Styles(),
            img_search=blank_photo,
            img_search_icon=blank_photo,
            on_search=lambda: None,
        )
        bar._entry_place.set("London")
        bar._entry_place.set("Tokyo")
        assert bar.get_place() == "Tokyo"

    def test_on_search_callback_is_stored(self, root: tk.Tk, blank_photo: tk.PhotoImage) -> None:
        callback: MagicMock = MagicMock()
        bar: SearchBar = SearchBar(
            parent=root,
            styles=Styles(),
            img_search=blank_photo,
            img_search_icon=blank_photo,
            on_search=callback,
        )
        assert bar._on_search is callback

    def test_entry_place_is_string_var(self, root: tk.Tk, blank_photo: tk.PhotoImage) -> None:
        bar: SearchBar = SearchBar(
            parent=root,
            styles=Styles(),
            img_search=blank_photo,
            img_search_icon=blank_photo,
            on_search=lambda: None,
        )
        assert isinstance(bar._entry_place, tk.StringVar)
