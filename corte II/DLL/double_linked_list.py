import time
from memory_profiler import memory_usage

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_node_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current =  self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            new_node.prev = current
        self.length += 1

    def add_node_at_start(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head= new_node
        self.length += 1

    def print_list(self):
        if self.head is None:
            return
        current = self.head
        while current is not None:
            print(current.data, end=' | ')
            current = current.next

    def add_node_in_position(self, position, data):
        print("cantidad de nodos: ", self.length)
        if position < 1 or position > self.length + 1:
            raise IndexError("posicion fuera del rango")
        new_node = Node(data)
        if position == 1:
            self.add_node_at_start(data)
        elif position == self.length +1:
            self.add_node_at_end(data)
        else:
            current_node = self.head
            for i in range(position -1):
                current_node = current_node.next
            new_node.next = current_node.next
            new_node.prev = current_node
            current_node.next.prev = new_node
            current_node.next = new_node
            self.length += 1

    def remove_node_at_start(self):
        if self.head is None:
            return
        else:
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
        self.length -1

    def remove_node_at_end(self):
        if self.head is None:
            return
        elif self.head.next is None:
            self.head = None
        else:
            current = self.head
            while current.next is not None:
                current= current.next
            current.prev.next = None
        self.length -= 1

    def remove_node_by_position(self, position):
        lenght = self.length
        if position < 1 or position > self.length + 1:
            raise IndexError("posicion fuera de rango")
        current_node = self.head
        if position == 1:
            self.remove_node_at_start()
        elif position == lenght:
            self.remove_node_at_end()
        else:
            for i in range(1, position):
                current_node = current_node.next
            current_node.prev.next = current_node.next
            current_node.next.prev = current_node.prev
            self.length -=1

    def remove_node_by_value(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            self.head.prev = None
            return
        current = self.head
        while current is not None:
            if current.data == data:
                if current.next is not None:
                    current.next.prev = current.prev
                current.prev.next = current.next
            current = current.next
            self.length -= 1

    def get_node_at_index(self, position):
        if self.head is None:
            return None
        current = self.head
        i = 1
        while current is not None and i<position:
            current = current.next
            i+=1
        return print(current.data)

    def get_node_by_value(self, data):
        if self.head is None:
            return None
        current = self.head
        while current is not None:
            if current.data == data:
                return print("nodo encontrado")
            current = current.next
        return print("nodo no encontrado")

    def update_node_at_index(self, position, data):
        if self.head is None:
            return
        current = self.head
        i = 1
        while current is not None and i < position:
            current = current.next
            i += 1
        if current is not None: 
            current.data = data

    def update_node_by_value(self, old_data, new_data):
        if self.head is None:
            return
        current = self.head
        while current is not None:
            if current.data == old_data:
                current.data = new_data
                return print(current.data)
            current = current.next

    def reverse(self):
        temporal_Node = None
        current = self.head
        while current is not None:
            temporal_Node = current.prev
            current.prev = current.next
            current.next = temporal_Node
            current = current.prev
        if temporal_Node is not None:
            self.head = temporal_Node

    def sort_asc(self):
        if self.head is None:
            return
        current = self.head
        while current.next is not None:
            next_node =  current.next
            while next_node is not None:
                if current.data > next_node.data:
                    current.data,next_node.data = next_node.data, current.data
                next_node = next_node.next
            current = current.next

    def has_duplicates(self):
        if self.head is None:
            return
        current = self.head
        values = set()
        while current is not None:
            if current.data in values:
                print(f'Find duplicates')
            values.add(current.data)
        print(values)
        return print('no duplicates')

    def has_duplicates_with_information_v2(self):
        if self.head is None:
            return
        current = self.head
        values= {}
        found_duplicates = False
        while current is not None:
            if current.data in values:
                values[current.data].append(current)
                found_duplicates = True
            else:
                values[current.data] = [current]
            current = current.next
        if found_duplicates:
            message = "the duplicates values are:\n"
            for value,nodes in values.items():
                if len(nodes) > 1:
                    message += f"- {value}: {len(nodes)} veces en los nodos "
                    message += ", " .join((str(Node))) + "\n"
            print(message)
            return True
        else:
            return False

    def calculate_complexity(self, func):
            func(0)

            start_time = time.time()
            func(0)
            end_time = time.time()
            exec_time = end_time - start_time

            mem_usage = max(memory_usage((func, (0,)), interval=0.1))

            print(f"Función {func.name}:")
            print(f"Tiempo de ejecución: {exec_time:.6f} segundos")
            print(f"Uso máximo de memoria: {mem_usage:.6f} MB")
            print("------------------------------------")