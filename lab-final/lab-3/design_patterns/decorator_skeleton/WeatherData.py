from Observable import Observable
from Observer import Observer

from IWeatherData import IWeatherData
from WeatherDataMeasurements import WeatherDataMeasurements

class WeatherData(IWeatherData, Observable):
    def __init__(self):
        super().__init__()
        self.__measurements = WeatherDataMeasurements(0, 0, 0)
        self.__observers: list[Observer] = list()
    
    def set_measurements(self, measurements):
        self.__measurements = measurements
        # self.notify_observers()
    
    def get_measurements(self):
        return self.__measurements
    
    def register_observer(self, observer):
        self.__observers.append(observer)
    
    def remove_observer(self, observer):
        self.__observers.remove(observer)
    
    def notify_observers(self):
        for observer in self.__observers:
            observer.update(self)
