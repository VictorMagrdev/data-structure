import pygame

class NumericInputBox:
    def __init__(self, width=300, height=200, font_name='Arial', font_size=20):
        pygame.init()
        self.font = pygame.font.SysFont(font_name, font_size)
        self.width = width
        self.height = height
        pygame.display.set_caption("Ingresar valor numérico")
        self.input_box = pygame.Rect(50, 50, 200, 32)
        self.color_inactive = pygame.Color('lightskyblue3')
        self.color_active = pygame.Color('dodgerblue2')
        self.color = self.color_inactive
        self.text = ''
        self.active = False

    def run(self, screen):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    return None
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.input_box.collidepoint(event.pos):
                        self.active = not self.active
                    else:
                        self.active = False
                    self.color = self.color_active if self.active else self.color_inactive
                if event.type == pygame.KEYDOWN:
                    if self.active:
                        if event.key == pygame.K_RETURN:
                            try:
                                value = float(self.text)
                                running = False
                                return value
                            except ValueError:
                                self.text = ''
                                continue
                        elif event.key == pygame.K_BACKSPACE:
                            self.text = self.text[:-1]
                        else:
                            self.text += event.unicode

            pygame.draw.rect(screen, self.color, self.input_box, 2)

            text_surface = self.font.render(self.text, True, (0, 0, 0))
            screen.blit(text_surface, (self.input_box.x + 5, self.input_box.y + 5))

            pygame.display.flip()

        pygame.quit()
