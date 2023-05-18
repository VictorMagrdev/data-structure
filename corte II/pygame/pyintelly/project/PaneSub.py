import pygame
from ComponentSup import component

from abc import ABC, abstractmethod

class Panel(component, ABC):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, width, height)
        self.color = color
        self.surface = pygame.Surface((width, height))
        self.surface.fill(color)
    
    @abstractmethod
    def draw(self, screen):
        pass