from collections import defaultdict

graph = {
    'A': {1, 2, 3},
    'B': {0, 2, 3},
    'C': {0, 1, 3},
    'D': {0, 1, 2}
}

for key in graph:
    print("key: %s , value: %s" % (key, graph[key]))
