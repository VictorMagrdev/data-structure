import pygame
from ComponentSup import Component


class Button(Component):
    def __init__(self, x, y, width, height, image):
        super().__init__(x, y, width, height)
        self.image = image
        self.checked = False
        self.objet = None

    def setobject(self, objectintern):
        self.objet = objectintern

    def draw(self, screen):
        # Dibuja el borde del botón
        border_color = (255, 0, 0) if self.checked else (255, 255, 0)
        pygame.draw.circle(screen, border_color,
                           (self.x + self.width // 2, self.y + self.height // 2),
                           min(self.width, self.height) // 2,
                           5)
        # Carga y dibuja la imagen del botón
        image = pygame.image.load(self.image)
        screen.blit(image,
                    (self.x + (self.width - image.get_width()) / 2,
                     self.y + (self.height - image.get_height()) / 2))

    def handle_event(self, event):
        # Cambia el estado del botón al hacer clic en él
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if (self.x <= x < self.x + self.width and
                    self.y <= y < self.y + self.height):
                self.checked = not self.checked
