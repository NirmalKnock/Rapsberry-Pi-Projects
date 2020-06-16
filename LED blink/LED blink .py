import Rpi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD) #Setup the mode
GPIO.setup(13,GPIO.OUT)

while True:
	GPIO.output(13,1)
	time.sleep(1000)
	GPIO.output(13,0)
	time.sleep(1000)
