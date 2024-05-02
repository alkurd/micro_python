import random
from pyMatrix import *

COLOUR_BACKGROUND = (100, 100, 100)  # (R, G, B)
COLOUR_RED        = (255,   0,   0)
COLOUR_GREEN      = (  0, 255,   0)
COLOUR_BLUE       = (  0,   0, 255)
COLOUR_WHITE      = (255, 255, 255)
COLOURS = (COLOUR_RED, COLOUR_GREEN,COLOUR_BLUE, COLOUR_WHITE )

def getRandomPos(maxX, maxY, notX = -1, notY = -1):
    x = random.randint(0,maxX)
    y = random.randint(0,maxY)
    if x == notX or y == notY:
        return getRandomPos(maxX, maxY, notX, notY)
    return x,y

game = pyMatrix(32,16, colourBackground = COLOUR_BACKGROUND)
maxX, maxY  = game.getWidthHeight()
objectX, objectY = getRandomPos(maxX, maxY) 
posX = maxX // 2
posY = maxY // 2
moveX, moveY = (1,0)
colour = COLOUR_GREEN
speed = 5
counter = 0
while True:
    keys = game.getPressedKey()
    if pygame.K_s in keys:
        moveX, moveY = ( 0,  1)
    elif pygame.K_w in keys:
        moveX, moveY = ( 0, -1)
    elif pygame.K_a in keys:
        moveX, moveY = (-1,  0)
    elif pygame.K_d in keys:
        moveX, moveY = ( 1,  0)

    elif pygame.K_DOWN in keys:
        moveX, moveY = ( 0,  1)
    elif pygame.K_UP in keys:
        moveX, moveY = ( 0, -1)
    elif pygame.K_LEFT in keys:
        moveX, moveY = (-1,  0)
    elif pygame.K_RIGHT in keys:
        moveX, moveY = ( 1,  0)

    elif pygame.K_ESCAPE in keys:
        pygame.quit()

    if True: #counter % speed == 0:
        if game.isPosAllowed(posX + moveX, posY + moveY):
            posX += moveX
            posY += moveY
    if objectX == posX and  objectY == posY:
        objectX, objectY = getRandomPos(maxX, maxY, posX, posY)
        
    positions =[(objectX, objectY, COLOUR_RED), (posX, posY, colour)]
    
    
    game.drawGame (positions)

    if game.quit():
        quit()

    counter += 1