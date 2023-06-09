import pygame
from ComponentSup import Component

NEGRO = (0, 0, 0)


class OptionBox(Component):

    def __init__(self, x, y, width, height, color, highlight_color, font, option_list, selected=0):
        super().__init__(x, y, width, height)
        self.color = color
        self.highlight_color = highlight_color
        self.font = font
        self.option_list = option_list
        self.selected = selected
        self.draw_menu = False
        self.menu_active = False
        self.active_option = -1
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, screen):
        NEGRO = (0, 0, 0)
        pygame.draw.rect(screen, self.highlight_color if self.menu_active else self.color, self.rect)
        pygame.draw.rect(screen, NEGRO, self.rect, 2)
        msg = self.font.render(self.option_list[self.selected], 1, NEGRO)
        screen.blit(msg, msg.get_rect(center=self.rect.center))

        if self.draw_menu:
            for i, text in enumerate(self.option_list):
                rect = self.rect.copy()
                rect.y += (i + 1) * self.rect.height
                pygame.draw.rect(screen, self.highlight_color if i == self.active_option else self.color, rect)
                msg = self.font.render(text, 1, NEGRO)
                screen.blit(msg, msg.get_rect(center=rect.center))
            outer_rect = (
                self.rect.x, self.rect.y + self.rect.height, self.rect.width, self.rect.height * len(self.option_list))
            pygame.draw.rect(screen, NEGRO, outer_rect, 2)

    def updateposicion(self):
        return self.active_option
    
    def selectionoption(self):
        return self.option_list[self.active_option]

    def update(self, event_list):
        mpos = pygame.mouse.get_pos()
        self.menu_active = self.rect.collidepoint(mpos)
        self.active_option = -1
        for i in range(len(self.option_list)):
            rect = self.rect.copy()
            rect.y += (i + 1) * self.rect.height
            if rect.collidepoint(mpos):
                self.active_option = i
                break

        if not self.menu_active and self.active_option == -1:
            self.draw_menu = False

        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.menu_active:
                    self.draw_menu = not self.draw_menu
                elif self.draw_menu and self.active_option >= 0:
                    self.selected = self.active_option
                    self.draw_menu = False
                    return self.active_option
        return -1
