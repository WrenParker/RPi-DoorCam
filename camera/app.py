from SendEmail import SendEmail
import time

def run():
    email = SendEmail()
    motionDetect = DetectMotion()
    while True:
        motion = DetectMotion.observeRoom()
        if motion == 1:
            SendEmail.sendEmail()
            time.sleep(5)
            motion = 0
