import matplotlib.pyplot as plt
import networkx as nx

# Створюю граф з масиву купи (0‑базований індекс)
def heap_to_graph(heap):
    G = nx.DiGraph()
    for i, val in enumerate(heap):
        G.add_node(i, label=str(val))
        left = 2*i + 1
        right = 2*i + 2
        if left < len(heap):
            G.add_node(left, label=str(heap[left]))
            G.add_edge(i, left)
        if right < len(heap):
            G.add_node(right, label=str(heap[right]))
            G.add_edge(i, right)
    return G

# Обчислюю позиції вузлів для гарного вигляду
def hierarchy_pos(G, root=0, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5):
    def _hierarchy_pos(G, root, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5, pos=None, parent=None):
        if pos is None:
            pos = {root: (xcenter, vert_loc)}
        else:
            pos[root] = (xcenter, vert_loc)
        children = list(G.successors(root))
        if len(children) != 0:
            dx = width/2
            nextx = xcenter - width/2 + dx/2
            for child in children:
                pos = _hierarchy_pos(G, child, width=dx, vert_gap=vert_gap,
                                     vert_loc=vert_loc-vert_gap, xcenter=nextx, pos=pos, parent=root)
                nextx += dx
        return pos
    return _hierarchy_pos(G, root, width, vert_gap, vert_loc, xcenter)

def visualize_heap(heap):
    G = heap_to_graph(heap)
    pos = hierarchy_pos(G)
    labels = nx.get_node_attributes(G, 'label')
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, labels=labels, with_labels=True, node_size=1500, node_color="#8cd3ff")
    plt.title("Бінарна купа")
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    heap = [0, 4, 1, 5, 10, 3]
    visualize_heap(heap)

