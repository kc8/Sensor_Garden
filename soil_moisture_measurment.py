import RPi.GPIO as GPIO
import Adafruit_ADS1x15
import time

def get_values(num_times_to_read, pin):
    '''reads pin 0 from ADC and returns the average of that amount'''
    list = 0
    GAIN = 1
    transistor_pin_0 = 26
    transistor_pin_1 = 16
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(transistor_pin_0, GPIO.OUT)
    GPIO.setup(transistor_pin_1, GPIO.OUT)
    adc = Adafruit_ADS1x15.ADS1015()

    try:
        GPIO.output(transistor_pin_0, 1)
        GPIO.output(transistor_pin_1, 1)
        for i in range(num_times_to_read):
            list += adc.read_adc(pin, gain=GAIN)
    except KeyboardInterrupt:
        GPIO.output(transistor_pin_0, 0)
        GPIO.output(transistor_pin_1, 0)
        GPIO.cleanup()
    GPIO.output(transistor_pin_0, 0)
    GPIO.output(transistor_pin_1, 0)
    GPIO.cleanup()

    return list/num_times_to_read
