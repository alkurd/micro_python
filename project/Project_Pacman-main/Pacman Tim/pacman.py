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

# Maze pattern global variable
maze_pattern = []

# Function to scale color by brightness
def scale_color(color, factor):
    return tuple(int(c * factor) for c in color)

# Function to set a pixel in the matrix
def set_pixel(x, y, color):
    if 0 <= x < WIDTH and 0 <= y < HEIGHT:
        np[y * WIDTH + x] = scale_color(color, BRIGHTNESS)

# Function to create the Pac-Man maze
def create_maze():
    global maze_pattern
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

# Function to check for collision with walls
def check_collision(x, y):
    return maze_pattern[y][x] == '1'

# Function to erase Pac-Man from its current position
def erase_pacman(x, y):
    set_pixel(x, y, (0, 0, 0))  # Erase Pac-Man by setting its pixel to black

# Function to draw Pac-Man at a specific position
def draw_pacman(x, y):
    set_pixel(x, y, PACMAN_COLOR)

# Function to draw colored ghost pixels
def draw_ghosts():
    for i, (x, y) in enumerate(GHOST_STARTPOSITION):
        set_pixel(x, y, GHOST_COLORS[i])

# Create the maze and write to the NeoPixel matrix
create_maze()
# Draw Pac-Man at the starting position
draw_pacman(PACMAN_STARTX, PACMAN_STARTY)
# Draw colored ghosts
draw_ghosts()
np.write()

