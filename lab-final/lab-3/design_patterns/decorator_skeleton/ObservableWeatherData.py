from abc import ABC

from IWeatherData import IWeatherData
from Observable import Observable

from WeatherData import WeatherData

class ObservableWeatherData(Observable, IWeatherData, ABC):
    def __init__(self, weather_data: WeatherData):
        super().__init__()
        self.__weather_data = weather_data
    
    def set_measurements(self, measurements):
        update = False
        current_measurements = self.__weather_data.get_measurements()
        self.__weather_data.set_measurements(measurements)

        if abs(current_measurements.temperature - measurements.temperature) >= 1:
            update = True
        elif abs(current_measurements.humidity - measurements.humidity) >= 1:
            update = True
        elif abs(current_measurements.pressure - measurements.pressure) >= 1:
            update = True
        
        if update:
            self.__weather_data.notify_observers()

    def get_measurements(self):
        return self.__weather_data.get_measurements()

    def register_observer(self, observer):
        self.__weather_data.register_observer(observer)
    
    def remove_observer(self, observer):
        self.__weather_data.remove_observer(observer)

    def notify_observers(self):
        self.__weather_data.notify_observers()