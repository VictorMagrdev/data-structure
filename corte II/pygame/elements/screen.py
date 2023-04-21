import pygame
from tabbedPane import TabbedPane, Panel
from button import Button
from dropdown import OptionBox

pygame.init()
screen = pygame.display.set_mode((900, 630))
color = (25,54,240)
list1 = OptionBox(
    40, 380, 160, 40, 
    (150, 150, 150), 
    (100, 200, 255), 
    pygame.font.SysFont(None, 30), 
    ["option 1",
    "2nd option",
    "another option"])

panel1 = Panel(0, 30, 942, 648, color)
panel2 = Panel(0, 30, 942, 648, color)

tabbed_pane = TabbedPane(0,0,620,460)
tabbed_pane.add_tab("SLL", panel1)
tabbed_pane.add_tab("DLL", panel2)

panel1.dropdown = list1
button_images = ["dragonbord red.png",
                "dragonborn monk.png",
                "dragonborn sitting.png"]
buttons = []
x_pos = 10
for image in button_images:
    button = Button(x_pos, 60, 266, 266, f"pygame\elements\\resources\{image}")
    panel1.buttons.append(button)
    buttons.append(button)
    x_pos += 276

run = True
while run:
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            run = False
        tabbed_pane.handle_event(event)
        for button in buttons:
            button.handle_event(event)

    selected_option = list1.update(event_list)
    if selected_option >= 0:
        print(selected_option)

    screen.fill((51,255,255))
    tabbed_pane.draw(screen)
    pygame.display.flip()

pygame.quit()