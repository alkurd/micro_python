import pygame

COLOUR_BACKGROUND = (100, 100, 100)  # (R, G, B)
COLOUR_RED        = (255,   0,   0)
COLOUR_GREEN      = (  0, 255,   0)
COLOUR_BLUE       = (  0,   0, 255)
COLOUR_WHITE      = (255, 255, 255)

class pyMatrix():
    _oldPositions = set()
    LINE_WIDTH    = 3
    MAX_PIXELS    = 1200
    
    def __init__(self, width=32, height=16, colourBackground=(100, 100, 100)):
        self._maxX = width
        self._maxY = height
        self._colourBackground = colourBackground
        self._squareSize = min((self.MAX_PIXELS / self._maxX) - self.LINE_WIDTH * ((self.MAX_PIXELS + 1) / self.MAX_PIXELS),
                               (self.MAX_PIXELS / self._maxY) - self.LINE_WIDTH * ((self.MAX_PIXELS + 1) / self.MAX_PIXELS))
        self._resolution = ((self._squareSize + self.LINE_WIDTH) * self._maxX, (self._squareSize + self.LINE_WIDTH) * self._maxY)
        self._screen = pygame.display.set_mode(self._resolution)
        pygame.display.set_caption('Neopixel matrix')
        self._drawScreen()
    
    def getIndex(self, posX, posY):
        if posX % 2 == 0:
            return posY + self._maxY * posX
        return self._maxY * (posX + 1) - 1 - posY
    
    def getXY(self, index):
        x = index // self._maxY
        y = index % self._maxY
        if x % 2 == 1:
            y = self._maxY - y - 1
        return x, y
    
    def getWidthHeight(self):
        return self._maxX, self._maxY
    
    def isPosAllowed(self, posX, posY):
        return 0 <= posX < self._maxX and 0 <= posY < self._maxY
    
    def drawGame(self, positions: list, colour=None):
        newCoordinates = set((p[0], p[1]) for p in positions)
        for xy in self._oldPositions - newCoordinates:
            self._draw_square(xy[0], xy[1], self._colourBackground)
        for x, y, c in positions:
            if colour is not None:
                c = colour     
            self._draw_square(x, y, c)
        self._oldPositions = newCoordinates
        pygame.display.update()
    
    def quit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return True
        return False
    
    def getPressedKey(self):
        keys = []
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                keys.append(event.key)
        return keys
          
    def _getPixelPos(self, posX, posY):
        return self.LINE_WIDTH * (posX + 1) + self._squareSize * posX, self.LINE_WIDTH * (posY + 1) + self._squareSize * posY

    def _draw_square(self, posX, posY, colour=None):
        if colour is None:
            colour = self._colourBackground
        x, y = self._getPixelPos(posX, posY)
        geometry = (x, y, self._squareSize, self._squareSize)
        pygame.draw.rect(self._screen, colour, geometry)
    
    def _draw_squares(self):
        for y in range(self._maxY):
            for x in range(self._maxX):
                self._draw_square(x, y)
    
    def _drawScreen(self):
        self._screen.fill((0, 0, 0))  
        self._draw_squares()
        pygame.display.flip()

if __name__ == "__main__":
    import random
    pygame.init()
    
    def getRandomPos(maxX, maxY, notX=-1, notY=-1):
        x = random.randint(0, maxX - 1)
        y = random.randint(0, maxY - 1)
        if x == notX or y == notY:
            return getRandomPos(maxX, maxY, notX, notY)
        return x, y
    
    game = pyMatrix(32, 16, colourBackground=COLOUR_BACKGROUND)
    maxX, maxY = game.getWidthHeight()
    objectX, objectY = getRandomPos(maxX, maxY) 
    posX = maxX // 2
    posY = maxY // 2
    moveX, moveY = (1, 0)
    colour = COLOUR_RED
    speed = 10
    counter = 0
    
    while not game.quit():
        keys = game.getPressedKey()
        if pygame.K_s in keys:
            moveX, moveY = (0, 1)
        elif pygame.K_w in keys:
            moveX, moveY = (0, -1)
        elif pygame.K_a in keys:
            moveX, moveY = (-1, 0)
        elif pygame.K_d in keys:
            moveX, moveY = (1, 0)
        elif pygame.K_DOWN in keys:
            moveX, moveY = (0, 1)
        elif pygame.K_UP in keys:
            moveX, moveY = (0, -1)
        elif pygame.K_LEFT in keys:
            moveX, moveY = (-1, 0)
        elif pygame.K_RIGHT in keys:
            moveX, moveY = (1, 0)
        elif pygame.K_ESCAPE in keys:
            pygame.quit()
        
        if counter % speed == 0:
            if game.isPosAllowed(posX + moveX, posY + moveY):
                posX += moveX
                posY += moveY
        if objectX == posX and  objectY == posY:
            objectX, objectY = getRandomPos(maxX, maxY, posX, posY)
        positions =[ (objectX, objectY, COLOUR_GREEN), (posX, posY, colour)]
        game.drawGame(positions)
        
        counter += 1

pygame.quit()
