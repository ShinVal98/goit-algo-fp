import matplotlib.pyplot as plt
import networkx as nx
import matplotlib.colors as mcolors

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Створюю графічне представлення дерева
def add_edges(G, node, idx=0):
    if not node:
        return
    G.add_node(idx, label=str(node.value))
    if node.left:
        G.add_edge(idx, 2*idx+1)
        add_edges(G, node.left, 2*idx+1)
    if node.right:
        G.add_edge(idx, 2*idx+2)
        add_edges(G, node.right, 2*idx+2)

def build_graph(root):
    G = nx.DiGraph()
    add_edges(G, root)
    return G

# Роблю BFS або DFS і повертаю порядок відвідання
def traverse(root, mode="bfs"):
    order = []
    if mode == "bfs":
        queue = [root]
        while queue:
            node = queue.pop(0)
            order.append(node)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
    else:  # dfs
        stack = [root]
        while stack:
            node = stack.pop()
            order.append(node)
            # додаю праве перше, щоб ліве було зверху стека
            if node.right: stack.append(node.right)
            if node.left: stack.append(node.left)
    return order

# Візуалізую обхід
def visualize_traversal(root, mode="bfs"):
    order = traverse(root, mode)
    G = build_graph(root)
    pos = nx.nx_agraph.graphviz_layout(G, prog="dot")
    labels = nx.get_node_attributes(G, 'label')

    # Створюю кольорову карту від темного до світлого
    cmap = list(mcolors.TABLEAU_COLORS.values())
    colors = {node: cmap[i % len(cmap)] for i, node in enumerate(order)}

    node_colors = [colors[node] for node in G.nodes()]
    plt.figure(figsize=(8,6))
    nx.draw(G, pos, labels=labels, node_color=node_colors, with_labels=True, node_size=1400)
    plt.title(f"Обхід дерева ({mode.upper()})")
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    # приклад дерева
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)

    visualize_traversal(root, mode="dfs")
    visualize_traversal(root, mode="bfs")

