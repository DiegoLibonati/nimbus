import os
import sys
from typing import Any


def add_zero(value: int) -> str:
    if value >= 0 and value < 10:
        return f"0{value}"

    return str(value)


def parse_weather_data(data: dict[str, Any]) -> dict[str, Any]:
    kelvin_offset = 273.15

    return {
        "temp": int(data["main"]["temp"] - kelvin_offset),
        "feels_like": int(data["main"]["feels_like"] - kelvin_offset),
        "wind": data["wind"]["speed"],
        "description": data["weather"][0]["description"],
        "humidity": data["main"]["humidity"],
        "pressure": data["main"]["pressure"],
    }


def resource_path(relative_path: str) -> str:
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
