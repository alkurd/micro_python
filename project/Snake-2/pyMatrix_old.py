"""
    about : pyMatris is a pyGame matrix of n x m pixels
            This matrix is created to silumate Neopixel matrix boards
            for development in python so the code can be ported to micropython
            with these neopixel matrixes
    Version : 0.02
    Date    : 27 februari 2024
"""
import pygame
import pygame.sysfont as sysfont
import random
from pyMatrix import *
from time import sleep

"""
    Matrix with dymantions width, heigt to simulate a Neopixel display
    This version uses X, Y position, a neopixel matrix works with an index number.
"""
class pyMatrix():
    _oldPositions = set()
    LINE_WIDTH 	  = 3
    MAX_PIXELS	  = 1200
    
    """
        init function of the class
    """
    def __init__(self, width = 32, height = 16, colourBackground = (100, 100, 100), caption = 'Neopixel matrix'):
        #print(sysfont.get_fonts()[0])
        #self.font = pygame.font.SysFont(sysfont.get_fonts()[0], 25)
        self._maxX = width
        self._maxY = height
        self._colourBackground = colourBackground
        self._squareSize       = min((self.MAX_PIXELS / self._maxX) - self.LINE_WIDTH * ((self.MAX_PIXELS + 1) / self.MAX_PIXELS),
                                     (self.MAX_PIXELS / self._maxY) - self.LINE_WIDTH * ((self.MAX_PIXELS + 1) / self.MAX_PIXELS))
        self._resolution 	  = ((self._squareSize + self.LINE_WIDTH) * self._maxX, (self._squareSize + self.LINE_WIDTH) * self._maxY)
        self._screen = pygame.display.set_mode(self._resolution)
        self._clock = pygame.time.Clock()  # to set max FPS
        pygame.display.set_caption(caption)
        self._drawScreen()
    
    """
        Return the NeoPixel index according to XY coordinates
    """
    def getIndex(self, posX, posY):
        if posX % 2 == 0:
            return posY + self._maxY * posX
        return self._maxY * (posX + 1) -1 - posY
    
    
    """
        Return the NeoPixel index according to XY coordinates
    """
    def getXY(self, index):
        x = index // self._maxY
        y = index % self._maxY
        if x % 2 == 1:
            y = self._maxY - y - 1
        return x, y
    
    def showNeoPixelIndex(self):
        for y in range(self._maxY):
            for x in range(self._maxX):
                x, y = self._getPixelPos(posX, posY)
                geometry = (x, y, self._squareSize, self._squareSize)
                index = self.getIndex(x,y)
                self._screen.blit(self.font.render(str(index), True, (255,255,255)), (200, 100))
                pygame.display.update()

    """
        return the width and height (in positions)  of the matrix
    """
    def getWidthHeight(self):
        return self._maxX, self._maxY
    
    """
        True if the PosX, posY is within the boundries of the matrix
    """
    def isPosAllowed(self, posX, posY):
        if posX < 0 or posY < 0:
            return False
        if posX >= self._maxX:
            return False
        if posY >= self._maxY:
            return False
        return True
    
    
    """
        position is a list of (row, col, color)
        if color is None, the background color is reset.
    """
    def drawGame(self, positions : list, colour = None):
        newCoordinates = set((p[0],p[1]) for p in positions )
        # reset pixels that are no longer used
        for xy in self._oldPositions:
            if xy not in newCoordinates:
                pygame.display.update(self._draw_square(xy[0], xy[1], self._colourBackground) )
                 
        for x,y,c in positions:
            if colour != None:
                c = colour     
            pygame.display.update(self._draw_square(x, y, c))
        self._oldPositions = newCoordinates


    
    """
        Check if quit event was raisen, if so quit the pyGame,
        You should end the program (quit()) 
    """
    def quit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return True
        return False
    
    """
        Get the raisen events
    """
    def getEvents(self):
        self._clock.tick(60)  # max FPS = 60
        return pygame.event.get()
    
    """
        return the keys pressedc (ascii value)
    """
    def getPressedKey(self):
        keys = []
        for event in self.getEvents():
            if event.type == pygame.KEYDOWN:
                keys.append(event.key)
        return keys
          
    """ ----------------------- Private functions ------------------------- """
    
    """
        from the postion posX, posY calculate and return the position in pixels.
    """
    def _getPixelPos(self, posX, posY):
        return self.LINE_WIDTH * (posX + 1) + self._squareSize * posX, self.LINE_WIDTH * (posY + 1) + self._squareSize * posY

    """
        Draw a square on the PosX, PosY location with a given colod
    """
    def _draw_square(self, posX, posY, colour = None):
        if colour == None:
            colour = self._colourBackground
        x, y = self._getPixelPos(posX, posY)
        geometry = (x, y, self._squareSize, self._squareSize)
        pygame.draw.rect(self._screen, colour, geometry)
        return geometry
    
    
    """
        Dwaw all the squares on the screen
    """
    def _draw_squares(self):
        for y in range(self._maxY):
            for x in range(self._maxX):
                self._draw_square(x, y)            
    
    
    """
        Redraw the complete screen
    """
    def _drawScreen(self):
        self._screen.fill((0, 0, 0))  # Fill screen with black color.
        self._draw_squares()
        pygame.display.flip()  # Update the screen.

        
if __name__ == "__main__":  

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
        elif keys == [27]:
            quit()
        return x, y, colour
            
        
    while True:
            keys = game.getPressedKey()
            moveX, moveY, colour = change(keys, moveX, moveY, colour)

            if counter % speed == 0:
                new_posX = posX + moveX
                new_posY = posY + moveY

                if (new_posX < 0 or new_posX >= maxX or 
                    new_posY < 0 or new_posY >= maxY or 
                    (new_posX, new_posY) in snake_positions):
                    quit()
                    
                    

                posX = new_posX
                posY = new_posY
                snake_positions = [(posX, posY)] + snake_positions[:-1]
                # print(snake_positions)
            if objectX == posX and objectY == posY:
                objectX, objectY = getRandomPos(maxX, maxY, posX, posY)
                snake_positions.append((objectX, objectY))

            positions = [(objectX, objectY, COLOUR_RED)] + [(x, y, colour) for x, y in snake_positions]
            game.drawGame(positions)

            counter += 1
    
    #test Index
    if False:
        game = pyMatrix()
        maxX, maxY= game.getWidthHeight()
        for x in range(maxX):
            for y in range(maxY):
                index = game.getIndex(x,y)
                calcX, calcY = game.getXY(index)
                print(f"{x:2}, {y:2}, {index:3}, {calcX:3}, {calcY:3}, {calcX - x == 0}, {calcY - y == 0}")
            
