import os
from tkinter import Tk

from dotenv import load_dotenv

from src.configs.development_config import DevelopmentConfig
from src.configs.production_config import ProductionConfig
from src.configs.testing_config import TestingConfig
from src.ui.interface_app import InterfaceApp
from src.utils.tkinter_exception_hook import tkinter_exception_hook

CONFIG_MAP = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig,
}


def main(environment: str = "production") -> None:
    load_dotenv()

    environment = os.getenv("ENVIRONMENT", environment)

    root = Tk()
    root.report_callback_exception = tkinter_exception_hook

    config_class = CONFIG_MAP.get(environment, ProductionConfig)
    config = config_class()

    InterfaceApp(root=root, config=config)
    root.mainloop()


if __name__ == "__main__":
    main(environment="development")
