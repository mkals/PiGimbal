from enum import Enum

class Mode(Enum):
    video = 0
    image = 1
    timelapse = 2
    faceTracking = 3
    objectTracking = 4


from RPi import GPIO

from video import VideoCapture
from switch import Switch
from pwm import Pwm
from led import Led

GPIO.setmode......

video = VideoCapture()
recordSwitch = Switch(12)
menuSwitch = Switch(14)
led = Led(14)

recording = False
mode = Mode.video

while True
    
    if menuSwitch.activated():


    if recordSwitch.activated():
        
    

GPIO.cleanup.....
