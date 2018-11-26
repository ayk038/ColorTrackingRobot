import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (240,144)
    camera.start_recording('my_video.h264')
    camera.wait_recording(60)
    camera.stop_recording()

