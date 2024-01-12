class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbor):
        if node not in self.graph:
            self.graph[node] = []
        self.graph[node].append(neighbor)

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()

        if start not in visited:
            print(start, end=' ')
            visited.add(start)
            for neighbor in self.graph.get(start, []):
                self.dfs(neighbor, visited)

my_graph = Graph()
my_graph.add_edge('A', 'B')
my_graph.add_edge('A', 'C')
my_graph.add_edge('B', 'D')
my_graph.add_edge('B', 'E')
my_graph.add_edge('C', 'F')
my_graph.add_edge('C', 'G')

print("DFS starting from 'A':")
my_graph.dfs('A')