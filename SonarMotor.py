
##Sonar linked to movement/motor function
#SonarMotor

import RPi.GPIO as GPIO, time
import picamera
from motorA import *
from sonarA import *

try:
      setupSonar(sonarPin=8)
      while True:
         dist = getDistance()
	 if dist < 15:
	    reverse(50)
	 elif dist >30:
	    forward(50)
	 elif dist >=15 and dist <=30:
	    stopall()
         print dist

except KeyboardInterrupt:
       GPIO.cleanup()
