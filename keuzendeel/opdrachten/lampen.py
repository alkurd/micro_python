from machine import Pin
from time import sleep

led3 = Pin(3,Pin.OUT)
led4 = Pin(4,Pin.OUT)

while True:
    led3.on()
    sleep(1)
    led4.on()
    led3.off()
    sleep(1)
