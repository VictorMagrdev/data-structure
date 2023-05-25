import sys

import pygame

from PaneSub import Panel


class Panelgraphs(Panel):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, width, height, color)
        self.color = color
        self.surface = pygame.Surface((width, height))
        self.surface.fill(color)