import RPi.GPIO as GPIO
from .exceptions import ADCChannelError
from .gpio_pin_config import GPIOPins
from Adafruit_ADS1x15 import ADS1015
from sensors import Observable


class SoilMoisture(Observable):

    def __init__(self, read_times: int, adc_channel: int, GPIO_pins: object, gain=1):
        """
        A class that reads values from an ADC which is connected to a soil moisture probe. This class
        will interpret the data to give an estimate of the moisture content in the water.

        The higher the amount of reads the more accurate the moisture amount is. Unfortunatley, this operation
        results in more resource use and a longer read time.
        :arg
            :gain: Default 1. The ADC gain error is is an offset error calculation

        """
        self._gain = gain
        self._read_times = read_times
        self._soil_moisture_content = None
        self._adc_reader = ADS1015()
        if adc_channel > 3 or adc_channel < 3:
            self._adc_channel = adc_channel
        else:
            raise ADCChannelError("Error creating ADC channel value must be between 0 - 3")
        self._gpio_pins_obj = GPIO_pins
        self._gpio_pins = []
        self._prior_value = ""

    def _setup_gpio_pins(self):
        """
        setup the gpio_pins to holding them in variables
        """
        for _ in self._gpio_pins_obj.get_pins():
            self._gpio_pins.append(_)

    def __str__(self):
        if self._soil_moisture_content is not None:
            return self._soil_moisture_content
        else:
            self.read_values()
            return self._soil_moisture_content

    def read_values(self) -> float:
        """"""
        _sub_total = 0
        self._setup_gpio_pins()
        GPIO.setmode(GPIO.BCM)
        for i in self._gpio_pins:
            GPIO.setup(i, GPIO.OUT)
        try:
            for i in self._gpio_pins:
                GPIO.output(i, 1)
            for i in range(self._read_times):
                _sub_total += self._adc_reader.read_adc(self._adc_channel, gain=self._gain)
            for i in self._gpio_pins:
                GPIO.output(i, 0)
        except:
            for i in self._gpio_pins:
                GPIO.output(i, 0)
            GPIO.cleanup()
            return "failed to get sensor reading"

        GPIO.cleanup()
        return _sub_total/self._read_times

    def data_refresh(self, object_sensor_to_update=""):
        """
        :arg: object_sensor_to_update: this is the name of the sensor specific to the object
        Refreshes the sensor data and notifies observers if needed
        :return: void
        """
        new_value = self.read_values()
        if self._prior_value != new_value:
            self.notify(value=new_value, opts=object_sensor_to_update)
            self._prior_value = new_value
