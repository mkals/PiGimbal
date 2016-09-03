from SimpleCV import Camera

cam = Camera()
disp = Display()


img = cam.getImage()
if disp.mouseLeft:
    break
img.save(disp)
    

