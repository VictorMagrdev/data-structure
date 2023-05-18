import sys

import pygame

from PaneSub import Panel


class Panelcards(Panel):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, width, height, color)
        self.color = color
        self.surface = pygame.Surface((width, height))
        self.surface.fill(color)
        self.crupier = None

        self.play_button_rect = pygame.Rect(50, 50, 100, 50)
        self.replay_button_rect = pygame.Rect(50, 50, 100, 50)
        self.font = pygame.font.Font(None, 36)

        self.playing = False
        self.opacity_enabled = False  # Variable de instancia para habilitar la opacidad

    def draw(self, screen):
        screen.blit(self.surface, (self.x, self.y))
        self.crupier.draw(screen)

    def handle_event(self, event):
        pass

