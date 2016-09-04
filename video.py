from picamera import PiCamera
import os

class VideoCapture: 
            
    cam = Camera()
    disp = Display()

    directory = '/home/video'
    name = 'videoFile'
    
    def __init__(self):
        self.camera = PiCamera()
        if not os.path.exists(directory):
            os.makedirs(directory)

    def startRecording():
        filePath = nextFilePath()
        self.camera.start_recording(filePath)

    def stopRecording():
        camera.stop_recording()
        
    def nextFilePath():
        i = 0
        while os.path.exists(filenameWithNumber(i)):
            i += 1
        return filenameWithNumber(i)

    def filenameWithNumber(i):
        return directory + name + str(i) + '.h264'

