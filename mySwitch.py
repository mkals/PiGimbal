import RPi.GPIO as GPIO

class Switch:

    def __init__(self, pinNumber): 
        self.pinNumber = pinNumber
        GPIO.setup(pinNo, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
    def activated():
    
        count = 0
        if lastPressed == False:
            while GPIO.input(self.pinNumber):
                self.lastPressed = true
                count = count + 1
                if count > 100: 
                    print "long press switch"
                    return (True, True)

            if count != 0: 
                print "short press"
                return (True, False)

        self.lastPressed = false
        print "noPress"
        return (False, False)
    
