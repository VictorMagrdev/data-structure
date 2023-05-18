import pygame
from buttoncard import ButtonCARD
from Card import Card

class Player:
    def __init__(self, name,x,y, button):
        self.name = name
        self.x = x
        self.y = y
        self.cards = []
        self.button = button

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
        for i in self.cards:
            i.draw(screen)
        font = pygame.font.SysFont('Arial', 25)
        text = font.render(self.name,True, (0,0,0))
        screen.blit(text, (self.x , self.y))
