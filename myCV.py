from SimpleCV import Camera

class CV:

    cam = Camera()
    disp = Display()

    def trackObject():
        img = cam.getImage()
        img.save(disp)
            

