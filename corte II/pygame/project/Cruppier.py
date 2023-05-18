import pygame

class Cruppier:
    def __init__(self, name,x,y):
        self.name = name
        self.x = x
        self.y = y
        self.baraja = []
        self.button
        self.deck
        self.players

    def draw(self, screen):
        for i in self.baraja:
            i.draw(screen)
        self.button.draw(screen)
        font = pygame.font.SysFont('Arial', 25)
        text = font.render(self.name,True, (0,0,0))
        screen.blit(text, (self.x , self.y))
