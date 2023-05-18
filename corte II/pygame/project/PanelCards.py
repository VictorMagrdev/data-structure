import pygame
from ComponentSup import component
from PaneSub import Panel
from Player import Player

class Panelcards(Panel):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, width, height, color)
        self.color = color
        self.surface = pygame.Surface((width, height))
        self.surface.fill(color)
        self.players = list()
    
    def draw(self, screen):
        screen.blit(self.surface, (self.x, self.y))
        for i in self.players:
            i.draw(screen)