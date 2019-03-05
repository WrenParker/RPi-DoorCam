from SendEmail import SendEmail
from DetectMotion import DetectMotion
import time

def run():
    email = SendEmail()
    motionDetect = DetectMotion()
    while True:
        motion = motionDetect.observeRoom()
        if motion == 1:
            email.sendEmail()
            time.sleep(60*15)
            motion = 0
