import random

import pygame


class Cruppier:
    def __init__(self, name, x, y):
        self.button = None
        self.name = name
        self.x = x
        self.y = y
        self.reverso = pygame.image.load(
            'C:\\UAM\\TAD 1SEM 2023\\corte II\\pygame\\pyintelly\\project\\carpeta\\reverso.jpg')
        self.baraja = []
        self.button = None
        self.players = []
        self.startbutton = None

    def shuffle(self):
        """
        Baraja la baraja
        """
        random.shuffle(self.baraja)

    def repartir_card(self):
        """
        Saca una carta de la baraja
        """
        for i in self.players:
            i.add_card(self.baraja[-1])
            self.baraja.pop()
            i.add_card(self.baraja[-1])
            self.baraja.pop()

    def pedir_card(self, player):
        """
        Saca una carta de la baraja
        """
        player.add_card(self.baraja[-1])
        self.baraja.pop()


    def draw(self, screen):
        self.startbutton.draw(screen)
        for i in self.players:
            i.draw(screen)
        self.button.draw(screen)
        font = pygame.font.SysFont('Arial', 25)
        text = font.render(self.name, True, (0, 0, 0))
        screen.blit(self.reverso, (550, 60))
        screen.blit(text, (self.x, self.y))
