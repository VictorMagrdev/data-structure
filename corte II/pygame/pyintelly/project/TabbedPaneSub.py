import pygame
from ComponentSup import Component


class TabbedPane(Component):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.tabs = []
        self.active_tab = 0

    def add_tab(self, title, panel):
        self.tabs.append((title, panel))

    def get_tab(self):
        return self.tabs

    def draw(self, screen):
        # Dibuja los títulos de las pestañas
        for i, (title, panel) in enumerate(self.tabs):
            color = (255, 0, 10) if i == self.active_tab else (0, 204, 255)
            pygame.draw.rect(screen, color, (self.x + i * 100, self.y, 100, 30))
            font = pygame.font.Font(None, 24)
            text = font.render(title, True, (0, 0, 0))
            screen.blit(text, (self.x + i * 100 + 10, self.y + 5))
        # Dibuja el panel activo
        panel = self.tabs[self.active_tab][1]
        panel.draw(screen)

    def handle_event(self, event):
        # Cambia la pestaña activa al hacer clic en un título
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if self.y <= y < self.y + 30:
                for i in range(len(self.tabs)):
                    if self.x + i * 100 <= x < self.x + (i + 1) * 100:
                        self.active_tab = i
