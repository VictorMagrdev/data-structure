import pygame
import sys

class PopupWindow:
    def __init__(self, width, height, message):
        pygame.init()
        self.width = width
        self.height = height
        self.message = message
        self.bg_color = (255, 255, 255)
        self.font_color = (0, 0, 0)
        self.font = pygame.font.Font(None, 24)
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Ventana emergente")

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pygame.quit()
                        sys.exit()

            self.screen.fill(self.bg_color)
            text = self.font.render(self.message, True, self.font_color)
            text_rect = text.get_rect(center=(self.width // 2, self.height // 2))
            self.screen.blit(text, text_rect)

            pygame.display.flip()
