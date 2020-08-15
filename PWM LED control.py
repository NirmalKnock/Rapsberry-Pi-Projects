  
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.OUT)
while True:
	pwm_obj=GPIO.PWM(8,400)
	pwm_obj.start(100)
	for i in range(0,101):
		pwm_obj.ChangeDutyCycle(i)
		print(i)
		time.sleep(0.05)
	for i in range(100,0,-1):
		pwm_obj.ChangeDutyCycle(i)
		print(i)
		time.sleep(0.1)	
