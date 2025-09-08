from Observer import Observer
from DisplayElement import DisplayElement

from IWeatherData import IWeatherData

class StatisticsDisplay(Observer, DisplayElement):
    def __init__(self):
        super().__init__()
        self.__temperatures: list[float] = list()
    
    def update(self, observable: IWeatherData):
        if isinstance(observable, IWeatherData):
            weather_data: IWeatherData = observable
            measurements = weather_data.get_measurements()
            self.__temperatures.append(measurements.temperature)
            self.display()
    
    def display(self):
        temp_avg = sum(self.__temperatures)/len(self.__temperatures)
        temp_max = max(self.__temperatures)
        temp_min = min(self.__temperatures)
        print(f"Avg/Max/Min temperature = {temp_avg:.1f}/{temp_max:.1f}/{temp_min:.1f}")