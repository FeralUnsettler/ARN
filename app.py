import random
import matplotlib.pyplot as plt

# Definição da classe Node para representar um nó da árvore
class Node:
    def __init__(self, key, color="RED"):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.color = color

# Definição da classe RedBlackTree para representar a árvore rubro-negra
class RedBlackTree:
    def __init__(self):
        self.NIL = Node(key=None, color="BLACK")
        self.root = self.NIL

    def insert(self, key):
        new_node = Node(key)
        new_node.left = self.NIL
        new_node.right = self.NIL

        parent = None
        current = self.root

        while current != self.NIL:
            parent = current
            if new_node.key < current.key:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent

        if parent is None:
            self.root = new_node
        elif new_node.key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

        new_node.color = "RED"
        self.fix_insert(new_node)

    def fix_insert(self, node):
        while node != self.root and node.parent.color == "RED":
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == "RED":
                    node.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self.right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == "RED":
                    node.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self.left_rotate(node.parent.parent)

        self.root.color = "BLACK"

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def inorder_traversal(self, node, x, y, dx):
        if node != self.NIL:
            plt.text(x, y, str(node.key), bbox=dict(facecolor=node.color, alpha=0.5), horizontalalignment='center')
            self.inorder_traversal(node.left, x - dx, y - 1, dx / 2)
            self.inorder_traversal(node.right, x + dx, y - 1, dx / 2)

# Função para gerar números aleatórios
def generate_random_numbers(length, min_value, max_value):
    return [random.randint(min_value, max_value) for _ in range(length)]

# Gerar uma árvore rubro-negra com números aleatórios entre 0 e 60
def generate_red_black_tree(numbers):
    tree = RedBlackTree()
    for num in numbers:
        tree.insert(num)
    return tree

# Gerar 20 números aleatórios entre 0 e 60
random_numbers = generate_random_numbers(20, 0, 60)

# Criar e plotar a árvore rubro-negra
rb_tree = generate_red_black_tree(random_numbers)
plt.figure(figsize=(10, 6))
rb_tree.inorder_traversal(rb_tree.root, 0.5, 1, 0.5)
plt.axis('off')
plt.title('Red-Black Tree')
plt.show()
