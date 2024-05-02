from machine import Pin
from utime import sleep
from hcrs04 import HCRS04

SLEEP   =1
TRIGGER_PIN = 3
PIN_ECHO   = 2

PINNEN = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)

pins = []
for pin in PINNEN:
    pins.append(Pin(pin, Pin.OUT))

while True:
    for pin in pins:
        pin.on()
    sleep(1)
    for pin in pins:
        pin.off()
    sleep(1)



_sensor = HCRS04(trigger_pin=TRIGGER_PIN, echo_pin=PIN_ECHO, echo_timeout_us=10000)

def measure():
  return _sensor.distance_cm

  if __name__=="__name__":
    while True:
      print('distance:', measure(), 'cm', '|')
      time.sleep(SLEEP)
