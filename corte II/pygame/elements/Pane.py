import pygame
from button import Button

class Panel:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.surface = pygame.Surface((width, height))
        self.surface.fill(color)
        self.buttons:Button = list()
        self.dropdown = None

    def draw(self, screen):
        screen.blit(self.surface, (self.x, self.y))
        self.dropdown.draw(screen)
        for i in self.buttons:
            i.draw(screen)

    def handle_event(self, event):
        pass  # Agrega aquí el código para manejar eventos