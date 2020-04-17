import os
import glob
import time
from exceptions import BaseTypeError


"""
here is an example of the data for the device that we need to be given: 
        os.system('modprobe w1-gpio')
        os.system('modprobe w1-therm')

        base_dir = '/sys/bus/w1/devices/'
        device_folder_tom0 = glob.glob(base_dir + '28-0316b09095ff')[0]
        device_folder_tom1 = glob.glob(base_dir + '28-0516b045b5ff')[0]
        device_file_tom0 = device_folder_tom0 + '/w1_slave'
        device_file_tom1 = device_folder_tom1 + '/w1_slave'
"""


class Temperature:

    def __init__(self, device_file: str, probe_directory='/w1_slave', base_dir='/sys/bus/w1/devices/'):
        """
        You will need to pass this object the serial ID of the temperature probe. Please read the documentation
        on how to find this value
        :param:
            probe_directory:
            device_file:
            base_dir: Default is '/sys/bus/w1/devices/'
        """
        self._device_file = device_file
        self._probe_directory = probe_directory
        self._temp = None # init but it will be none until invoke method to read
        self._base_dir = base_dir
        self._device = None # Setup in self._setup_devices()
        self._setup_devices() # We need to setup the devices in order to use them

    def __cmp__(self, other):
        """
        :param other:
        :return:
        """
        return self.temperature == other.temperature

    def __str__(self):
        return self.get_temperature()

    def _setup_devices(self):
        """
        Setup the devices and check for errors. Need to make sure what the user
        gave the object is a string. need to then convert them to the correct
        data types to ensure we can use them.
        :return:
        """
        if not isinstance(self._device_file, str):
            raise BaseTypeError
        if not isinstance(self._probe_directory, str):
            raise BaseTypeError

        # Need to change some OS level settings,
        # To-DO: Check to make sure these work properly and what errors we may need to handle
        os.system('modprobe w1-gpio')
        os.system('modprobe w1-therm')

        self._device_path = glob.glob(self._base_dir + self._device_file)[0]
        # Below is now the device needed to reference for the sensor:
        self._device = self._device_path + self._probe_directory

    def _read_temp_raw(self):
        """
        Reads the raw data from the temperature probe
        :arg
        :return:
        """

    def _read_temp(self):
        """
        Need to re-do this function and then combine with the read_raw if appropraite
        :return:
        """
        with open(self._device, 'r') as f:
            lines = f.readlines()
            f.close()
        #if lines[0].strip()[-3:] != 'YES':
        #    self.temp = lines[0].strip()[-3:]
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
            self._temp = lines[1][equals_pos+2:]

    def convert_temperature_measurement(self, temperature_system):
        """
        Converts the temperature to either Farenehiet (f) or Celcius (c).
        Please use F or c
        :arg
        """
        self._temp = float(self._temp) / 1000.0 # this is also the C value
        if temperature_system.lower() == 'f':
            return self._temp * 9.0 / 5.0 + 32.0
        elif temperature_system.lower() == 'c':
            return self._temp
        else:
            raise BaseTypeError

    def get_temperature(self):
        """
        Gets and returns the temperature of the probe
        :return: Returns the temperature of the probe in Fahrenheit
        """
        self._read_temp()
        if self._temp == None:
            return None
        self._temp = self.convert_temperature_measurement('f')
        return self._temp
