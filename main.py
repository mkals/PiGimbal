from enum import Enum

class Mode(Enum):
    video = 0
    image = 1
    timelapse = 2
    faceTracking = 3
    objectTracking = 4


from RPi import GPIO

from myCamera import Camera
from mySwitch import Switch
from myPWM import PWM
from myLED import LED

GPIO.setmode(GPIO.BCM)


camera = Camera()
recordSwitch = Switch(12)
menuSwitch = Switch(14)
led = LED(14)

recording = False
mode = Mode.video

while True:
    
    if not recording and menuSwitch.activated():
        if mode == Mode.video:
            mode = Mode.image
        elif mode == Mode.image:
            mode = Mode.timelapse
        elif mode == Mode.timelapse:
            mode = Mode.faceTracking
        elif mode == Mode.faceTracking:
           mode = Mode.objectTracking
        else:
            mode = Mode.video

    if recordSwitch.activated():

        if mode == Mode.video:
            if recording:
                camera.stopRecording()
                recording = False
            else:
                camera.startRecording()
                recording = True

        elif mode == Mode.image():
            camera.takePhoto()

        elif mode == Mode.timelapse:
            if recording:
                camera.stopTimelapse()
                recording = False
            else:
                camera.startTimelapse()
                recording = True

        elif mode == Mode.faceTracking:
            if recording:
                recording = False
            else:
                recording = True

        elif mode == Mode.objectTracking:
            if recording:
                recording = False
            else:
                recording = True
            
    

#GPIO.cleanup.....
