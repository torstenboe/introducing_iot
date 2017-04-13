import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

led = GPIO.PWM(11, 100)
pwm.start(0)
pause = 0.1

for i in range(0, 100 + 1):
   led.ChangeDutyCycle(i)
   time.sleep(pause)

for i in range(100, -1, -1):
   led.ChangeDutyCycle(i)
   time.sleep(pause)

GPIO.cleanup()