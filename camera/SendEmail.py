import smtplib, ssl

class SendEmail:

    def __init__(self):
        self.port = 465
        self.email = 'wrenparkercamera@gmail.com'
        self.password = 'Wi2JbAVS'
        self.context = ssl.create_default_context()
        self.message = "Enemy Spotted"

    def sendEmail(self):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(self.email, self.password)
        server.sendmail(self.email, "3048862808@mms.cricketwireless.net", self.message)
