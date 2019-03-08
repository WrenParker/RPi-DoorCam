from SendEmail import SendEmail
from DetectMotion import DetectMotion
from display import Display
import time

def run():
    email = SendEmail()
    motionDetect = DetectMotion()
    display = Display()
    while True:
        motion = motionDetect.observeRoom()
        if motion == 0:
            email.sendEmail()
            display.sayHello()
            time.sleep(3)
            motion = 0
        else:
            motion = 1
            display.standBy()
