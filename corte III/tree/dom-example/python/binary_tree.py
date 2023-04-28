class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left_node = None
        self.right_node = None
    
    def insert(self,root, node):
        if root is None:
            root = None
        else:
            if root.value > node.value:
                if root.left_node is None:
                    root.left_node = node 
                else:
                    self.insert(root.left_node, node)
            else:
                if root.right_node is None:
                    root.right_node = node 
                else:
                    self.insert(root.right_node, node)
    
    def print_tree(self, root):
        if root is not None:
            self.print_tree(root.left_node)
            print(root.value)
            self.print_tree(root.right_node)


