import RPi.GPIO as GPIO
import time

class DetectMotion:

    def __init__(self):
        self.pinIn = 11
        self.setupGPIO()
        self.out = GPIO.input(self.pinIn)

    def setupGPIO(self):
        GPIO.setup(self.pinIn,GPIO.IN)
        GPIO.setmode(GPIO.BOARD)


    def observeRoom(self):
        if self.out == 1:
            print('DetectMotion')
            return self.out

test = DetectMotion()
test.observeRoom()
