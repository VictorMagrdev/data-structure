import pygame
from ComponentSup import component

class sllprint():
    def __init__(self):
        self.rect = pygame.Rect(10, 400, 870, 200)
        self.image = list()

    def draw(self, screen):
        border_color = (255, 0, 0)
        
        pygame.draw.rect(screen, border_color, self.rect)
        available_width = self.rect.width - 10  
        available_height = self.rect.height - 10  
        x = self.rect.x + 5 
        y = self.rect.y + 5
        for image in self.image:
            image = pygame.image.load(image)
            if image.get_width() > available_width or image.get_height() > available_height:
                ratio = min(available_width / image.get_width(), available_height / image.get_height())
                new_size = (int(image.get_width() * ratio), int(image.get_height() * ratio))
                image = pygame.transform.scale(image, new_size)
            
            screen.blit(image, (x, y))
            x += image.get_width() + 5









