from CurrentConditionsDisplay import CurrentConditionsDisplay
from ForecastDisplay import ForecastDisplay
from StatisticsDisplay import StatisticsDisplay
from WeatherData import WeatherData
from WeatherDataMeasurements import WeatherDataMeasurements

if __name__ == '__main__':
    weather_data = WeatherData()
    current_conditions_display = CurrentConditionsDisplay()
    statistics_display = StatisticsDisplay()
    forecast_display = ForecastDisplay()

    weather_data.register_observer(current_conditions_display)
    weather_data.register_observer(statistics_display)
    weather_data.register_observer(forecast_display)

    weather_data.set_measurements(WeatherDataMeasurements(80, 65, 30.4))
    print('---')
    weather_data.set_measurements(WeatherDataMeasurements(80.5, 65, 29.5))
    print('---')
    weather_data.set_measurements(WeatherDataMeasurements(78, 90, 29.2))

    print('\n------removing forecast display------\n')

    weather_data.remove_observer(forecast_display)
    weather_data.set_measurements(WeatherDataMeasurements(76, 85, 32.2))

    print('\n------removing statistics display------\n')

    weather_data.remove_observer(statistics_display)
    weather_data.set_measurements(WeatherDataMeasurements(81, 84, 32))

    print('\n------removing current conditions display------\n')

    weather_data.remove_observer(current_conditions_display)
    weather_data.set_measurements(WeatherDataMeasurements(81, 84, 32))