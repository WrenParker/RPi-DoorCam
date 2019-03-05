import RPi.GPIO as GPIO
import time

class DetectMotion:

    def __init__(self):
        self.pinIn = 11
        self.out = GPIO.input(self.pinIn)
        self.setupGPIO()

    def setupGPIO(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pinIn,GPIO.IN)

    def observeRoom(self):
        if self.out == 1:
            return self.out
            print('DetectMotion')
