import RPi.GPIO as GPIO
# import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)

while True:
    # == code ==