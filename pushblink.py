import  RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)


while True:
    inputValue = GPIO.input(12)
    if (inputValue == False):
        GPIO.output(11, True)
        time.sleep(1)
        GPIO.output(11, False)
        time.sleep(1)
        print("Button press ")
    time.sleep(0.3)