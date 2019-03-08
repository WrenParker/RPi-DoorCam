from SendEmail import SendEmail
from DetectMotion import DetectMotion
from display import Display
import time

def run():
    # instantiates objects
    email = SendEmail()
    motionDetect = DetectMotion()
    display = Display()
    while True:
        motion = motionDetect.observeRoom()
        if motion == 1:
            email.sendEmail()
            display.sayHello()
            time.sleep(10*60) # sends an email ONLY every ten minutes.
            motion = 0
        else:
            motion = 0
            display.standBy()
