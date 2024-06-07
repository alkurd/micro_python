import machine
import neopixel
import time

# Define constants for the NeoPixel matrix size
WIDTH = 16
HEIGHT = 16

# Define Colors
BLINKY_COLOR = (255, 0, 0)  # Red
PINKY_COLOR = (255, 0, 255)  # Pink
INKY_COLOR = (0, 255, 255)  # Cyan
CLYDE_COLOR = (255, 100, 0)  # Orange

# Define constant for Pac-Man color
PACMAN_COLOR = (255, 255, 0)  # Yellow
PACMAN_STARTX = 7
PACMAN_STARTY = 11

GHOST_STARTPOSITION = [(9, 6), (8, 6), (7, 6), (6, 6)]
GHOST_COLORS = [BLINKY_COLOR, PINKY_COLOR, INKY_COLOR, CLYDE_COLOR]

# Initialize the NeoPixel object
pin = machine.Pin(28)
np = neopixel.NeoPixel(pin, WIDTH * HEIGHT)

# Brightness factor
BRIGHTNESS = 0.02

# Function to scale color by brightness
def scale_color(color, factor):
    return tuple(int(c * factor) for c in color)

# Function to set a pixel in the matrix
def set_pixel(x, y, color):
    if 0 <= x < WIDTH and 0 <= y < HEIGHT:
        np[y * WIDTH + x] = scale_color(color, BRIGHTNESS)

# Function to create the Pac-Man maze
def create_maze():
    maze_pattern = [
        "1111111111111111",
        "1000000110000001",
        "1011110110111101",
        "1011110110111101",
        "1011000000001101",
        "1011011111101101",
        "1011000000001101",
        "1011011111101101",
        "0000000000000000",
        "1011011111101101",
        "1011011111101101",
        "1011000000001101",
        "1011110110111101",
        "1011110110111101",
        "1000000110000001",
        "1111111111111111",
    ]

    # Color definitions
    wall_color = (0, 0, 255)  # Blue
    path_color = (0, 0, 0)  # Black (off)

    for y in range(HEIGHT):
        for x in range(WIDTH):
            if maze_pattern[y][x] == '1':
                set_pixel(x, y, wall_color)
            else:
                set_pixel(x, y, path_color)

# Function to erase Pac-Man from its current position
def erase_pacman(x, y):
    set_pixel(x, y, (0, 0, 0))  # Erase Pac-Man by setting its pixel to black

# Function to draw Pac-Man at a specific position
def draw_pacman(x, y):
    # Pac-Man's shape is represented as a circle with an open mouth on the right side
    for i in range(4, 12):
        for j in range(4, 12):
            distance = ((i - 8) ** 2 + (j - 8) ** 2) ** 0.5
            if distance <= 4 and not (3 <= i <= 6 and 6 <= j <= 9):
                # Pac-Man's shape is represented as a circle with an open mouth on the right side
                # We will only light up the LED at the center of Pac-Man's shape
                set_pixel(x, y, PACMAN_COLOR)

# Function to handle Pac-Man movement to the right
def move_right(x, y):
    erase_pacman(x, y)  # Erase Pac-Man from current position
    x = (x + 1) % WIDTH  # Move Pac-Man one step to the right
    draw_pacman(x, y)  # Draw Pac-Man at the new position
    return x, y

# Function to handle Pac-Man movement to the left
def move_left(x, y):
    erase_pacman(x, y)  # Erase Pac-Man from current position
    x = (x - 1) % WIDTH  # Move Pac-Man one step to the left
    draw_pacman(x, y)  # Draw Pac-Man at the new position
    return x, y

# Function to handle Pac-Man movement upwards
def move_up(x, y):
    erase_pacman(x, y)  # Erase Pac-Man from current position
    y = (y - 1) % HEIGHT  # Move Pac-Man one step upwards
    draw_pacman(x, y)  # Draw Pac-Man at the new position
    return x, y

# Function to handle Pac-Man movement downwards
def move_down(x, y):
    erase_pacman(x, y)  # Erase Pac-Man from current position
    y = (y + 1) % HEIGHT  # Move Pac-Man one step downwards
    draw_pacman(x, y)  # Draw Pac-Man at the new position
    return x, y

# Function to draw colored ghost pixels
def draw_ghosts():
    for i, (x, y) in enumerate(GHOST_STARTPOSITION):
        set_pixel(x, y, GHOST_COLORS[i])

# Create the maze and write to the NeoPixel matrix
create_maze()
# Draw Pac-Man at a specific position (for example, (2, 2))
draw_pacman(PACMAN_STARTX, PACMAN_STARTY)
# Draw colored ghosts
draw_ghosts()
np.write()

# Function to handle user input for Pac-Man movement
def handle_input(x, y):
    while True:
        # Check for user input
        if machine.Pin(10).value() == 0:  # 'A' key pressed
            x, y = move_left(x, y)
            np.write()
            time.sleep(0.2)  # Delay to prevent rapid movement
        elif machine.Pin(9).value() == 0:  # 'D' key pressed
            x, y = move_right(x, y)
            np.write()
            time.sleep(0.2)  # Delay to prevent rapid movement
        elif machine.Pin(11).value() == 0:  # 'W' key pressed
            x, y = move_up(x, y)
            np.write()
            time.sleep(0.2)  # Delay to prevent rapid movement
        elif machine.Pin(12).value() == 0:  # 'S' key pressed
            x, y = move_down(x, y)
            np.write()
            time.sleep(0.2)  # Delay to prevent rapid movement

# Start handling user input for Pac-Man movement
handle_input(PACMAN_STARTX, PACMAN_STARTY)

