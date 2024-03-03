import networkx as nx
import matplotlib.pyplot as plt

def dfs_paths(graph, start, goal, path=None):
    if path is None:
        path = [start]
    if start == goal:
        yield path
    for neighbor in graph.neighbors(start):
        if neighbor not in path:
            yield from dfs_paths(graph, neighbor, goal, path + [neighbor])

def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        current, path = queue.pop(0)
        for neighbor in graph.neighbors(current):
            if neighbor not in path:
                if neighbor == goal:
                    yield path + [neighbor]
                else:
                    queue.append((neighbor, path + [neighbor]))

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
    G.add_edge(edge[0], edge[1], distance=distance, color='lightblue')

start_city = 'Львів'
end_city = 'Рогатин'

# Шляхи за допомогою DFS
dfs_all_paths = list(dfs_paths(G, start_city, end_city))
print(f"DFS Шляхи від {start_city} до {end_city}:")
for path in dfs_all_paths:
    print(path)

# Шляхи за допомогою BFS
bfs_all_paths = list(bfs_paths(G, start_city, end_city))
print(f"\nBFS Шляхи від {start_city} до {end_city}:")
for path in bfs_all_paths:
    print(path)

pos = nx.spring_layout(G)
edge_colors = [G[edge[0]][edge[1]]['color'] for edge in G.edges()]

nx.draw(G, pos, with_labels=True, edge_color=edge_colors)
nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'distance'))

for path in dfs_all_paths:
    edges = list(zip(path, path[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='red', width=2)

for path in bfs_all_paths:
    edges = list(zip(path, path[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='blue', width=2)

plt.title("Шляхи між містами з використанням DFS та BFS")
plt.show()
