from sensors import SoilMoisture, GPIOPins,Temperature

temp = Temperature(device_file="28-0316b09095ff")

#device_file: str, device_folder: str,
"""        device_folder_tom0 = glob.glob(base_dir + '28-0316b09095ff')[0]
        device_folder_tom1 = glob.glob(base_dir + '28-0516b045b5ff')[0]
        device_file_tom0 = device_folder_tom0 + '/w1_slave'
        device_file_tom1 = device_folder_tom1 + '/w1_slave'


"""
print(temp.get_temperature())


"""
    ADC pins for the GPIO. 
    transistor_pin_0 = 26
    transistor_pin_1 = 16
    adc_channels are 1,0
"""

pins = GPIOPins((26, 16))
soil_one = SoilMoisture(2, 0, pins)
print(soil_one.read_values())
