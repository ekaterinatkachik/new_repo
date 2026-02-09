import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
leds = [16,12,25,17,27,23,22,24]
GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds,0)
GPIO.setup(9, GPIO.IN)
GPIO.setup(10, GPIO.IN)
num = 0
def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]
sleep_time = 0.2
while True:
    if GPIO.input(9) and GPIO.input(10):
        num = 255
        print(num, dec2bin(num))
        time.sleep(sleep_time)
        continue
    if GPIO.input(9):
        num+=1
        print(num, dec2bin(num))
        time.sleep(sleep_time)
    if GPIO.input(10):
        num-=1
        print(num, dec2bin(num))
        time.sleep(sleep_time)
    if num<1:
        num = 1
    if num>256:
        num = 256
    GPIO.output(leds, dec2bin(num))