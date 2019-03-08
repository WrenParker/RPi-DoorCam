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
        if motion == 1:
            #email.sendEmail()
            display.sayHello()
            time.sleep(1)
            motion = 0
        else:
            motion = 0
            display.standBy()
