try:
    from picamera import PiCamera
    camera = PiCamera()    
except ImportError:
    camera = None


def take():
    if camera: 
        camera.capture('./image.jpg')
        return 'image.jpg'
    else:
        return 'sponge.jpg'

