from sensors import AmbientSensor, Temperature, GPIOPins, SoilMoisture
from observer import Observable
from updaters import UpdateFirestore
from observer import Observer

# To-Do: Need to think of a better way to handle these updates rather than just one
#     large Class
class SensorReadings(Observable):

    def __init__(self):
        Observable.__init__(self)
        # Soil moisture content:
        self.soil_moisture_plant_1 = ""
        self.soil_moisture_plant_2 = ""
        # Soil temperature from plants
        self.soil_temp_plant_1 = ""
        self.soil_temp_plant_2 = ""
        # From BME200 sensor/ ambient sensor readings:
        self.ambient_temp = ""
        self.ambient_humidity = ""
        self.ambient_pressure = ""
        # Soil temperature from plants

    def ambient_sensor_refresh(self):
        ambient_readings = AmbientSensor()
        self.ambient_temp = ambient_readings.get_temp()
        self.ambient_humidity = ambient_readings.get_humidity()
        self.ambient_pressure = ambient_readings.get_pressure()

    def soil_moisture_refresh(self):
        """Reads the soil moisture content from both plants"""
        pins = GPIOPins((26, 16))
        soil_moisture_plant_1_device = SoilMoisture(1, 0, pins)
        soil_moisture_plant_2_device = SoilMoisture(2, 0, pins)
        self.soil_moisture_plant_1 = soil_moisture_plant_1_device.read_values()
        self.soil_moisture_plant_2 = soil_moisture_plant_2_device.read_values()

    def soil_temperature_refresh(self):
        soil_temp_1_device = Temperature(device_file="28-0316b09095ff")
        soil_temp_2_device = Temperature(device_file="28-0516b045b5ff")
        self.soil_temp_plant_1 = soil_temp_1_device.get_temperature()
        self.soil_temp_plant_2 = soil_temp_2_device.get_temperature()

    def data_refresh(self):
        """Callss all the update methods to check for new values"""
        # 1. Update new values with methods and set.
        # 2. Check each one against old values
        # 2.3. Call trigger_update if there is a change in the value

        #self._trigger_update(_readings)

    def _trigger_update(self, value):
        self.notify(value=value)


if __name__ == '__main__':
    # The names of the sensors which are also the columns, fields IDs, or names  in our observers
    sensor_names = [
        "soil_moisture_plant_1",
        "soil_moisture_plant_2",
        "soil_temp_plant_1",
        "soil_temp_plant_2",
        "ambient_temp" ,
        "ambient_humidity",
        "ambient_pressure",
    ]
    # Create the soil mositure temperature observable
    soil_gpio_pins = GPIOPins((26, 16))
    soil_moisture_plant_1_observable = SoilMoisture(1, 0, soil_gpio_pins)
    soil_moisture_plant_2_observable = SoilMoisture(2, 0, soil_gpio_pins)
    # Create Observers:
    firestore_observer = UpdateFirestore()
    # Add observers to observables for notification
    soil_moisture_plant_2_observable.add(firestore_observer)
    soil_moisture_plant_1_observable.add(firestore_observer)
    while True:
        soil_moisture_plant_1_observable.data_refresh(sensor_names[0])
        soil_moisture_plant_2_observable.data_refresh(sensor_names[1])


