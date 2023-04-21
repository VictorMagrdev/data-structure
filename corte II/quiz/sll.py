class Sll:
    class Node:
        def __init__(self,value):
            self.value=value
            self.next=None
        
    def __init__(self):
        self.tail = None
        self.head = None
        self.lenght = 0
    
    def show_sll(self):
        array_with_values = []
        current_node = self.head
        while(current_node != None):
            array_with_values.append(current_node)
            current_node=current_node.next
        print(array_with_values)
    
    def append_node(self,value):
        new_node =self.Node(value)
        if self.lenght == 0:
            self.head = new_node
            self.tail = new_node
            self.lenght+=1
        else:
            self.tail.next = new_node
            self.tail= new_node
            self.lenght +=1
    def show_sll_x2(self):
        array_with_values = []
        current_node = self.head
        while(current_node != None):
            x2 = current_node.value*2
            array_with_values.append(x2)
            current_node=current_node.next
        print(array_with_values)