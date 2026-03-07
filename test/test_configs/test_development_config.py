from src.configs.default_config import DefaultConfig
from src.configs.development_config import DevelopmentConfig


class TestDevelopmentConfig:
    def test_inherits_from_default_config(self) -> None:
        assert issubclass(DevelopmentConfig, DefaultConfig)

    def test_debug_is_true(self) -> None:
        config: DevelopmentConfig = DevelopmentConfig()
        assert config.DEBUG is True

    def test_env_is_development(self) -> None:
        config: DevelopmentConfig = DevelopmentConfig()
        assert config.ENV == "development"

    def test_testing_is_false(self) -> None:
        config: DevelopmentConfig = DevelopmentConfig()
        assert config.TESTING is False

    def test_api_key_is_inherited(self) -> None:
        config: DevelopmentConfig = DevelopmentConfig()
        assert isinstance(config.API_KEY, str)
