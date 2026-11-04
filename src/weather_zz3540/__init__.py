"""Weather utilities package."""

from importlib.metadata import version

from .weather_zz3540 import (
    celsius_to_fahrenheit,
    clean_readings,
    summarize_temperatures,
)

__version__ = version("weather_zz3540")
