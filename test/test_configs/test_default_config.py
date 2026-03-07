from src.configs.default_config import DefaultConfig


class TestDefaultConfig:
    def test_debug_is_false(self) -> None:
        config: DefaultConfig = DefaultConfig()
        assert config.DEBUG is False

    def test_testing_is_false(self) -> None:
        config: DefaultConfig = DefaultConfig()
        assert config.TESTING is False

    def test_tz_has_default_value(self) -> None:
        config: DefaultConfig = DefaultConfig()
        assert config.TZ == "America/Argentina/Buenos_Aires"

    def test_api_key_has_default_value(self) -> None:
        config: DefaultConfig = DefaultConfig()
        assert config.API_KEY == "YOUR_API_KEY"

    def test_api_url_has_default_value(self) -> None:
        config: DefaultConfig = DefaultConfig()
        assert config.API_URL == "https://api.openweathermap.org/data/2.5"

    def test_tz_is_string(self) -> None:
        config: DefaultConfig = DefaultConfig()
        assert isinstance(config.TZ, str)

    def test_api_key_is_string(self) -> None:
        config: DefaultConfig = DefaultConfig()
        assert isinstance(config.API_KEY, str)

    def test_api_url_is_string(self) -> None:
        config: DefaultConfig = DefaultConfig()
        assert isinstance(config.API_URL, str)
