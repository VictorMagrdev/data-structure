import os
from ast import Index
import pygame
from TabbedPaneSub import TabbedPane, Panel
from PaneSub import Panel
from ButtonSub import Button
from DropdownSub import OptionBox
from single_linked_list import SingleLinkedList
from ButtonSubOk import ButtonOk
from sllprint import sllprint
from alert import AlertBox
from PaneSLL import PanelSLL
from PanelCards import Panelcards
from Player import Player
from buttoncard import ButtonCARD
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
    "remover nodos duplicados",
    "ordenar duplicados"
    ])
buttonok = ButtonOk(700, 340, 50, 30, "ok")
GREEN = (0, 128, 0)

panel1 = PanelSLL(0, 30, 942, 648, color)
panel2 = Panelcards(0, 30, 942, 648, GREEN)

tabbed_pane = TabbedPane(0,0,620,460)
tabbed_pane.add_tab("SLL", panel1)
tabbed_pane.add_tab("blackjact", panel2)

button1 = ButtonCARD( "Plantarme", [100,400])
button2 = ButtonCARD( "Plantarme", [350,400])
button3 = ButtonCARD( "Plantarme", [600,400])

player1= Player("juan", 100, 415, button1)
player2= Player("pedro", 350, 415, button2)
player3= Player("daniel", 600, 415, button3)

panel1.dropdown = list1
panel1.buttonok = buttonok
panel1.SLL = SLL
panel1.sllprint = imagenes

panel2.players.append(player1)
panel2.players.append(player2)
panel2.players.append(player3)

carpeta = "carpeta"
for archivo in os.listdir(carpeta):
    path = os.path.join(carpeta, archivo)
    print(path)


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
    if (panel1.SLL.length <= 7):    
        for i in buttons:
            if i.checked:
                image = i.image
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
        elif opcion == 9:
            panel1.opcionten()
        elif opcion == 10:
            panel1.opcioneleven()
    if panel1.SLL.length > 7:
        alertBox = AlertBox()
        alertBox.run(screen)

run = True
activeopcion = -1  
while run:
    event_list = pygame.event.get()

    for event in event_list:
        selected_option = list1.update(event_list)
        if selected_option >= 0:
            list1.updatePosicion()
            activeopcion = list1.active_option
        if buttonok.handle_event(event):
            Okaction(activeopcion, screen)
            panel1.sllprinte.draw(screen)
        if event.type == pygame.QUIT:
            run = False
        tabbed_pane.handle_event(event)
        button1.handle_event(event)
        button2.handle_event(event)
        button3.handle_event(event)
        for button in buttons:
            button.handle_event(event)

    screen.fill((51,255,255))
    tabbed_pane.draw(screen)
    pygame.display.flip()

pygame.quit()