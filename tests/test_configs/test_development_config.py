from src.configs.development_config import DevelopmentConfig


class TestDevelopmentConfig:
    def test_debug_is_true(self) -> None:
        config: DevelopmentConfig = DevelopmentConfig()
        assert config.DEBUG is True

    def test_env_is_development(self) -> None:
        config: DevelopmentConfig = DevelopmentConfig()
        assert config.ENV == "development"

    def test_testing_is_false(self) -> None:
        config: DevelopmentConfig = DevelopmentConfig()
        assert config.TESTING is False

    def test_inherits_default_tz(self) -> None:
        config: DevelopmentConfig = DevelopmentConfig()
        assert config.TZ == "America/Argentina/Buenos_Aires"

    def test_has_api_key_attribute(self) -> None:
        config: DevelopmentConfig = DevelopmentConfig()
        assert hasattr(config, "API_KEY")

    def test_has_api_url_attribute(self) -> None:
        config: DevelopmentConfig = DevelopmentConfig()
        assert hasattr(config, "API_URL")
