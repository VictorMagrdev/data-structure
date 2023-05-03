import pygame
from ButtonSub import Button
from ButtonSubOk import ButtonOk
from ComponentSup import component
from single_linked_list import SingleLinkedList
from DropdownSub import OptionBox
from sllprint import sllprint
from NumericInput import NumericInputBox

class Panel(component):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, width, height)
        self.color = color
        self.surface = pygame.Surface((width, height))
        self.surface.fill(color)
        self.buttons = list()
        self.dropdown = OptionBox( 
                30, 340, 610, 25, 
                (150, 150, 150), 
                (100, 200, 255), 
                pygame.font.SysFont(None, 25), 
                [""
                ])
        self.buttonok = ButtonOk(700, 340, 50, 30, "ok")
        self.SLL = SingleLinkedList()
        self.sllprinte = sllprint()

    #Agregar un elemento al principio de la lista simplemente
    def opcionone(self,image):
        self.SLL.create_node_sll_unshift(image)
        imagelist = list()
        for i in range(1, self.SLL.get_length_sll() +1 ):
            image = self.SLL.get_node(i).value
            imagelist.append(image)
        self.sllprinte.image = imagelist

    #Agregar un elemento al final de la lista
    def opciontwo(self,image):
        self.SLL.create_node_sll_ends(image)
        imagelist = list()
        for i in range(1, self.SLL.get_length_sll() +1 ):
            image = self.SLL.get_node(i).value
            imagelist.append(image)
        self.sllprinte.image = imagelist
    
    #Eliminar el primer elemento de la lista
    def opcionthree(self):
        self.SLL.shift_node_sll()
        imagelist = list()
        for i in range(1, self.SLL.get_length_sll() +1 ):
            image = self.SLL.get_node(i).value
            imagelist.append(image)
        self.sllprinte.image = imagelist
    
    #Eliminar el último elemento de la lista
    def opcionfour(self):
        self.SLL.delete_node_sll_pop()
        imagelist = list()
        for i in range(1, self.SLL.get_length_sll() +1 ):
            image = self.SLL.get_node(i).value
            imagelist.append(image)
        self.sllprinte.image = imagelist
    
    #Invertir la lista
    def opcionfive(self):
        self.SLL.reverse()
        self.sllprinte.image.clear()
        imagelist = list()
        for i in range(1, self.SLL.get_length_sll() +1):
            image = self.SLL.get_node(i).value
            imagelist.append(image)
        self.sllprinte.image = imagelist

    
    #Eliminar todos los elementos de la lista
    def opcionsix(self):
        self.SLL.erase_all()
        imagelist = list()
        for i in range(1, self.SLL.get_length_sll() +1 ):
            image = self.SLL.get_node(i).value
            imagelist.append(image)
        self.sllprinte.image = imagelist
    
    #Eliminar un elemento en una posición determinada de la lista
    def opcionseven(self, screen):
        self.sllprinte.image.clear()
        input_box = NumericInputBox()
        value = int(input_box.run(screen))
        self.SLL.remove_node(value)
        imagelist = list()
        for i in range(1, self.SLL.get_length_sll() +1 ):
            image = self.SLL.get_node(i).value
            imagelist.append(image)
        self.sllprinte.image = imagelist
    
    #Insertar un elemento en una posición determinada de la lista
    def opcioneight(self,image, screen):
        self.sllprinte.image.clear()
        input_box = NumericInputBox()
        value = int(input_box.run(screen))
        self.SLL.insert_at_position(image, value)
        imagelist = list()
        for i in range(1, self.SLL.get_length_sll() +1 ):
            image = self.SLL.get_node(i).value
            imagelist.append(image)
        self.sllprinte.image = imagelist
    
    #Actualizar el valor de un elemento en una posición determinada de la lista
    def opcionnine(self, image, screen):
        self.sllprinte.image.clear()
        input_box = NumericInputBox()
        value = int(input_box.run(screen))
        self.SLL.update_node_value(value, image)
        imagelist = list()
        for i in range(1, self.SLL.get_length_sll() +1 ):
            image = self.SLL.get_node(i).value
            imagelist.append(image)
        self.sllprinte.image = imagelist

    def opcionten(self):
        self.sllprinte.image.clear()
        self.SLL.remove_duplicates()
        imagelist = list()
        for i in range(1, self.SLL.get_length_sll() +1 ):
            image = self.SLL.get_node(i).value
            imagelist.append(image)
        self.sllprinte.image = imagelist
    
    def draw(self, screen):
        screen.blit(self.surface, (self.x, self.y))
        
        self.sllprinte.draw(screen)
        self.dropdown.draw(screen)
        self.buttonok.draw(screen)
        
        for i in self.buttons:
            i.draw(screen)
        