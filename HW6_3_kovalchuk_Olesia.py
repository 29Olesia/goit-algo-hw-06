import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from itertools import permutations

def dijkstra_shortest_paths(graph, start):
    distances = {node: float('inf') for node in graph.nodes}
    distances[start] = 0
    visited = {node: 0 for node in graph.nodes}

    while not all(visited.values()):
        current_node = min((node for node, mark in visited.items() if mark == 0), key=lambda x: distances[x])

        for neighbor in graph.neighbors(current_node):
            if visited[neighbor] == 0:
                new_distance = distances[current_node] + graph[current_node][neighbor]['distance']
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance

        visited[current_node] = 1

    return distances

def tsp_bruteforce(graph, cities):
    shortest_path_length = float('inf')
    shortest_path = None

    for permuted_cities in permutations(cities):
        total_distance = 0
        for i in range(len(permuted_cities) - 1):
            total_distance += graph[permuted_cities[i]][permuted_cities[i + 1]]['distance']
        total_distance += graph[permuted_cities[-1]][permuted_cities[0]]['distance']

        if total_distance < shortest_path_length:
            shortest_path_length = total_distance
            shortest_path = permuted_cities

    return shortest_path

G = nx.Graph()

cities = ['Львів', 'Миколаїв', 'Стрий', 'Журавно', 'Жидачів', 'Рогатин']
distances = {
    ('Львів', 'Миколаїв'): 38,
    ('Львів', 'Стрий'): 71,
    ('Львів', 'Журавно'): 81,
    ('Львів', 'Жидачів'): 67,
    ('Львів', 'Рогатин'): 72,
    ('Миколаїв', 'Стрий'): 35,
    ('Миколаїв', 'Журавно'): 43,
    ('Миколаїв', 'Жидачів'): 25,
    ('Миколаїв', 'Рогатин'): 59,
    ('Стрий', 'Журавно'): 47,
    ('Стрий', 'Жидачів'): 29,
    ('Стрий', 'Рогатин'): 68,
    ('Журавно', 'Жидачів'): 19,
    ('Журавно', 'Рогатин'): 35,
    ('Жидачів', 'Рогатин'): 39,
}

for city in cities:
    G.add_node(city)

for edge, distance in distances.items():
    G.add_edge(edge[0], edge[1], distance=distance, color=mcolors.to_rgba('lightgray', alpha=0.7))

city_numbers = {city: i + 1 for i, city in enumerate(cities)}

start_city = 'Львів'

shortest_paths = dijkstra_shortest_paths(G, start_city)
print(f"Найкоротші шляхи від {start_city}:")
for city, distance in shortest_paths.items():
    print(f"До {city} (місто {city_numbers[city]}): {distance}")

tsp_path = tsp_bruteforce(G, cities)
print(f"Оптимальний маршрут для відвідування всіх міст: {tsp_path}")

pos = nx.spring_layout(G)
edge_colors = [G[edge[0]][edge[1]]['color'] for edge in G.edges()]
nx.draw(G, pos, with_labels=True, edge_color=edge_colors)
nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'distance'))

tsp_edges = list(zip(tsp_path, tsp_path[1:]))
tsp_edges.append((tsp_path[-1], tsp_path[0]))
nx.draw_networkx_edges(G, pos, edgelist=tsp_edges, edge_color='blue', width=2)

city_positions = {city: (pos[city][0], pos[city][1] + 0.05) for city in G.nodes()}
nx.draw_networkx_labels(G, city_positions, labels={city: str(city_numbers[city]) for city in cities}, font_color='black')

plt.title("Граф з оптимальним маршрутом (Проблема комівояжера)")
plt.show()
