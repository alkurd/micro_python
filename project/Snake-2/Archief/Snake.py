import random
from pyMatrix import *
from time import sleep
import LETTERS 

 

COLOUR_BACKGROUND = (100, 100, 100)  # (R, G, B)
COLOUR_RED        = (255,   0,   0)
COLOUR_GREEN      = (  0, 255,   0)
COLOUR_BLUE       = (  0,   0, 255)
COLOUR_WHITE      = (255, 255, 255)
COLOUR_YELLOW     = (255, 255, 0)  
COLOURS = (COLOUR_RED, COLOUR_GREEN, COLOUR_BLUE, COLOUR_WHITE)

def getRandomPos(maxX, maxY, notX=-1, notY=-1):
    x = random.randint(0, maxX-1)
    y = random.randint(0, maxY-1)
    if x == notX or y == notY:
        return getRandomPos(maxX, maxY, notX, notY)
    return x, y
def draw_positions(word, start_x, start_y, color):
    positions = []
    x_offset = 0
    for character in word:
        if character == " ":  # Negeer spaties
            x_offset += 1  # Voeg extra ruimte toe tussen woorden
            continue
        m = LETTERS.getMatrix(character)
        for y, row in enumerate(m):
            for x, pixel in enumerate(row):
                if pixel == 1:
                    positions.append((start_x + x + x_offset , start_y + y, color))
        x_offset +=  len(m[0])+1
    return positions 



maxX, maxY = 63, 32
posX, posY = maxX // 2, maxY // 2
game = pyMatrix(maxX, maxY, colourBackground=COLOUR_BACKGROUND, fpspeed = 10)
objectX, objectY = getRandomPos(maxX, maxY, posX, posY)
moveX, moveY = (0, 0)
colour = COLOUR_GREEN
speed = 10
counter = 0
snake_positions = [(posX, posY)]
started = False
gameover = False



def change(keys: list, x, y, colour):
    
    
    
    if gameover == False:
        if ord("s") in keys:
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

  
 
while True:
    keys = game.getPressedKey()
    positions = draw_positions('welcome', 11, 1, COLOUR_GREEN)
    positions += draw_positions('to snake',10 ,7, COLOUR_WHITE)
    positions += draw_positions('press  any ',7 ,13, COLOUR_WHITE)
    positions += draw_positions('button to',8 ,20, COLOUR_WHITE)
    positions += draw_positions('start',17 ,26, COLOUR_WHITE)
    game.drawGame(positions)
    if keys == [27]:
        quit()
    if keys != []:
        break

while True:
    keys = game.getPressedKey()
    if keys != [] and started == False:
        started = True 
    moveX, moveY, colour = change(keys, moveX, moveY, colour)
    new_posX = posX + moveX
    new_posY = posY + moveY
    if (new_posX < 0 or new_posX >= maxX or 
        new_posY < 0 or new_posY >= maxY or 
        ((new_posX, new_posY) in snake_positions and started == True)):
            gameover = True
            positions = draw_positions('game  over', 7, 1, COLOUR_RED)
            positions += draw_positions('c',22 ,7, COLOUR_GREEN) + draw_positions('to',33 ,7, COLOUR_WHITE)
            positions += draw_positions('Restart ',12 ,13, COLOUR_WHITE)
            positions += draw_positions('q',22 ,20, COLOUR_RED) + draw_positions('to',33 ,20, COLOUR_WHITE)
            positions += draw_positions('quit',20 ,26, COLOUR_WHITE)
            if ord ('c') in keys:
                posX, posY = maxX // 2, maxY // 2
                objectX, objectY = getRandomPos(maxX, maxY, posX, posY)
                moveX, moveY = (0, 0)
                colour = COLOUR_GREEN
                counter = 0
                snake_positions = [(posX, posY)]
                started = False
                gameover = False
            elif keys == [27] or ord ('q') in keys:
                quit() 
    else:
        posX = new_posX
        posY = new_posY
        snake_positions = [(posX, posY)] + snake_positions[:-1]
        if objectX == posX and objectY == posY:
            objectX, objectY = getRandomPos(maxX, maxY, posX, posY)
            snake_positions.append((objectX, objectY))

        positions = [(objectX, objectY, COLOUR_RED)] + [(x, y, colour) for x, y in snake_positions]
    
    game.drawGame(positions)

                # positions = [(objectX, objectY, COLOUR_RED)] + [(x, y, colour) for x, y in snake_positions]
# print(draw_positions('p',14 ,1, COLOUR_WHITE))
# exit()

# while True:
#     keys = game.getPressedKey()
#     moveX, moveY, colour = change(keys, moveX, moveY, colour)

#     if counter % speed == 0:
#         new_posX = posX + moveX
#         new_posY = posY + moveY

#         if (new_posX < 0 or new_posX >= maxX or 
#             new_posY < 0 or new_posY >= maxY or 
#             (new_posX, new_posY) in snake_positions):
#             game_over_positions = draw_positions('GAMEOVER', 1, 1, COLOUR_WHITE)
#             game_over_positions = draw_positions('PRESS C', 14, 1, COLOUR_WHITE, game_over_positions)
#             game.drawGame(game_over_positions)
#             while True:
#                 keys = game.getPressedKey()
#                 if ord('c') in keys:
#                     # Reset game
#                     posX, posY = maxX // 2, maxY // 2
#                     objectX, objectY = getRandomPos(maxX, maxY, posX, posY)
#                     moveX, moveY = (1, 0)
#                     colour = COLOUR_GREEN
#                     counter = 0
#                     snake_positions = [(posX, posY)]
#                     break
#                 elif keys == [27]:
#                     quit()
#             continue

#         posX = new_posX
#         posY = new_posY
#         snake_positions = [(posX, posY)] + snake_positions[:-1]

#     if objectX == posX and objectY == posY:
#         objectX, objectY = getRandomPos(maxX, maxY, posX, posY)
#         snake_positions.append((objectX, objectY))

#     positions = [(objectX, objectY, COLOUR_RED)] + [(x, y, colour) for x, y in snake_positions]
    
#     game.drawGame(positions)

#     counter += 1