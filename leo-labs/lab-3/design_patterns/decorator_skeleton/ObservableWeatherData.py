from abc import ABC

from IWeatherData import IWeatherData
from Observable import Observable


class ObservableWeatherData(Observable, IWeatherData, ABC):
    pass
