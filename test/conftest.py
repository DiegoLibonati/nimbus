from tkinter import PhotoImage, StringVar
from unittest.mock import MagicMock

import pytest

from src.ui.styles import Styles


@pytest.fixture
def mock_root() -> MagicMock:
    root: MagicMock = MagicMock()
    root.title = MagicMock()
    root.geometry = MagicMock()
    root.resizable = MagicMock()
    root.config = MagicMock()
    root.columnconfigure = MagicMock()
    root.rowconfigure = MagicMock()
    return root


@pytest.fixture
def mock_styles() -> MagicMock:
    styles: MagicMock = MagicMock()
    styles.PRIMARY_COLOR = "#4c75bd"
    styles.SECONDARY_COLOR = "#F37878"
    styles.WHITE_COLOR = "#FFFFFF"
    styles.BLACK_COLOR = "#000000"
    styles.FONT_POPPINS_15 = "poppins 15"
    styles.FONT_POPPINS_16 = "poppins 16"
    styles.FONT_POPPINS_20 = "poppins 20"
    styles.FONT_POPPINS_22 = "poppins 22"
    styles.FONT_POPPINS_40 = "poppins 40"
    styles.FONT_POPPINS_BOLD_25 = "poppins 25 bold"
    styles.RELIEF_FLAT = "flat"
    styles.CURSOR_HAND2 = "hand2"
    styles.JUSTIFY_CENTER = "center"
    styles.ANCHOR_CENTER = "center"
    styles.SIDE_BOTTOM = "bottom"
    return styles


@pytest.fixture
def real_styles() -> Styles:
    return Styles()


@pytest.fixture
def mock_on_search() -> MagicMock:
    return MagicMock()


@pytest.fixture
def mock_img() -> MagicMock:
    return MagicMock(spec=PhotoImage)


@pytest.fixture
def variable() -> MagicMock:
    return MagicMock(spec=StringVar)
