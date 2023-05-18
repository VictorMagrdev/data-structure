from pygame import *

init()
screen = display.set_mode((800, 600))

name_font = font.Font(None, 32)
name_text = ''


class Rectangle:

    def __init__(self, x, y):
        self.active = False
        self.x = x
        self.y = y
        self.text_surface = name_font.render(name_text, True, (255, 255, 255))
        self.rect_width = max(140, 10 + self.text_surface.get_width())
        self.input_rect = Rect(x, y, self.rect_width, 32)
        draw.rect(screen, (0, 0, 0), self.input_rect, 0)
        draw.rect(screen, (255, 255, 255), self.input_rect, 2)
        self.input_rect.w = self.text_surface.get_width() + 10
        screen.blit(self.text_surface, (self.input_rect.x + 5, self.input_rect.y + 5))

    def naming(self, internevents):
        global rect_1
        global name_text

        for iter_e in internevents:
            if iter_e.type == MOUSEBUTTONDOWN:
                mx, my = iter_e.pos
                if self.input_rect.x + 150 >= mx >= self.input_rect.x - 10:
                    if self.input_rect.y + 40 >= my >= self.input_rect.y - 10:
                        self.active = True
                if not self.input_rect.x + 150 >= mx >= self.input_rect.x - 10:
                    if not self.input_rect.y + 40 >= my >= self.input_rect.y - 10:
                        self.active = False

            if iter_e.type == KEYDOWN:
                if self.active:
                    if iter_e.key == K_BACKSPACE:
                        name_text = name_text[:-1]
                    else:
                        name_text += iter_e.unicode
                    self.text_surface = name_font.render(name_text, True, (255, 255, 255))

    def draw(self, screenintern):
        draw.rect(screenintern, (0, 0, 0), self.input_rect, 0)
        draw.rect(screenintern, (255, 255, 255), self.input_rect, 2)
        self.input_rect.w = self.text_surface.get_width() + 10
        screenintern.blit(self.text_surface, (self.input_rect.x + 5, self.input_rect.y + 5))


rect_1 = Rectangle(200, 200)

run = True
while run:

    events = event.get()
    for e in events:
        if e.type == QUIT:
            run = False

    rect_1.naming(events)

    screen.fill(0)
    rect_1.draw(screen)
    display.update()
    time.delay(1)
