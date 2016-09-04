import RPi.GPIO as GPIO
import time
from sets import Set

class Switch:

    def __init__(self, pinNumber): 
        self.pinNumber = pinNumber
        GPIO.setup(pinNo, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
    def activated():
        inputState = GPIO.input(self.pinNumber)

        if inputState == False:
            if buttonLastPressed == False:
                self.buttonLastPressed = True
                return True
        
        buttonLastPressed = False
        return False
    
