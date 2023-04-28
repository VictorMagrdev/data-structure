from ast import Index
import pygame
from TabbedPaneSub import TabbedPane, Panel
from PaneSub import Panel
from ButtonSub import Button
from DropdownSub import OptionBox
from single_linked_list import SingleLinkedList
from ButtonSubOk import ButtonOk
from sllprint import sllprint
from NumericInput import NumericInputBox

pygame.init()
imagenes = sllprint()
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
panel1.sllprint = imagenes

button_images = ["dragonbordred.png",
                "dragonbornmonk.png",
                "dragonbornsitting.png"]
buttons = []
x_pos = 10
for image in button_images:
    button = Button(x_pos, 60, 266, 266, f"C:\\UAM\\TAD 1SEM 2023\\corte II\\pygame\\project\\resources\{image}")
    panel1.buttons.append(button)
    buttons.append(button)
    x_pos += 276

def reset (button):
    button.checked = False
def Okaction(opcion, screen):
    print("posicion "+str(opcion))
    for i in buttons:
        if i.checked:
            image = pygame.image.load(i.image)
            if opcion == 0:
                panel1.opcionone(image)
            elif opcion == 1:
                panel1.opciontwo(image)
            elif opcion == 7:
                panel1.opcioneight(image, screen)     
            elif opcion == 8:
                panel1.opcionnine(image, screen)
            reset(i)
        
    if opcion == 2:
        panel1.opcionthree()
    elif opcion == 3:
        panel1.opcionfour()
    elif opcion == 4:
        panel1.opcionfive()
    elif opcion == 5:
        panel1.opcionsix()
    elif opcion == 6:
        panel1.opcionseven(screen)

run = True
activeopcion = -1  # initialize activeopcion outside of the loop
while run:
    event_list = pygame.event.get()

    for event in event_list:
        selected_option = list1.update(event_list)
        if selected_option >= 0:
            list1.updatePosicion()
            activeopcion = list1.active_option
            print("posicion "+str(activeopcion))
        if buttonok.handle_event(event):
            Okaction(activeopcion, screen)
            panel1.sllprinte.draw(screen)
        if event.type == pygame.QUIT:
            run = False
        tabbed_pane.handle_event(event)
        for button in buttons:
            button.handle_event(event)

    screen.fill((51,255,255))
    tabbed_pane.draw(screen)
    pygame.display.flip()

pygame.quit()