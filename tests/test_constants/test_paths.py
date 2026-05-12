from src.constants import paths


class TestPaths:
    def test_path_box_is_str(self) -> None:
        assert isinstance(paths.PATH_BOX, str)

    def test_path_logo_is_str(self) -> None:
        assert isinstance(paths.PATH_LOGO, str)

    def test_path_search_icon_is_str(self) -> None:
        assert isinstance(paths.PATH_SEARCH_ICON, str)

    def test_path_search_is_str(self) -> None:
        assert isinstance(paths.PATH_SEARCH, str)

    def test_path_box_ends_with_box_png(self) -> None:
        assert paths.PATH_BOX.endswith("box.png")

    def test_path_logo_ends_with_logo_png(self) -> None:
        assert paths.PATH_LOGO.endswith("logo.png")

    def test_path_search_icon_ends_with_search_icon_png(self) -> None:
        assert paths.PATH_SEARCH_ICON.endswith("search_icon.png")

    def test_path_search_ends_with_search_png(self) -> None:
        assert paths.PATH_SEARCH.endswith("search.png")

    def test_all_paths_not_empty(self) -> None:
        all_paths: list[str] = [
            paths.PATH_BOX,
            paths.PATH_LOGO,
            paths.PATH_SEARCH_ICON,
            paths.PATH_SEARCH,
        ]
        for p in all_paths:
            assert len(p) > 0
