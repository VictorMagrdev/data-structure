import random

import pygame
from popwindow import PopupWindow

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
        self.resetbutton = None
        self.players = []
        self.startbutton = None
        self.cruppiermano = []
        self.puntaje = 0
        self.resultado = " "

    def shuffle(self):
        """
        Baraja la baraja
        """
        random.shuffle(self.baraja)
        
    def remove_cards_from_players(self):
        self.baraja.extend(self.cruppiermano)
        self.cruppiermano = []
        for player in self.players:
            self.baraja.extend(player.cards)
            player.cards = []
        self.analizarpuntaje()

    def determinar_resultados(self):
        if self.puntaje > 21:
            self.resultado = "Pierde"
        elif self.puntaje > max(jugador.puntaje for jugador in self.players):
            self.resultado = "Pierde"
        elif self.puntaje < max(jugador.puntaje for jugador in self.players if jugador.puntaje <= 21):
            self.resultado = "Gana"
        else:
            self.resultado = "Empate"

        for jugador in self.players:
            if jugador.puntaje > 21:
                jugador.resultado = "Pierde"
            elif jugador.puntaje > self.puntaje or self.puntaje > 21:
                jugador.resultado = "Gana"
            elif jugador.puntaje < self.puntaje:
                jugador.resultado = "Pierde"
            else:
                jugador.resultado = "Empate"

    def repartir_card(self):
        """
        Saca una carta de la baraja
        """
        self.cruppiermano.append(self.baraja[-1])
        self.baraja.pop()
        self.cruppiermano.append(self.baraja[-1])
        self.baraja.pop()
        for i in self.players:
            i.add_card(self.baraja[-1])
            self.baraja.pop()
            i.add_card(self.baraja[-1])
            
            self.baraja.pop()
    def cruppierturn(self):
        
        puntaje = 0
        for c in self.cruppiermano:
            puntaje += c.value
        self.puntaje= puntaje
        if puntaje <= 16:
            self.cruppiermano.append(self.baraja[-1])
            self.baraja.pop()
            
    def analizarpuntaje(self):
        for jugador in self.players:
            puntaje_total = 0
            for carta in jugador.cards:
                puntaje_total += carta.value
            jugador.puntaje = puntaje_total
        
    def pedir_card(self, player):
        """
        Saca una carta de la baraja
        """
        player.add_card(self.baraja[-1])
        self.analizarpuntaje()
        self.baraja.pop()


    def draw(self, screen):
        self.startbutton.draw(screen)
        for i in self.players:
            i.draw(screen)
        self.button.draw(screen)
        self.resetbutton.draw(screen)
        offset = 30

        for i, card in enumerate(self.cruppiermano):
            card.x = self.x + 230
            card.y = self.y - 120
            card.draw(screen)

        font = pygame.font.SysFont('Arial', 25)
        text = font.render(self.name, True, (0, 0, 0))
        screen.blit(self.reverso, (550, 60))
        screen.blit(text, (self.x, self.y))
        text = font.render(str(self.puntaje), True, (0, 0, 0))
        screen.blit(text, (self.x + 150, self.y))
        text = font.render(self.resultado, True, (0, 0, 0))
        screen.blit(text, (self.x+170, self.y))
