### Este script gera uma árvore rubro-negra a partir de 20 números aleatórios entre 0 e 60 e imprime a árvore em ordem. 
##### A árvore pode não ser visualizada de forma gráfica, mas os números e suas cores (vermelho ou preto) serão impressos.

Os comentários explicam cada parte do código, desde a definição das classes e métodos até a geração de números aleatórios e a criação da árvore rubro-negra.
```python
import random

# Classe que define um nó da árvore
class Node:
    def __init__(self, key, color="RED"):
        self.key = key  # Valor armazenado no nó
        self.left = None  # Referência para o filho esquerdo
        self.right = None  # Referência para o filho direito
        self.parent = None  # Referência para o pai
        self.color = color  # Cor do nó, padrão é vermelho (RED)

# Classe que define uma árvore rubro-negra
class RedBlackTree:
    def __init__(self):
        self.NIL = Node(key=None, color="BLACK")  # Nó NIL representa um nó nulo (folha preta)
        self.root = self.NIL  # Raiz da árvore é inicialmente o nó NIL

    # Método para inserir um novo nó na árvore
    def insert(self, key):
        new_node = Node(key)  # Criar um novo nó com o valor especificado
        new_node.left = self.NIL  # O filho esquerdo é inicialmente o nó NIL
        new_node.right = self.NIL  # O filho direito é inicialmente o nó NIL

        parent = None  # Inicializar a referência para o pai como None
        current = self.root  # Começar a busca a partir da raiz

        # Encontrar a posição correta para inserir o novo nó
        while current != self.NIL:
            parent = current
            if new_node.key < current.key:
                current = current.left
            else:
                current = current.right

        # Atualizar as referências do novo nó e do pai
        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

        # O novo nó é inicialmente vermelho
        new_node.color = "RED"
        # Corrigir o balanceamento da árvore após a inserção
        self.fix_insert(new_node)

    # Método para corrigir o balanceamento da árvore após a inserção
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

    # Método para realizar uma rotação para a esquerda
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

    # Método para realizar uma rotação para a direita
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

    # Método para percorrer a árvore em ordem e imprimir os nós
    def inorder_traversal(self, node):
        if node != self.NIL:
            self.inorder_traversal(node.left)
            print(f"{node.key} - {node.color}")
            self.inorder_traversal(node.right)

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

# Criar e imprimir a árvore rubro-negra
rb_tree = generate_red_black_tree(random_numbers)
print("Árvore Rubro-Negra:")
rb_tree.inorder_traversal(rb_tree.root)
```

Esses comentários explicam cada parte do código, desde a definição das classes e métodos até a geração de números aleatórios e a criação da árvore rubro-negra. Isso deve ajudar a entender como o código funciona.
