import sys

import pygame

from PaneSub import Panel


class Panelgraphs(Panel):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, width, height, color)
        self.color = color
        self.surface = pygame.Surface((width, height))
        self.surface.fill(color)
        self.buttons = list()
        self.dropdownusuario = None
        self.dropdowngrafo = None
        self.dropdownamigo = None
        self.dropdowntipografo = None
        
    def drawimage(self, screen, image):
        image = pygame.image.load(image)
        screen.blit(self.image, (self.x, self.y))
        
    def draw(self, screen):
        screen.blit(self.surface, (self.x, self.y))
        for i in self.buttons:
            i.draw(screen)
        self.dropdowngrafo.draw(screen)
        self.dropdowntipografo.draw(screen)
        self.dropdownamigo.draw(screen)
        self.dropdownusuario.draw(screen)
        