from SendEmail import SendEmail

def run():
    email = SendEmail()
    motionDetect = DetectMotion()
    while True:
        motion = DetectMotion.observeRoom()
        if motion == 1:
            SendEmail.sendEmail()
