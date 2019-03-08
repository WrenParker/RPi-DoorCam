import RPi.GPIO as GPIO
import time

class DetectMotion:

    def __init__(self):
        self.pinIn = 11
        self.setupGPIO()

    def setupGPIO(self):
        GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.pinIn, GPIO.IN)

    def observeRoom(self):
        input = GPIO.input(self.pinIn)
        if input == 0:
            print('Enemy Spotted')
            return input
