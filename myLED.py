import RPi.GPIO as GPIO
import time

menuFlashTime = 0.3
recordFlashTime = 1
delayTime = 1

class LED:
    
    def __init__(self, pinNumber):
        self.pinNumber = pinNumber

        GPIO.setup(pinNumber, GPIO.OUT)
        print "led on"

    def flash(count):
        for num in range(count):
            GPIO.ouput(self.pinNumber, GPIO.HIGH)
            delay(delayTimeHigh)
            GPIO.out(self.pinNumber,HPIO.LOW)
            delay(delayTimeLow)
            
        return

