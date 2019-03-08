import Adafruit_CharLCD as LCD

class Display:

    def __init__(self):
        self.rs = 25
        self.en = 24
        self.d4 = 23
        self.d5 = 17
        self.d6 = 18
        self.d7 = 22
        self.backLight = 4
        self.columns = 16
        self.rows = 2
        self.lcd = LCD.Adafruit_CharLCD(self.rs, self.en, self.d4, self.d5, self.d6, self.d7, self.backLight, self.columns, self.rows)

    def sayHello(self):
        lcd.home()
        lcd.message("ENEMY SPOTTED\n")
        lcd.message("Hello There!")

    def standBy(self):
        lcd.home()
        lcd.message("All Clear!")

test = Display()
test.sayHello()
