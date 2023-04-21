class SingleLinkedList:

    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

    """ Por fuera de la clase nodo """
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def show_list(self):
        array_with_nodes_value = list()
        current_node = self.head 
        while(current_node != None):
            array_with_nodes_value.append(current_node.value)
            current_node = current_node.next
        print(array_with_nodes_value)
    
    def create_node_sll_ends(self, value):
        new_node = self.Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1
    
    def create_node_sll_unshift(self, value):
        new_node = self.Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            print(self.head.value)
        else:
            new_node.next = self.head
            self.head = new_node
        self.length +=1

    def delete_node_sll_pop(self):
        if self.length == 0:
            print('>> Lista vacía no hay nodos por eliminar <<')
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
        else:
            current_node = self.head
            new_tail = current_node
            while current_node.next != None:
                new_tail = current_node
                current_node = current_node.next
            print(f'Valor del nodo a eliminar es: {self.tail.value}')
            self.tail = new_tail
            self.tail.next = None
            self.length -= 1

    '''Eliminar nodo al inicio de la lista'''
    def shift_node_sll(self):
        if self.length == 0:
            print('>> Lista vacía no hay nodos por eliminar <<')
        elif self.length == 1:

            self.head = None
            self.tail = None
            self.length -= 1
        else:
            remove_node = self.head
            print(f'Valor del nodo a eliminar es: {remove_node.value}')
            self.head = remove_node.next
            self.length -=1
            
    def get_node(self, index):
        if index < 1 or index > self.length:
            return None
        elif index ==1:
            return self.head
        elif index == self.length:
            return self.tail
        else:
            current_node = self.head
            node_counter = 1
            while(index != node_counter):
                current_node = current_node.next
                node_counter += 1
            return current_node
    
    def update_node_value(self, index, new_value):
        seach_node = self.get_node(index)
        if seach_node != None:
            print(f'actualizando el valor del nodo')
            seach_node.value = new_value
        else:
            print("no encontro nodo")
    
    def remove_node(self, index):
        if index == 1:
            self.shift_node_sll()
        elif index == self.length:
            self.delete_node_sll_pop()
        else:
            remove_node_sll = self.get_node(index)
            if remove_node_sll != None:
                previus_node = self.get_node(index-1)
                previus_node.next = remove_node_sll.next
                remove_node_sll.next = None