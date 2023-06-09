import json

import pygame
import os
import re
import graphvisualization

from TabbedPaneSub import TabbedPane
from ButtonSub import Button
from DropdownSub import OptionBox
from single_linked_list import SingleLinkedList
from ButtonSubOk import ButtonOk
from sllprint import Sllprint
from alert import AlertBox
from PaneSLL import PanelSLL
from PanelCards import Panelcards
from Player import Player
from buttoncard import ButtonCARD
from Cruppier import Cruppier
from Card import Card
from Panelgraphs import Panelgraphs
from facebook_visualization import UserExtractor

pygame.init()
imagenes = Sllprint()
SLL = SingleLinkedList()
screen = pygame.display.set_mode((900, 630))
color = (25, 54, 240)

list1 = OptionBox(
    30, 340, 610, 25,
    (150, 150, 150),
    (100, 200, 255),
    pygame.font.SysFont('', 25),
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
Blue = (0, 0, 255)

json_file = r'C:\\UAM\\TAD 1SEM 2023\\corte II\\pygame\\pyintelly\\project\\project\\facebook_data.json'

def extract_user_names_from_json(file_path):
    
    with open(file_path, "r") as file:
        data = json.load(file)
    users = data["users"]
    user_names = [user["name"] for user in users]

    return user_names

userlist = extract_user_names_from_json(json_file)

dropdown1 = OptionBox(
    600,35, 150, 20, Blue, (100, 200, 255), pygame.font.SysFont('', 25), userlist,
    )
dropdown2 = OptionBox(
    600,70, 220, 30, Blue, (100, 200, 255), pygame.font.SysFont('', 25), ["red familiares", "red amigos"],
    )

buttonredespropias = ButtonOk(600, 110, 100, 20, "dibujar")

dropdown3 = OptionBox(
    600,150, 180, 30, Blue, (100, 200, 255), pygame.font.SysFont('', 25), [""],
    )
dropdown4 = OptionBox(
    600,200, 280, 30, Blue, (100, 200, 255), pygame.font.SysFont('', 25), ["comunidades que ambos siguen"],
    )
buttonrfriends = ButtonOk(600, 260, 100, 20, "dibujar")

panel1 = PanelSLL(0, 30, 942, 648, color)
panel2 = Panelcards(0, 30, 942, 648, GREEN)
panel3 = Panelgraphs(0, 30, 942, 648, GREEN)

panel3.dropdownusuario = dropdown1
panel3.dropdowngrafo = dropdown2
panel3.dropdownamigo = dropdown3
panel3.dropdowntipografo = dropdown4
panel3.buttons.append(buttonredespropias)
panel3.buttons.append(buttonrfriends)

tabbed_pane = TabbedPane(0, 0, 620, 460)
tabbed_pane.add_tab("SLL", panel1)
tabbed_pane.add_tab("blackjact", panel2)
tabbed_pane.add_tab("grafos", panel3)

button1 = ButtonCARD("Plantarme", [100, 400])
button2 = ButtonCARD("Plantarme", [350, 400])
button3 = ButtonCARD("Plantarme", [600, 400])

player1 = Player("juan", 100, 415, button1,True)
player2 = Player("pedro", 350, 415, button2, False)
player3 = Player("daniel", 600, 415, button3, True)

panel1.dropdown = list1
panel1.buttonok = buttonok
panel1.SLL = SLL
panel1.sllprint = imagenes

buttonpedir = ButtonCARD("pedir", [400, 200])
buttonstart = ButtonCARD("start", [10, 40])
buttonreset = ButtonCARD("reset", [70, 40])
cruppier = Cruppier("Victoria Petrov", 400, 220)
cruppier.button = buttonpedir
cruppier.resetbutton = buttonreset
cruppier.startbutton = buttonstart
cruppier.players.append(player1)
cruppier.players.append(player2)
cruppier.players.append(player3)

carpeta = "C:\\UAM\\TAD 1SEM 2023\\corte II\\pygame\\pyintelly\\project\\carpeta"

for archivo in os.listdir(carpeta):
    if "reverso" in archivo:
        continue  
    path = os.path.join(carpeta, archivo)
    
    if "AS" in archivo:
        value = 1
    elif "J" in archivo or "Q" in archivo or "K" in archivo:
        value = 10
    else:
        num_str = re.search(r'\d+', archivo)
        value = int(num_str.group()) if num_str else 0
    card = Card(path, value, 550, 60)
    cruppier.baraja.append(card)

panel2.crupier = cruppier

button_images = ["dragonbordred.png",
                 "dragonbornmonk.png",
                 "dragonbornsitting.png"]
buttons = []
x_pos = 10
for image in button_images:
    button = Button(x_pos, 60, 266, 266, f"C:\\UAM\\TAD 1SEM 2023\\corte II\\pygame\\pyintelly\\project\\resources\\{image}")
    panel1.buttons.append(button)
    buttons.append(button)
    x_pos += 276


def reset(buttonintern):
    buttonintern.checked = False

def update_friends(user):
    userid = UserExtractor(json_file).get_user_by_name(user)
    friends = UserExtractor(json_file).get_friends_names(userid)
    dropdown3.option_list = friends

def turn(buttonevent):
    if player1.puntaje == "Gana" or player1.puntaje == "Pierde" or player1.puntaje == "Empate":
        pass
    elif player2.puntaje == "Gana" or player2.puntaje == "Pierde" or player2.puntaje == "Empate":
        pass
    elif player3.puntaje == "Gana" or player3.puntaje == "Pierde" or player3.puntaje == "Empate":
        pass
    elif player1.turno == True and cruppier.button.handle_event(buttonevent):
        cruppier.pedir_card(player1)
        player1.turno = False
        player2.turno  = True
        player3.turno = False
    elif player2.turno == True and cruppier.button.handle_event(buttonevent):
        cruppier.pedir_card(player2)
        player2.turno  = False
        player1.turno = False
        player3.turno = True
    elif player3.turno == True and cruppier.button.handle_event(buttonevent):
        cruppier.pedir_card(player3)
        player3.turno = False
        player2.turno  = False
        player1.turno = True
        cruppier.analizarpuntaje()
        cruppier.determinar_resultados()
        
def plantarseturn(buttonevent):
    if player1.turno == True and button1.handle_event(buttonevent):
        player1.turno = False
        player2.turno  = True
        player3.turno = False
    elif player2.turno == True and button2.handle_event(buttonevent):
        player2.turno  = False
        player1.turno = False
        player3.turno = True
    elif player3.turno == True and button3.handle_event(buttonevent):
        player3.turno = False
        player2.turno  = False
        player1.turno = True


def Okaction(opcion, screen_intern):
    if panel1.SLL.length <= 7:
        for i in buttons:
            if i.checked:
                imageintern = i.image
                if opcion == 0:
                    panel1.opcionone(imageintern)
                elif opcion == 1:
                    panel1.opciontwo(imageintern)
                elif opcion == 7:
                    panel1.opcioneight(imageintern, screen_intern)
                elif opcion == 8:
                    panel1.opcionnine(imageintern, screen_intern)
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
            panel1.opcionseven(screen_intern)
        elif opcion == 9:
            panel1.opcionten()
        elif opcion == 10:
            panel1.opcioneleven()
    if panel1.SLL.length > 7:
        alert_box = AlertBox()
        alert_box.run(screen_intern)


run = True
activeopcion = -1
while run:
    event_list = pygame.event.get()

    for event in event_list:
        selected_option = list1.update(event_list)
        if selected_option >= 0:
            list1.updateposicion()
            activeopcion = list1.active_option
        if buttonok.handle_event(event):
            Okaction(activeopcion, screen)
            panel1.sllprinte.draw(screen)
        if event.type == pygame.QUIT:
            run = False
        tabbed_pane.handle_event(event)
        
        if buttonredespropias.handle_event(event):
            if dropdown2.selectionoption == "red familiares":
                user = dropdown1.selectionoption
                image = graphvisualization.drawnodefamily(user)
                panel3.drawimage(screen, image)
            elif dropdown2.selectionoption ==  "red amigos":
                user = dropdown1.selectionoption
                image = graphvisualization.drawnodefriends(user)
                panel3.drawimage(screen, image)
        
        if dropdown1.update(event_list) >= 0:
            list1.updateposicion()
            userelection = dropdown1.selectionoption()
            update_friends(userelection)
            
        dropdown2.update(event_list)
        dropdown3.update(event_list)
        dropdown4.update(event_list)
        if buttonpedir.handle_event(event):
            turn(event)
            
        cruppier.shuffle()
        start = buttonstart.handle_event(event)
        if buttonreset.handle_event(event):
            cruppier.remove_cards_from_players()
        if start:
            cruppier.repartir_card()
            cruppier.analizarpuntaje()
            cruppier.cruppierturn()
        if button1.handle_event(event) or button2.handle_event(event) or button3.handle_event(event):
            plantarseturn(event)
        for button in buttons:
            button.handle_event(event)

    screen.fill((51, 255, 255))
    tabbed_pane.draw(screen)
    pygame.display.flip()

pygame.quit()
