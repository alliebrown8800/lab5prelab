# Basic code for DC motor control using manual PWM
# Set PWM period = 20 ms

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
pwmPin = 20
GPIO.setup(pwmPin, GPIO.OUT)

# set min & max % duty cycles
dcMin = 0
dcMax = 100

pwm = GPIO.PWM(pwmPin, 50) # PWM object at 50 Hz (20 ms period)
pwm.start(0)

try:
  for dc in range(dcMax,dcMin,-1):
    pwm.ChangeDutyCycle(dc)
    print(dc)
    time.sleep(.02)
except KeyboardInterrupt:
  print("closing")
GPIO.cleanup()