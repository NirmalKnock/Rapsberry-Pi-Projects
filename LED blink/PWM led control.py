import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.OUT)
while True:
	pwm_obj=GPIO.PWM(8,400)
	pwm_obj.start(100) 
	time.sleep(1)
	pwm_obj.ChangeDutyCycle(20)
	time.sleep(3)
	pwm_obj.ChangeDutyCycle(5)
	time.sleep(3)
	pwm_obj.ChangeDutyCycle(30)
	time.sleep(3)
	pwm_obj.ChangeDutyCycle(80)
	time.sleep(4)

