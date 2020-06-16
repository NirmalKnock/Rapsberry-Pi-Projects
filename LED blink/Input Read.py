import RPi.GPIO as GPIO

GPIO.setup(13,IN)

value=GPIO.input(13)
