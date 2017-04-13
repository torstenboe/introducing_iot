import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

pwm = GPIO.PWM(11, 50)
pwm.start(0)

foreach i in range(100):
   pwm.ChangeDutyCycle(i)
   time.sleep(0.1)
foreach i in range(100, 0, -1)
   pwm.ChangeDutyCycle(i)
   time.sleep(0.1)

GPIO.cleanup()