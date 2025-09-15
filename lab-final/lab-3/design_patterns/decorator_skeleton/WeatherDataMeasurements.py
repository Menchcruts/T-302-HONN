from dataclasses import dataclass


@dataclass
class WeatherDataMeasurements:
    temperature: float
    humidity: float
    pressure: float
