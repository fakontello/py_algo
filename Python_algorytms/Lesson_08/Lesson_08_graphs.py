from collections import namedtuple

# матрица смежности
graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [1, 1, 1, 0]
]

print(*graph, sep='\n')

# списки смежности
graph_2 = {
    0: {1, 2, 3},
    1: {0, 2, 3},
    2: {0, 1, 3},
    3: {0, 1, 2}
}
print(graph_2)

# граф с весом рёбер
Vertex = namedtuple('Vertex', ['vertex', 'edge'])
graph_3 = []

graph_3.append([Vertex(1, 2), Vertex(2, 3)])
graph_3.append([Vertex(0, 2), Vertex(2, 2), Vertex(3, 1)])
graph_3.append([Vertex(0, 3), Vertex(1, 2)])
graph_3.append([Vertex(1, 1)])

print(*graph_3, sep='\n')

class Graph:
    def __init__(self, vertex, edge, spam):
        self.vertex = vertex
        self.edge = edge
        self.spam = spam

# список рёбер(без веса)
graph_4 = [(0, 1), (0, 2), (1, 2), (2, 1), (1, 3)]
print(*graph_4, sep='\n')
