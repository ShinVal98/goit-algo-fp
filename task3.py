import heapq

# Обчислюю найкоротші шляхи від вершини start
def dijkstra(graph, start):
    # graph: {vertex: [(neighbor, weight), ...], ...}
    # Ініціалізую відстані та чергу
    distances = {v: float('inf') for v in graph}
    distances[start] = 0
    prev = {v: None for v in graph}
    queue = [(0, start)]

    while queue:
        dist, v = heapq.heappop(queue)
        if dist > distances[v]:
            continue  # ігнорую застарілу пару
        for neighbor, weight in graph[v]:
            alt = dist + weight
            if alt < distances[neighbor]:
                distances[neighbor] = alt
                prev[neighbor] = v
                heapq.heappush(queue, (alt, neighbor))
    return distances, prev

# Відновлюю шлях від start до target
def shortest_path(prev, target):
    path = []
    while target is not None:
        path.append(target)
        target = prev[target]
    return list(reversed(path))

if __name__ == "__main__":
    # приклад графа
    G = {
        'A': [('B', 1), ('C', 4)],
        'B': [('C', 2), ('D', 5)],
        'C': [('D', 1)],
        'D': []
    }
    start = 'A'
    distances, prev = dijkstra(G, start)
    print("Відстані:", distances)
    print("Шлях A -> D:", shortest_path(prev, 'D'))

