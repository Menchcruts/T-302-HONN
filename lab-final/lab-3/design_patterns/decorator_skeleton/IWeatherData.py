from abc import ABC, abstractmethod

from WeatherDataMeasurements import WeatherDataMeasurements


class IWeatherData(ABC):
    @abstractmethod
    def set_measurements(self, measurements: WeatherDataMeasurements) -> None:
        pass

    @abstractmethod
    def get_measurements(self) -> WeatherDataMeasurements:
        pass
