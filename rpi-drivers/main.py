#!/usr/bin/python3
from sensors_observers.sensors import AmbientTemperature, AmbientHumidity, AmbientPressure,\
                                        Temperature, GPIOPins, SoilMoisture
from sensors_observers.observer import Observable, Observer
from updaters import UpdateSensorGardenBackend
import os

# To-Do: Need to think of a better way to handle these updates rather than just one
#     large Class

if __name__ == '__main__':

    # The names of the sensors which are also the columns, fields IDs, or names  in our observers
    sensor_names = [
        "soil_moisture_plant_1",
        "soil_moisture_plant_2",
        "soil_temp_plant_1",
        "soil_temp_plant_2",
        "ambient_temp",
        "ambient_humidity",
        "ambient_pressure",
    ]
    # Create the soil mositure temperature observable
    soil_gpio_pins = GPIOPins((26, 16))
    soil_moisture_plant_1_observable = SoilMoisture(read_times=4, adc_channel=1, GPIO_pins=soil_gpio_pins,
                                                    friendly_name="Soil Moisture Plant 1")
    soil_moisture_plant_2_observable = SoilMoisture(read_times=4, adc_channel=2, GPIO_pins=soil_gpio_pins,
                                                    friendly_name="Soil Moisture Plant 2")
    # Create soil temperature
    soil_temp_1_observable = Temperature(device_file="28-0316b09095ff", friendly_name="Soil Temperature Plant 1")
    soil_temp_2_observable = Temperature(device_file="28-0516b045b5ff", friendly_name="Soil Temperature Plant 2")
    # Create ambient sensors
    ambient_temperature = AmbientTemperature(friendly_name="Ambient Temperature")
    ambient_humidity = AmbientHumidity(friendly_name="Ambient Humidity")
    ambient_pressure = AmbientPressure(friendly_name="Ambient Pressure")
    # Create Observers:
    sgb_observer = UpdateSensorGardenBackend()

    # Add observers to observables for notification
    soil_moisture_plant_2_observable.add(sgb_observer)
    soil_moisture_plant_1_observable.add(sgb_observer)
    soil_temp_1_observable.add(sgb_observer)
    soil_temp_2_observable.add(sgb_observer)
    ambient_humidity.add(sgb_observer)
    ambient_pressure.add(sgb_observer)
    ambient_temperature.add(sgb_observer)

    while True:
        soil_moisture_plant_1_observable.data_refresh(sensor_names[0])
        soil_moisture_plant_2_observable.data_refresh(sensor_names[1])
        soil_temp_1_observable.data_refresh(sensor_names[2])
        ambient_temperature.data_refresh(sensor_names[4])
        ambient_humidity.data_refresh(sensor_names[5])
        ambient_pressure.data_refresh(sensor_names[6])
        soil_temp_2_observable.data_refresh(sensor_names[3])

