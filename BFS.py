from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbor):
        if node not in self.graph:
            self.graph[node] = []
        self.graph[node].append(neighbor)

    def bfs(self, start):
        visited = set()
        queue = deque([start])

        while queue:
            node = queue.popleft()
            if node not in visited:
                print(node, end=' ')
                visited.add(node)
                queue.extend(neighbor for neighbor in self.graph.get(node, []) if neighbor not in visited)

my_graph = Graph()
my_graph.add_edge('A', 'B')
my_graph.add_edge('A', 'C')
my_graph.add_edge('B', 'D')
my_graph.add_edge('B', 'E')
my_graph.add_edge('C', 'F')
my_graph.add_edge('C', 'G')


print("BFS starting from 'A':")
my_graph.bfs('A')