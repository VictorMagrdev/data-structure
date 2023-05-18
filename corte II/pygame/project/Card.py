import pygame

class Card:
    def __init__(self,image,value, reverse, x, y):
            self.x = x
            self.y = y
            self.image = image
            self.reverse = reverse
            self.value = value
    
    def draw(self, screen):
        # Carga y dibuja la imagen del botón
        image = pygame.image.load(self.image)
        screen.blit(image,
                (self.x,
                self.y))