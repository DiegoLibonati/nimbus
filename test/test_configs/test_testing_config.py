from src.configs.default_config import DefaultConfig
from src.configs.testing_config import TestingConfig


class TestTestingConfig:
    def test_inherits_from_default_config(self) -> None:
        assert issubclass(TestingConfig, DefaultConfig)

    def test_testing_is_true(self) -> None:
        config: TestingConfig = TestingConfig()
        assert config.TESTING is True

    def test_debug_is_true(self) -> None:
        config: TestingConfig = TestingConfig()
        assert config.DEBUG is True

    def test_env_is_testing(self) -> None:
        config: TestingConfig = TestingConfig()
        assert config.ENV == "testing"

    def test_api_key_is_inherited(self) -> None:
        config: TestingConfig = TestingConfig()
        assert isinstance(config.API_KEY, str)
