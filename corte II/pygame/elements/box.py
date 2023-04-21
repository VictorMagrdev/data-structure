import pygame
from button import Button

pygame.init()
screen = pygame.display.set_mode((800, 500))
button = Button(10, 60, 256, 90, "Hello")
betton = Button(120, 60, 90, 90, "Hello")
batton = Button(240, 60, 90, 90, "Hello")
buttons = []
buttons.append(button)
buttons.append(betton)
buttons.append(batton)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        for i in buttons:
            i.handle_event(event)

    screen.fill((0, 0, 0))
    for i in buttons:
        i.draw(screen)
    pygame.display.flip()

pygame.quit()