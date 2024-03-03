import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

# Визначення міст та відстаней між ними
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

pos = nx.spring_layout(G)
edge_colors = [G[edge[0]][edge[1]]['color'] for edge in G.edges()]
nx.draw(G, pos, with_labels=True, edge_color=edge_colors)
nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'distance'))
plt.title("Зв'язки міст")
plt.show()

# Базовий аналіз графа
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
avg_degree = sum(dict(G.degree()).values()) / num_nodes

print(f"Кількість вузлів: {num_nodes}")
print(f"Кількість ребер: {num_edges}")
print(f"Середня ступінь вузлів: {avg_degree}")
