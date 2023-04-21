from ast import Index
import pygame
from TabbedPaneSub import TabbedPane, Panel
from PaneSub import Panel
from ButtonSub import Button
from DropdownSub import OptionBox
from single_linked_list import SingleLinkedList
from ButtonSubOk import ButtonOk
from image import Image

pygame.init()

SLL = SingleLinkedList()
screen = pygame.display.set_mode((900, 630))
color = (25,54,240)

list1 = OptionBox(
    30, 340, 610, 25, 
    (150, 150, 150), 
    (100, 200, 255), 
    pygame.font.SysFont(None, 25), 
    ["Agregar un elemento al principio de la lista simplemente",
    "Agregar un elemento al final de la lista",
    "Eliminar el primer elemento de la lista",
    "Eliminar el último elemento de la lista",
    "Invertir la lista",
    "Eliminar todos los elementos de la lista",
    "Eliminar un elemento en una posición determinada de la lista",
    "Insertar un elemento en una posición determinada de la lista",
    "Actualizar el valor de un elemento en una posición determinada de la lista",
    ""
    ])
buttonok = ButtonOk(700, 340, 50, 30, "ok")

panel1 = Panel(0, 30, 942, 648, color)
panel2 = Panel(0, 30, 942, 648, color)

tabbed_pane = TabbedPane(0,0,620,460)
tabbed_pane.add_tab("SLL", panel1)
tabbed_pane.add_tab("DLL", panel2)

panel1.dropdown = list1
panel1.buttonok = buttonok
panel1.SLL = SLL

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


def Okaction(opcion):
    print(opcion)
    x_pos = 10
    for i in buttons:
        if i.checked:
            image = Image(i.image,x_pos , 800)
            x_pos += 276
            if opcion == 0:
                panel1.SLL.create_node_sll_unshift(image)
            elif opcion == 1:
                print("hello1")
                panel1.SLL.create_node_sll_ends(image)
            elif opcion == 2:
                print("hello2")
                panel1.SLL.delete_node_sll_pop()
            elif opcion == 3:
                panel1.SLL.delete_node_sll_pop()
            elif opcion == 4:
                panel1.SLL.reverse()
            elif opcion == 5:
                panel1.SLL.erase_all()
            elif opcion == 6:
                panel1.SLL.remove_node(i)
            elif opcion == 7:
                panel1.SLL.shift_node_sll()
            elif opcion == 8:
                panel1.SLL.sort_sll()


run = True
while run:
    event_list = pygame.event.get()
    
    for event in event_list:
        selected_option = list1.update(event_list)
        activeopcion = 0
        if selected_option > -1:
            activeopcion = selected_option
            print(selected_option)
        if event.type == pygame.QUIT:
            run = False
        tabbed_pane.handle_event(event)
        if buttonok.handle_event(event):
            Okaction(activeopcion)
            panel1.drawimage(screen)
        for button in buttons:
            button.handle_event(event)

    screen.fill((51,255,255))
    tabbed_pane.draw(screen)
    pygame.display.flip()

pygame.quit()