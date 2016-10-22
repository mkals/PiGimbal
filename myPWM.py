import RPi.GPIO as GPIO

class Pwm:
    frequency = 50

    def __init__(self, pinNumber):

        GPIO.setup(7, GPIO.OUT)
        self.p = GPIO.PWM(pinNumber, frequency)
        self.p.start(0)

    def move(value):
        self.p.ChangeDutyCycle(i)
        
