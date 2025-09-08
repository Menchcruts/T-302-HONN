from Observer import Observer
from DisplayElement import DisplayElement

from IWeatherData import IWeatherData
from WeatherDataMeasurements import WeatherDataMeasurements


class CurrentConditionsDisplay(Observer, DisplayElement):
    def __init__(self):
        super().__init__()
        self.__measurements: WeatherDataMeasurements = None
    
    def update(self, observable: IWeatherData):
        if isinstance(observable, IWeatherData):
            weather_data: IWeatherData = observable
            self.__measurements = weather_data.get_measurements()
            self.display()
    
    def display(self):
        if self.__measurements is not None:
            print(f"Current conditions: {self.__measurements.temperature:.1f}F degrees and {self.__measurements.humidity:.1f}% humidity")
