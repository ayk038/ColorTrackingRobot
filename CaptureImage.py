#streaming camera
#captures a streamed image

from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.start_preview()
while True:
	camera.capture("image.jpg")
sleep(10)

