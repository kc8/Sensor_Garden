import RPi.GPIO as GPIO
from .exceptions import ADCChannelError
from .gpio_pin_config import GPIOPins
from Adafruit_ADS1x15 import ADS1015
from sensors_observers.observer import Observable


class SoilMoisture(Observable):

    def __init__(self, read_times: int, adc_channel: int, GPIO_pins: object, gain=1, friendly_name=None):
        """
        A class that reads values from an ADC which is connected to a soil moisture probe. This class
        will interpret the data to give an estimate of the moisture content in the water.

        The higher the amount of reads the more accurate the moisture amount is. Unfortunatley, this operation
        results in more resource use and a longer read time.
        :arg
            :gain: Default 1. The ADC gain error is is an offset error calculation

        """
        Observable.__init__(self)
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
        self._prior_value = 9999
        self.friendly_name = friendly_name
        self.opts = {}

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

    def _calculate_percent(self, voltage, reference_voltage=3300):
        """
        Caclulates the % of moisture where the reference voltage is the whole and the voltage is the part
        :param voltage: part or voltage being read
        :param reference_voltage: The whole or the reference voltage
        :return: % of moisture based on the voltage
        """
        return (voltage/reference_voltage)*100

    def data_refresh(self, object_sensor_to_update=""):
        """
        :arg: object_sensor_to_update: this is the name of the sensor specific to the object
        Refreshes the sensor data and notifies observers if needed
        :return: void
        """
        new_value = self.read_values()
        if new_value-1 <= self._prior_value >= new_value+1:
            self._prior_value = new_value
            self.opts = {
                "sensor_id": object_sensor_to_update,
                "units_of_measure" : "% Saturation",
                "measurement_precise": new_value,
                "measurement_friendly": int(self._calculate_percent(new_value)),
                "common_name": self.friendly_name
            }
            self.notify(value=new_value, opts=object_sensor_to_update, kwarg_opts=self.opts)