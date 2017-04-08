import  RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.IN,pull_up_down=GPIO.PUD_UP)


while True:
    inputValue = GPIO.input(12)
    if (inputValue == False):
        print("Button press ")
    time.sleep(1)