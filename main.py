#!/usr/bin/python3
from sensors_observers.sensors import AmbientTemperature, AmbientHumidity, AmbientPressure,\
                                        Temperature, GPIOPins, SoilMoisture
from sensors_observers.observer import Observable, Observer
from updaters import UpdateFirestore

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
    soil_moisture_plant_1_observable = SoilMoisture(read_times=4, adc_channel=1, GPIO_pins=soil_gpio_pins)
    soil_moisture_plant_2_observable = SoilMoisture(read_times=4, adc_channel=2, GPIO_pins=soil_gpio_pins)
    # Create soil temperature
    soil_temp_1_observable = Temperature(device_file="28-0316b09095ff")
    # soil_temp_2_observable = Temperature(device_file="") # Currently broken
    # Create ambient sensors
    ambient_temperature = AmbientTemperature()
    ambient_humidity = AmbientPressure()
    ambient_pressure = AmbientHumidity()
    # Create Observers:
    firestore_observer = UpdateFirestore()
    # Add observers to observables for notification
    soil_moisture_plant_2_observable.add(firestore_observer)
    soil_moisture_plant_1_observable.add(firestore_observer)
    soil_temp_1_observable.add(firestore_observer)
    ambient_humidity.add(firestore_observer)
    ambient_pressure.add(firestore_observer)
    ambient_temperature.add(firestore_observer)
    while True:
        soil_moisture_plant_1_observable.data_refresh(sensor_names[0])
        soil_moisture_plant_2_observable.data_refresh(sensor_names[1])
        soil_temp_1_observable.data_refresh(sensor_names[2])
        ambient_temperature.data_refresh(sensor_names[4])
        ambient_humidity.data_refresh(sensor_names[5])
        ambient_pressure.data_refresh(sensor_names[6])

