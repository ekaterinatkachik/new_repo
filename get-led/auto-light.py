import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
state = 0
botton = 26
GPIO.setup(botton, GPIO.OUT)
tran = 6
GPIO.setup(tran, GPIO.IN)
while True:
    GPIO.output(botton, not GPIO.input(tran))

