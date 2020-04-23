from Adafruit_BME280 import *
from sensors_observers.observer import Observable


class AmbientSensor(Observable):

    def __init__(self):
        self._sensor = BME280(t_mode=BME280_OSAMPLE_8,
                              p_mode=BME280_OSAMPLE_8,
                              h_mode=BME280_OSAMPLE_8)
        self._prior_measurement = 0
        self._measurement = 0
    # TO-DO: Create an abstract method?
    def get_measurement(self):
        pass

    def data_refresh(self, object_sensor_to_update=""):
        self.get_measurement()
        # We need to round the following or else we will be updating the DB with a long floating point number.
        if round(self._measurement) < round(self._prior_measurement) or \
                                    round(self._prior_measurement) < round(self._measurement):
            self._prior_measurement = self._measurement
            self.notify(self._measurement, object_sensor_to_update)


class AmbientTemperature(AmbientSensor):

    def __init__(self):
        AmbientSensor.__init__(self)

    def get_measurement(self):
        """return temperature in fahrenheit"""
        self._measurement = self._sensor.read_temperature() * 9.0 / 5.0 + 32.0
        return self._measurement


class AmbientPressure(AmbientSensor):

    def __init__(self):
        AmbientSensor.__init__(self)

    def get_measurement(self):
        """'''returns the hectopascals (current pressure reading)'''"""
        _pascals = self._sensor.read_pressure()
        _hectopascals = _pascals / 100
        self._measurement = _hectopascals
        return self._measurement


class AmbientHumidity(AmbientSensor):

    def __init__(self):
        AmbientSensor.__init__(self)

    def get_measurement(self):
        """'''returns the current humidity reading'''"""
        _humidity = self._sensor.read_humidity()
        self._measurement = _humidity
        return self._measurement

