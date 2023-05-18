import pygame

class Card:
    def __init__(self,image,value, reverse, x, y):
            self.x = x
            self.y = y
            self.image = image
            self.reverse = reverse
            self.value = value