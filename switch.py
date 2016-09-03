import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    inputState = GPIO.input(18)
    if inputState == False:
        print("Button pressed")
        time.sleep(.2)
