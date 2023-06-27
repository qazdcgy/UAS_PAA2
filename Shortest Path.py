import sys
import time

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    visited = set()

    while len(visited) < len(graph):
        current_node = min(
            (node for node in graph if node not in visited),
            key=lambda node: distances[node]
        )

        visited.add(current_node)

        for neighbor, distance in graph[current_node].items():
            if neighbor not in visited:
                new_distance = distances[current_node] + distance
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance

    return distances

def tsp(graph, current_node, visited, distance, path, start_node):
    visited.add(current_node)
    path.append(current_node)

    if len(visited) == len(graph) and start_node in graph[current_node]:
        distance += graph[current_node][start_node]
        path.append(start_node)
        return distance, path

    min_distance = sys.maxsize
    min_path = []

    for node, weight in graph[current_node].items():
        if node not in visited:
            new_distance, new_path = tsp(
                graph, node, visited.copy(), distance + weight, path.copy(), start_node
            )
            if new_distance < min_distance:
                min_distance = new_distance
                min_path = new_path

    return min_distance, min_path

graph = {
    'a': {'b': 12, 'c': 10, 'g': 12},
    'b': {'a': 12, 'd': 12, 'c': 8},
    'c': {'a': 10, 'b': 8, 'd': 11, 'e': 3, 'g': 9},
    'd': {'b': 12, 'c': 11, 'e': 11, 'f': 10},
    'e': {'c': 3, 'd': 11, 'f': 6, 'g': 7},
    'f': {'d': 10, 'e': 6, 'g': 9},
    'g': {'a': 12, 'c': 9, 'e': 7, 'f': 9}
}

print("Pilih algoritma:")
print("1. TSP (Travelling Salesman Problem)")
print("2. Dijkstra")
choice = input("Masukkan pilihan (1/2): ")

if choice == '1':
    start_node = input("Masukkan simpul awal: ")

    start_time = time.time()
    distance, path = tsp(graph, start_node, set(), 0, [], start_node)
    end_time = time.time()

    print("Jarak terpendek: ", distance)
    print("Jalur terpendek: ", ' -> '.join(path))
    print("Waktu komputasi: ", end_time - start_time, "detik")

elif choice == '2':
    start_node = input("Masukkan simpul awal: ")

    start_time = time.time()
    distances = dijkstra(graph, start_node)
    end_time = time.time()

    for node, distance in distances.items():
        print("Jarak terpendek dari", start_node, "ke", node, ":", distance)

    print("Waktu komputasi: ", end_time - start_time, "detik")

else:
    print("Pilihan tidak valid.")
