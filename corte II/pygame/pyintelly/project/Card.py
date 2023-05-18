import pygame


class Card:
    def __init__(self, image, value, x, y):
        self.x = x
        self.y = y
        self.image = self.image = pygame.image.load(image)
        self.value = value

    def draw(self, screen):
        # Dibujar la imagen en la pantalla en las coordenadas (x, y)
        screen.blit(self.image, (self.x, self.y))
