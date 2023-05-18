import pygame


class ButtonCARD:
    def __init__(self, text, position):
        self.text = text
        self.position = position
        self.font = pygame.font.SysFont('', 32)
        self.width, self.height = self.font.size(text)
        self.rect = pygame.Rect(position[0], position[1], self.width, self.height)

        self.color = (255, 255, 255)  # Color normal del botón
        self.clicked_color = (128, 128, 128)  # Color del botón cuando se presiona
        self.turn = False

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        text_surface = self.font.render(self.text, True, (0, 0, 0))
        surface.blit(text_surface, self.position)

    def is_clicked(self, mouse_position):
        if self.rect.collidepoint(mouse_position):
            self.color = self.clicked_color  # Cambia el color del botón
            return True
        else:
            self.color = (255, 255, 255)  # Restaura el color normal del botón
            return False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.color = self.clicked_color  # Cambia el color del botón
                return True
        else:
            self.color = (255, 255, 255)  # Restaura el color normal del botón
        return False
