from tkinter import BOTTOM, CENTER, FLAT

from src.ui.styles import Styles


class TestStyles:
    def test_primary_color(self) -> None:
        assert Styles.PRIMARY_COLOR == "#4c75bd"

    def test_secondary_color(self) -> None:
        assert Styles.SECONDARY_COLOR == "#F37878"

    def test_white_color(self) -> None:
        assert Styles.WHITE_COLOR == "#FFFFFF"

    def test_black_color(self) -> None:
        assert Styles.BLACK_COLOR == "#000000"

    def test_font_poppins_base(self) -> None:
        assert Styles.FONT_POPPINS == "poppins"

    def test_font_poppins_12(self) -> None:
        assert Styles.FONT_POPPINS_12 == "poppins 12"

    def test_font_poppins_13(self) -> None:
        assert Styles.FONT_POPPINS_13 == "poppins 13"

    def test_font_poppins_40(self) -> None:
        assert Styles.FONT_POPPINS_40 == "poppins 40"

    def test_font_poppins_bold_25(self) -> None:
        assert Styles.FONT_POPPINS_BOLD_25 == "poppins 25 bold"

    def test_center_equals_tkinter_center(self) -> None:
        assert Styles.CENTER == CENTER

    def test_justify_center_equals_tkinter_center(self) -> None:
        assert Styles.JUSTIFY_CENTER == CENTER

    def test_anchor_center_equals_tkinter_center(self) -> None:
        assert Styles.ANCHOR_CENTER == CENTER

    def test_side_bottom_equals_tkinter_bottom(self) -> None:
        assert Styles.SIDE_BOTTOM == BOTTOM

    def test_relief_flat_equals_tkinter_flat(self) -> None:
        assert Styles.RELIEF_FLAT == FLAT

    def test_cursor_hand2(self) -> None:
        assert Styles.CURSOR_HAND2 == "hand2"

    def test_font_poppins_14(self) -> None:
        assert Styles.FONT_POPPINS_14 == "poppins 14"

    def test_font_poppins_15(self) -> None:
        assert Styles.FONT_POPPINS_15 == "poppins 15"

    def test_font_poppins_16(self) -> None:
        assert Styles.FONT_POPPINS_16 == "poppins 16"

    def test_font_poppins_20(self) -> None:
        assert Styles.FONT_POPPINS_20 == "poppins 20"

    def test_font_poppins_22(self) -> None:
        assert Styles.FONT_POPPINS_22 == "poppins 22"
