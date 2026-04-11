import os
from unittest.mock import patch

from src.configs.default_config import DefaultConfig


class TestDefaultConfig:
    def test_default_tz(self) -> None:
        config: DefaultConfig = DefaultConfig()
        assert config.TZ == "America/Argentina/Buenos_Aires"

    def test_default_debug(self) -> None:
        config: DefaultConfig = DefaultConfig()
        assert config.DEBUG is False

    def test_default_testing(self) -> None:
        config: DefaultConfig = DefaultConfig()
        assert config.TESTING is False

    def test_default_api_key(self) -> None:
        config: DefaultConfig = DefaultConfig()
        assert config.API_KEY == "YOUR_API_KEY"

    def test_default_api_url(self) -> None:
        env_without_api_url: dict[str, str] = {k: v for k, v in os.environ.items() if k != "API_URL"}
        with patch.dict("os.environ", env_without_api_url, clear=True):
            config: DefaultConfig = DefaultConfig()
            assert config.API_URL == "YOUR_API_URL"

    def test_tz_from_env(self) -> None:
        with patch.dict("os.environ", {"TZ": "UTC"}):
            config: DefaultConfig = DefaultConfig()
            assert config.TZ == "UTC"

    def test_api_key_from_env(self) -> None:
        with patch.dict("os.environ", {"API_KEY": "test_key_123"}):
            config: DefaultConfig = DefaultConfig()
            assert config.API_KEY == "test_key_123"

    def test_api_url_from_env(self) -> None:
        with patch.dict("os.environ", {"API_URL": "https://example.com"}):
            config: DefaultConfig = DefaultConfig()
            assert config.API_URL == "https://example.com"
