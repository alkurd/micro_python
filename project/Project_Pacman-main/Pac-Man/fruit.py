import pygame
from Entity import entity
from Constants import *
from Sprites import FruitSprites

class Fruit(entity):
    def __init__(self, node, level=0):
        entity.__init__(self, node)
        self.name = FRUIT
        self.color = GREEN
        self.lifespan = 5
        self.timer = 0
        self.destroy = False
        self.points = 100 + level*20
        self.setBetweenNodes(RIGHT)
        self.sprites = FruitSprites(self, level)

    def update(self, dt):
        self.timer += dt
        if self.timer >= self.lifespan:
            self.destroy = True