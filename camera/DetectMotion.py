import RPi.GPIO as GPIO
import time

class DetectMotion:

    def __init__(self):
        self.pinIn = 11 # if GPIO was board, this would be 22
        self.setupGPIO()

    def setupGPIO(self):
        GPIO.cleanup()
        # sets GPIO to BCM to match the lcd library setup. Only changes the pinIn value
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        # set up only input, output is through the SendEmail, and display classes.
        GPIO.setup(self.pinIn, GPIO.IN)

    def observeRoom(self):
        input = GPIO.input(self.pinIn)
        # watches for input to change from 0 to 1
        if input == 1:
            print('Enemy Spotted')
            return input
