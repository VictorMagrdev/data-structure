import pygame
from ButtonSub import Button
from ButtonSubOk import ButtonOk
from ComponentSup import component
from single_linked_list import SingleLinkedList
from DropdownSub import OptionBox

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

    def draw(self, screen):
        screen.blit(self.surface, (self.x, self.y))
        self.dropdown.draw(screen)
        self.buttonok.draw(screen)
        for i in self.buttons:
            i.draw(screen)
        x_pos = 10
        for i in range(1, self.SLL.get_length_sll() +1 ):
            image = self.SLL.get_node(i).value
            screen.blit(image,( x_pos , 800))
            x_pos += 276
    
    def handle_event(self, panel):
        pass