from SendEmail import SendEmail
from DetectMotion import DetectMotion
import time

def run():
    email = SendEmail()
    motionDetect = DetectMotion()
    while True:
        motion = motionDetect.observeRoom()
        if motion == 1:
            SendEmail.sendEmail()
            time.sleep(5)
            motion = 0
