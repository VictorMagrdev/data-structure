class SingleLinkedList:
    class Node:
        def __init__(self,value):
            self.value= value
            self.next = None
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def show_list(self):
        array_with_nodes_value = list()
        current_node = self.head
        while current_node != None:
            array_with_nodes_value.append(current_node.value*2)
            current_node = current_node.next
        print(f'Los valores deélos nodos de la lista son \n {array_with_nodes_value}')
        
    def create_node(self,value):
        new_node = self.Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length+=1
        