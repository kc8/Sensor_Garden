import RPi.GPIO as GPIO
import time

GPIO_RELAY_1 = 5 #14
GPIO_RELAY_2 = 6
WAIT = 15


def water(plant_num):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GPIO_RELAY_1, GPIO.OUT)
    GPIO.setup(GPIO_RELAY_2, GPIO.OUT)

    if(plant_num == 0):
        try:
            GPIO.output(GPIO_RELAY_2, 1)
            time.sleep(WAIT)
            GPIO.output(GPIO_RELAY_2, 0)
        except KeyboardInterrupt:
            GPIO.output(GPIO_RELAY_1, 0)
            GPIO.output(GPIO_RELAY_2, 0)
            GPIO.cleanup()
    elif(plant_num == 1):
        try:
            GPIO.output(GPIO_RELAY_1, 1)
            time.sleep(WAIT)
            GPIO.output(GPIO_RELAY_1, 0)
        except KeyboardInterrupt:
            GPIO.output(GPIO_RELAY_1, 0)
            GPIO.output(GPIO_RELAY_2, 0)
            GPIO.cleanup()
    else:
        GPIO.output(GPIO_RELAY_1, 0)
        GPIO.output(GPIO_RELAY_2, 0)
        GPIO.cleanup()


water(0)