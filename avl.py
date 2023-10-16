class Node():
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val
        self.height = 1

class EdgePrinter:
    def __init__(self, prev=None, str=None):
        self.prev = prev
        self.str = str

class AVLTree():
    def __init__(self):
        self.root = None

    def get_height(self, root):
        if not root:
            return 0
        return root.height
 
    def get_difference(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def rotate_left(self, x):
        y = x.right
        temp = y.left
        y.left = x
        x.right = temp
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def rotate_right(self, x):
        y = x.left
        temp = y.right
        y.right = x
        x.left = temp
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def balance(self, root):
        balance = self.get_difference(root)
        if balance > 1:
            if self.get_difference(root.left) > 0:
                return self.rotate_right(root), True
            else:
                root.left = self.rotate_left(root.left)
                return self.rotate_right(root), True
        elif balance < -1:
            if self.get_difference(root.right) < 0:
                return self.rotate_left(root), True
            else:
                root.right = self.rotate_right(root.right)
                return self.rotate_left(root), True
        return root, False

    def insert_node(self, key):
        self.root, should_print = self.insert(self.root, key)
        if should_print:
                self.print_tree()

    def insert(self, root, key):
        if not root:
            return Node(key), True
        elif key < root.val:
            root.left, should_print = self.insert(root.left, key)
            if should_print:
                self.print_tree()
        else:
            root.right, should_print = self.insert(root.right, key)
            if should_print:
                self.print_tree()
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        root, rotated = self.balance(root)
        return root, False or rotated

    def delete_node(self, key):
        self.root, should_print = self.delete(self.root, key)
        if should_print:
                self.print_tree()

    def delete(self, root, key):
        if not root:
            return root, True
        elif key < root.val:
            root.left, should_print = self.delete(root.left, key)
            if should_print:
                self.print_tree()
        elif key > root.val:
            root.right, should_print = self.delete(root.right, key)
            if should_print:
                self.print_tree()
        else:
            if root.left is None:
                return root.right, True
            elif root.right is None:
                return root.left, True
            temp = self.get_max_node(root.left)
            root.val = temp.val
            root.left, should_print = self.delete(root.left, temp.val)
            if should_print:
                self.print_tree()
        
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        root, rotated = self.balance(root)
        return root, False or rotated

    def get_max_node(self, root):
        if root is None or root.right is None:
            return root
        return self.get_max_node(root.right)
 
    def print_edge(self, edge):
        if edge is None:
            return
        self.print_edge(edge.prev)
        print(edge.str, end="")
        
    def print_tree(self):
        print("\n\n\n\n")
        self.print(self.root)
        print("\n\n\n\n")

    def print(self, root, prev_edge=None, is_left=False):
        if root is None:
            return
        prev_str = "      "
        edge = EdgePrinter(prev_edge, prev_str)
        self.print(root.right, edge, True)
    
        if prev_edge is None:
            edge.str = "—————"
        else:
            if is_left:
                edge.str = ".—————"
                prev_str = "     |"
            else:
                edge.str = "˙—————"
                prev_edge.str = prev_str
    
        self.print_edge(edge)
        print("", root.val)

        if prev_edge:
            prev_edge.str = prev_str

        edge.str = "     |"
        self.print(root.left, edge, False)

tree = AVLTree()
while True:
    text = input("Commands:\nInsert: /i <key>\nDelete: /d <key>\nQuit: /q\nEnter command: ")
    words = text.split()
    if len(words) == 0:
        continue
    command = words[0]
    if command == "/q":
        exit()
    if len(words) != 2 or not words[1].isdigit():
        continue
    key = int(words[1])
    if command == "/i":
        tree.insert_node(key)
    elif command == "/d":
        tree.delete_node(key)

    