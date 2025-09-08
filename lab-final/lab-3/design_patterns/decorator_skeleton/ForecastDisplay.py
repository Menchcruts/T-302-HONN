from Observer import Observer
from DisplayElement import DisplayElement

from IWeatherData import IWeatherData


class ForecastDisplay(Observer, DisplayElement):    
    def __init__(self):
        super().__init__()
        self.__last_pressure: float = 0.
        self.__current_pressure: float = 0.
        
    
    def update(self, observable):
        if isinstance(observable, IWeatherData):
            weather_data: IWeatherData = observable
            measurements = weather_data.get_measurements()
            self.__current_pressure = measurements.pressure
            self.display()
            
        return super().update(observable)
    
    def display(self):
        if self.__last_pressure > self.__current_pressure:
            print("Forecast: Watch out for cooler, rainy weather")
        elif self.__last_pressure == self.__current_pressure:
            print("Forecast: More of the same")
        elif self.__last_pressure < self.__current_pressure:
            print("Forecast: Improving weather on the way!")
        else: pass

        self.__last_pressure = self.__current_pressure
