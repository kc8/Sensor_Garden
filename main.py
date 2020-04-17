from soil_temperatures import Temperature

temp = Temperature(device_file="28-0316b09095ff")

#device_file: str, device_folder: str,
"""        device_folder_tom0 = glob.glob(base_dir + '28-0316b09095ff')[0]
        device_folder_tom1 = glob.glob(base_dir + '28-0516b045b5ff')[0]
        device_file_tom0 = device_folder_tom0 + '/w1_slave'
        device_file_tom1 = device_folder_tom1 + '/w1_slave'


"""
print(temp.get_temperature())