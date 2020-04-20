from Adafruit_BME280 import *
from sensors import Observable


class AmbientSensor(Observable):

    def __init__(self):
        self._sensor = BME280(t_mode=BME280_OSAMPLE_8,
                              p_mode=BME280_OSAMPLE_8,
                              h_mode=BME280_OSAMPLE_8)
        self._prior_f_degrees = ""
        self._prior_pressure = ""
        self._prior_humidity = ""

    def get_temp(self):
        """return temperature in fahrenheit"""
        _f_degrees = self._sensor.read_temperature() * 9.0 / 5.0 + 32.0
        return round(_f_degrees, 3)

    def get_pressure(self):
        """'''returns the hectopascals (current pressure reading)'''"""
        _pascals = self._sensor.read_pressure()
        _hectopascals = _pascals / 100
        return round(_hectopascals, 3)

    def get_humidity(self):
        """'''returns the current humidity reading'''"""
        _humidity = self._sensor.read_humidity()
        return round(_humidity, 3)

    def update(self, value):
        self.notify(value)