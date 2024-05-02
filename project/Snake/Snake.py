import random
from pyMatrix import *
from time import sleep
from LETTERS import LETTERS

COLOUR_BACKGROUND = (100, 100, 100)  # (R, G, B)
COLOUR_RED        = (255,   0,   0)
COLOUR_GREEN      = (  0, 255,   0)
COLOUR_BLUE       = (  0,   0, 255)
COLOUR_WHITE      = (255, 255, 255)
COLOURS = (COLOUR_RED, COLOUR_GREEN, COLOUR_BLUE, COLOUR_WHITE)

def getRandomPos(maxX, maxY, notX=-1, notY=-1):
    x = random.randint(0, maxX)
    y = random.randint(0, maxY)
    if x == notX or y == notY:
        return getRandomPos(maxX, maxY, notX, notY)
    return x, y



maxX, maxY = 32, 16
posX, posY = maxX // 2, maxY // 2
game = pyMatrix(maxX, maxY, colourBackground=COLOUR_BACKGROUND)
objectX, objectY = getRandomPos(maxX, maxY, posX, posY)
moveX, moveY = (1, 0)
colour = COLOUR_GREEN
speed = 10
counter = 0
snake_positions = [(posX, posY)]

def change(keys: list, x, y, colour):
    if ord("q") in keys:
        colour = random.choice(COLOURS)
    elif ord("s") in keys:
        x, y = (0, 1)
    elif ord("w") in keys:
        x, y = (0, -1)
    elif ord("a") in keys:
        x, y = (-1, 0)
    elif ord("d") in keys:
        x, y = (1, 0)
    elif keys == [1073741904]:  # Links
        x, y = (-1, 0)
    elif keys == [1073741903]:  # Rechts
        x, y = (1, 0)
    elif keys == [1073741906]:  # Omhoog
        x, y = (0, -1)
    elif keys == [1073741905]:  # Omlaag
        x, y = (0, 1)
    elif keys == [27]:
        quit()
    return x, y, colour

def draw_positions(word, start_x, start_y, color,positions=[]):
    x_offset = 0
    for character in word:
        # if character == " ":  # Behandel spaties apart
        #     x_offset += 1  # Voeg extra ruimte toe tussen woorden
        #     continue
        for y, row in enumerate(LETTERS[character]):
            for x, pixel in enumerate(row):
                if pixel == 1:
                    positions.append((start_x + x + x_offset, start_y + y, color))
        x_offset += len(LETTERS[character][0]) + 1  # Voeg een spatie toe tussen de letters
    return positions
    
while True:
        keys = game.getPressedKey()
        moveX, moveY, colour = change(keys, moveX, moveY, colour)

        if counter % speed == 0:
            new_posX = posX + moveX
            new_posY = posY + moveY

            if (new_posX < 0 or new_posX >= maxX or 
                new_posY < 0 or new_posY >= maxY or 
                (new_posX, new_posY) in snake_positions):

                
                if keys == [27]:
                    quit()
                
                

            posX = new_posX
            posY = new_posY
            snake_positions = [(posX, posY)] + snake_positions[:-1]
            # print(snake_positions)
        if objectX == posX and objectY == posY:
            objectX, objectY = getRandomPos(maxX, maxY, posX, posY)
            snake_positions.append((objectX, objectY))
        if moveX == 0 and moveY == 0:
            positions = [(25,25,COLOUR_WHITE), (25,26,COLOUR_BLUE)]
        else:
            positions = [(objectX, objectY, COLOUR_RED)] + [(x, y, colour) for x, y in snake_positions]
        game.drawGame(positions)

        counter += 1
