from tkinter import StringVar
from unittest.mock import MagicMock, patch

import pytest

from src.ui.components.search_bar import SearchBar


@pytest.fixture
def search_bar(mock_styles: MagicMock, mock_on_search: MagicMock, mock_img: MagicMock) -> SearchBar:
    with (
        patch("src.ui.components.search_bar.Frame.__init__", return_value=None),
        patch("src.ui.components.search_bar.Label"),
        patch("src.ui.components.search_bar.Entry"),
        patch("src.ui.components.search_bar.Button"),
        patch("src.ui.components.search_bar.StringVar"),
    ):
        instance: SearchBar = SearchBar.__new__(SearchBar)
        instance._styles = mock_styles
        instance._img_search = mock_img
        instance._img_search_icon = mock_img
        instance._on_search = mock_on_search
        instance._entry_place = MagicMock(spec=StringVar)
        return instance


class TestSearchBarInit:
    def test_stores_styles(self, search_bar: SearchBar, mock_styles: MagicMock) -> None:
        assert search_bar._styles == mock_styles

    def test_stores_on_search(self, search_bar: SearchBar, mock_on_search: MagicMock) -> None:
        assert search_bar._on_search == mock_on_search

    def test_stores_img_search(self, search_bar: SearchBar, mock_img: MagicMock) -> None:
        assert search_bar._img_search == mock_img

    def test_stores_img_search_icon(self, search_bar: SearchBar, mock_img: MagicMock) -> None:
        assert search_bar._img_search_icon == mock_img

    def test_entry_is_created_with_variable(self, mock_styles: MagicMock, mock_on_search: MagicMock, mock_img: MagicMock) -> None:
        with (
            patch("src.ui.components.search_bar.Frame.__init__", return_value=None),
            patch("src.ui.components.search_bar.Label") as mock_label,
            patch("src.ui.components.search_bar.Entry") as mock_entry,
            patch("src.ui.components.search_bar.Button") as mock_button,
            patch("src.ui.components.search_bar.StringVar") as mock_string_var,
        ):
            mock_label.return_value.place = MagicMock()
            mock_entry.return_value.place = MagicMock()
            mock_button.return_value.place = MagicMock()
            mock_var: MagicMock = MagicMock(spec=StringVar)
            mock_string_var.return_value = mock_var
            instance: SearchBar = SearchBar.__new__(SearchBar)
            instance._styles = mock_styles
            SearchBar.__init__(
                instance,
                parent=MagicMock(),
                styles=mock_styles,
                img_search=mock_img,
                img_search_icon=mock_img,
                on_search=mock_on_search,
            )

        _, kwargs = mock_entry.call_args
        assert kwargs.get("textvariable") == mock_var

    def test_button_command_is_on_search(self, mock_styles: MagicMock, mock_on_search: MagicMock, mock_img: MagicMock) -> None:
        with (
            patch("src.ui.components.search_bar.Frame.__init__", return_value=None),
            patch("src.ui.components.search_bar.Label") as mock_label,
            patch("src.ui.components.search_bar.Entry") as mock_entry,
            patch("src.ui.components.search_bar.Button") as mock_button,
            patch("src.ui.components.search_bar.StringVar"),
        ):
            mock_label.return_value.place = MagicMock()
            mock_entry.return_value.place = MagicMock()
            mock_button.return_value.place = MagicMock()
            instance: SearchBar = SearchBar.__new__(SearchBar)
            instance._styles = mock_styles
            SearchBar.__init__(
                instance,
                parent=MagicMock(),
                styles=mock_styles,
                img_search=mock_img,
                img_search_icon=mock_img,
                on_search=mock_on_search,
            )

        _, kwargs = mock_button.call_args
        assert kwargs.get("command") == mock_on_search


class TestSearchBarGetPlace:
    def test_get_place_returns_entry_value(self, search_bar: SearchBar) -> None:
        search_bar._entry_place.get.return_value = "Buenos Aires"
        result: str = search_bar.get_place()
        assert result == "Buenos Aires"

    def test_get_place_returns_empty_string_when_empty(self, search_bar: SearchBar) -> None:
        search_bar._entry_place.get.return_value = ""
        result: str = search_bar.get_place()
        assert result == ""

    def test_get_place_calls_entry_get(self, search_bar: SearchBar) -> None:
        search_bar._entry_place.get.return_value = "London"
        search_bar.get_place()
        search_bar._entry_place.get.assert_called_once()
