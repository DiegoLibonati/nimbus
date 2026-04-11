from src.configs.testing_config import TestingConfig


class TestTestingConfig:
    def test_testing_is_true(self) -> None:
        config: TestingConfig = TestingConfig()
        assert config.TESTING is True

    def test_debug_is_true(self) -> None:
        config: TestingConfig = TestingConfig()
        assert config.DEBUG is True

    def test_env_is_testing(self) -> None:
        config: TestingConfig = TestingConfig()
        assert config.ENV == "testing"

    def test_inherits_default_tz(self) -> None:
        config: TestingConfig = TestingConfig()
        assert config.TZ == "America/Argentina/Buenos_Aires"

    def test_has_api_key_attribute(self) -> None:
        config: TestingConfig = TestingConfig()
        assert hasattr(config, "API_KEY")
