import pygame
from ComponentSup import component

NEGRO = (0, 0, 0)

class ButtonOk(component):
    def __init__(self, x, y, width, height, text):
        super().__init__(x, y, width, height)
        self.text = text

    def draw(self, screen):
        pygame.draw.rect(
            screen, 
            NEGRO, 
            (   self.x, 
                self.y, 
                self.width, 
                self.height
                )
            )
        font = pygame.font.SysFont(
            'Arial',
            25
            )
        text = font.render(
            self.text,
            True, 
            (255, 255, 255)
            )
        screen.blit(
            text, 
            (
                self.x + (self.width / 2 - text.get_width() / 2),
                self.y + (self.height / 2 - text.get_height() / 2)
            )
        )

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if (x >= self.x and x < self.x + self.width and
                y >= self.y and y < self.y + self.height):
                return True