from Card import Card
import pygame
import random

class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        """
        Crea una baraja completa de 52 cartas
        """
        self.cards = []

    def shuffle(self):
        """
        Baraja la baraja
        """
        random.shuffle(self.cards)

    def repartir_card(self, player):
        """
        Saca una carta de la baraja
        """
