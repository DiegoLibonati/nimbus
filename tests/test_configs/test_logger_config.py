import logging

from src.configs.logger_config import setup_logger


class TestSetupLogger:
    def test_returns_logger(self) -> None:
        logger: logging.Logger = setup_logger()
        assert isinstance(logger, logging.Logger)

    def test_default_name(self) -> None:
        logger: logging.Logger = setup_logger()
        assert logger.name == "tkinter-app"

    def test_custom_name(self) -> None:
        logger: logging.Logger = setup_logger("custom-logger")
        assert logger.name == "custom-logger"

    def test_logger_level_is_debug(self) -> None:
        logger: logging.Logger = setup_logger("level-test-logger")
        assert logger.level == logging.DEBUG

    def test_logger_has_handler(self) -> None:
        logger: logging.Logger = setup_logger("handler-test-logger")
        assert len(logger.handlers) > 0

    def test_idempotent_handlers(self) -> None:
        logger: logging.Logger = setup_logger("idempotent-logger")
        count_first: int = len(logger.handlers)
        setup_logger("idempotent-logger")
        assert len(logger.handlers) == count_first
