# This script is for continuous video capture
# In addition it uses opencv to transform
# the video frams to HSV and displays the video stream
import RPi.GPIO as GPIO
from motorA import *
from sonarA import * 
import cv2
import cv2.cv
import picamera
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import numpy as np

def nothing(x):
    pass
# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

# allow the camera to warmup
time.sleep(0.1)

h, s, v = 0, 180,166
img_low = np.zeros((15,512,3),np.uint8)

def countPix(img):
    lefthalf = img[0:480,0:320]
    righthalf = img[0:480,320:640]
    cv2.imshow('result',lefthalf)
    cv2.imshow('result1',righthalf)
    numWhite1=cv2.countNonZero(lefthalf)
    numWhite2=cv2.countNonZero(righthalf)
    print(str(numWhite1)+ "and" + str(numWhite2))
# capture frames from the camera
def takePic():
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        # grab the raw NumPy array representing the image, then initialize the timestamp
        # and occupied/unoccupied text
        image = frame.array
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        cv2.imshow('result', img_low)

        img_low[:] = [h,s,v]
        # define the range of the blue color in hsv
        lower_green = np.array([h,s,v])
        upper_green = np.array([255, 255, 255])

        # Threshold the hsv image to get only blue colors
        mask = cv2.inRange(hsv, lower_green, upper_green)

        #Bitwise AND mask and original image
        res = cv2.bitwise_and(image, image, mask = mask)
        
        numpix=countPix(mask)
        
        # show the frame
        cv2.imshow("Frame", image)
        cv2.imshow("Mask", mask)
        cv2.imshow("Res", res)

        key = cv2.waitKey(1) & 0xFF

        # clear the stream in preparation for the next frame
        rawCapture.truncate(0)

        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
            cv2.destroyAllWindows()
            break

takePic()

try:
	setupSonar(sonarPin = 8)
	while True:
	   dist = getDistance()
	   if dist < 15:
	      reverse(50)
	   elif dist > 30:
	      forward(50)
	   elif dist >=15 and dist <=30:
	      stopall()
	   elif numWhite1 > numWhite2:
	      turn(rspeed=50,lspeed=0)
	   elif numWhite2 > numWhite1:
	      turn(rspeed=0,lspeed=50)
	   print dist
except KeyboardInterrupt:
       GPIO.cleanup()
