import neopixel
import machine
import time

# Configure the NeoPixel LED strip
NUM_LEDS = 8  # Number of NeoPixels
PIN = 0       # GPIO pin connected to the NeoPixels
np = neopixel.NeoPixel(machine.Pin(PIN), NUM_LEDS)

# Define colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Main loop
while True:
    # Turn on all pixels to red
    for i in range(NUM_LEDS):
        np[i] = RED
    np.write()
    time.sleep(1)

    # Turn on all pixels to green
    for i in range(NUM_LEDS):
        np[i] = GREEN
    np.write()
    time.sleep(1)

    # Turn on all pixels to blue
    for i in range(NUM_LEDS):
        np[i] = BLUE
    np.write()
    time.sleep(1)
