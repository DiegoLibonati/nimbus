from src.configs.production_config import ProductionConfig


class TestProductionConfig:
    def test_debug_is_false(self) -> None:
        config: ProductionConfig = ProductionConfig()
        assert config.DEBUG is False

    def test_env_is_production(self) -> None:
        config: ProductionConfig = ProductionConfig()
        assert config.ENV == "production"

    def test_testing_is_false(self) -> None:
        config: ProductionConfig = ProductionConfig()
        assert config.TESTING is False

    def test_inherits_default_tz(self) -> None:
        config: ProductionConfig = ProductionConfig()
        assert config.TZ == "America/Argentina/Buenos_Aires"

    def test_has_api_key_attribute(self) -> None:
        config: ProductionConfig = ProductionConfig()
        assert hasattr(config, "API_KEY")

    def test_has_api_url_attribute(self) -> None:
        config: ProductionConfig = ProductionConfig()
        assert hasattr(config, "API_URL")
