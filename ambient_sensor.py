from Adafruit_BME280 import *

sensor = BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8, h_mode=BME280_OSAMPLE_8)

degrees = sensor.read_temperature()
pascals = sensor.read_pressure()
hectopascals = pascals / 100
humidity = sensor.read_humidity()
def get_temp():
    '''returns the temp in celius'''
    f_degrees = degrees * 9.0 / 5.0 + 32.0
    return (round(f_degrees, 3)) #convert to freedom units

def get_pressure():
    '''returns the hectopascals (current pressure reading)'''
    return (round(hectopascals, 3))

def get_humidity():
    '''returns the current humidity reading'''
    return (round(humidity, 3))


#print ('Pressure  = {0:0.2f} hPa'.format(hectopascals))
#print ('Humidity  = {0:0.2f} %'.format(humidity))
