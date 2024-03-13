class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def printLevelOrder(root):
    if root is None:
        return
    
    # Usamos uma lista para simular uma fila (queue)
    queue = []
    # Adicionamos a raiz à fila
    queue.append(root)
    
    while len(queue) > 0:
        # Obtemos o nó atual da fila
        current_node = queue.pop(0)
        # Imprimimos o valor do nó
        print(current_node.data, end=' ')
        
        # Adicionamos os filhos à fila, se existirem
        if current_node.left is not None:
            queue.append(current_node.left)
        if current_node.right is not None:
            queue.append(current_node.right)

# Exemplo de uso
if __name__ == "__main__":
    # Construção da árvore da empresa
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    print("Ordem de nível da matriz da empresa:")
    printLevelOrder(root)
