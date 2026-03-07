import os


class DefaultConfig:
    def __init__(self) -> None:
        # General
        self.TZ = os.getenv("TZ", "America/Argentina/Buenos_Aires")
        self.DEBUG = False
        self.TESTING = False

        # App
        self.API_KEY = os.getenv("API_KEY", "YOUR_API_KEY")
        self.API_URL = os.getenv("API_URL", "YOUR_API_URL")
