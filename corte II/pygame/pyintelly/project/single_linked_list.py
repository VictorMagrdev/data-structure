
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
        while current_node is not None:
            array_with_nodes_value.append(current_node.value)
            current_node = current_node.next
        print(array_with_nodes_value)

    def create_node_sll_ends(self, value):
        new_node = self.Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def create_node_sll_unshift(self, value):
        new_node = self.Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            print(self.head.value)
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

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
            while current_node.next is not None:
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
            self.length -= 1

    def get_node(self, index):
        if index < 1 or index > self.length:
            return None
        elif index == 1:
            return self.head
        elif index == self.length:
            return self.tail
        else:
            current_node = self.head
            node_counter = 1
            while index != node_counter:
                current_node = current_node.next
                node_counter += 1
            return current_node

    def get_node_value(self, index):
        if index < 1 or index > self.length:
            print('No se encontró')
        elif index == 1:
            print(self.head.value)
        elif index == self.length:
            print(self.tail.value)
        else:
            current_node = self.head
            node_counter = 1
            while index != node_counter:
                current_node = current_node.next
                node_counter += 1
            print(current_node.value)
            return current_node.value

    def update_node_value(self, index, new_value):
        search_node = self.get_node(index)
        if search_node is not None:
            print(f'Actualizando el valor del nodo ...\n'
                  f'           >> {search_node.value} << a\n'
                  f'           >>{new_value}<<')

            search_node.value = new_value
        else:
            print("     >> No se encontró el nodo <<")

    def remove_node(self, index):
        if index < 1 or index > self.length:
            raise IndexError("Índice fuera de rango.")
        if index == 1:
            self.head = self.head.next
            if self.length == 1:
                self.tail = None
        else:
            prev = None
            current = self.head
            for i in range(index - 1):
                prev = current
                current = current.next
            prev.next = current.next
            if index == self.length:
                self.tail = prev
        self.length -= 1

    def get_length_sll(self):
        return self.length

    def get_node_index(self, value):
        search_node = value
        seach_index = 1
        current_node = self.head
        while current_node.value != search_node:
            seach_index += 1
            current_node = current_node.next

        print("Del nodo " + search_node + " su indice es: " + str(seach_index))

    def reverse(self):
        if self.length > 1:
            aux_head = self.tail
            aux_tail = self.head
            if self.length == 2:
                self.head = aux_head
                self.head.next = aux_tail
                self.tail = aux_tail
                self.tail.next = None
                return

            current_node = self.tail
            for i in range(1, self.length - 1):
                node = self.get_node(self.length - i)
                current_node.next = node
                current_node = node
            node.next = aux_tail
            self.head = aux_head
            self.tail = aux_tail
            self.tail.next = None

    def erase_all(self):
        while self.head is not None:
            remove_node = self.head
            self.head = remove_node.next
            self.length -= 1

    def sort_sll(self):
        result = []
        current = self.head
        while current is not None:
            result.append(current.value)
            current = current.next
        self.erase_all()
        result.sort()
        for i in result:
            self.create_node_sll_ends(i)

    def insert_at_position(self, value, position):
        new_node = self.Node(value)
        if position == 0:
            self.create_node_sll_unshift()
            if self.head is None:
                self.head = new_node
                self.tail = new_node
        elif position == self.length:
            self.create_node_sll_ends()
        else:
            counter = 1
            current = self.head
            while counter < position - 1:
                counter += 1
                current = current.next
            new_node.next = current.next
            current.next = new_node
        self.length += 1

    def remove_duplicates(self):
        if self.head is None:
            return

        current = self.head
        seen_values = {current.value}

        while current.next is not None:
            if current.next.value in seen_values:
                current.next = current.next.next
                self.length -= 1
            else:
                seen_values.add(current.next.value)
                current = current.next
        self.tail = current

    def remove_duplicates(self):
        if self.head is None:
            return

        current = self.head
        seen_values = {current.value}

        while current.next is not None:
            if current.next.value in seen_values:
                current.next = current.next.next
                self.length -= 1
            else:
                seen_values.add(current.next.value)
                current = current.next
        self.tail = current

    def join_equal_nodes(self):
        if self.head is None:
            pass
        else:
            current = self.head
            seconcurrent = self.head
            seen_values = [current.value]
            duplicate_values = []
            while current.next is not None:
                if current.next.value in seen_values:
                    duplicate_values.append(current.next.value)
                    seen_values.remove(current.next.value)
                    current.next = current.next
                else:
                    seen_values.append(current.next.value)
                    current = current.next
            self.erase_all()
            for i in seen_values:
                self.create_node_sll_ends(i)
            for i in duplicate_values:
                self.create_node_sll_ends(i)
