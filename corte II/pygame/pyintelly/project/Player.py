import pygame


class Player:
    def __init__(self, name, x, y, button, turno):
        self.name = name
        self.x = x
        self.y = y
        self.cards = []
        self.button = button
        self.turno = turno
        self.puntaje = 0
        self.resultado = " "

    def add_card(self, card):
        self.cards.append(card)

    def get_hand_value(self):
        pass

    def clear_hand(self):
        self.cards = []

    def get_name(self):
        return self.name

    def draw(self, screen):
        self.button.draw(screen)
        offset = 30

        for i, card in enumerate(self.cards):
            card.x = self.x - (i * offset) + 30
            card.y = self.y + 45
            card.draw(screen)

        font = pygame.font.SysFont('Arial', 25)
        text = font.render(self.name, True, (0, 0, 0))
        screen.blit(text, (self.x, self.y))
        text = font.render(str(self.puntaje), True, (0, 0, 0))
        screen.blit(text, (self.x + 70, self.y))
        text = font.render(self.resultado, True, (0, 0, 0))
        screen.blit(text, (self.x+90, self.y))
