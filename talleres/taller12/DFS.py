from collections import defaultdict
 
class Graph:
 
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
 
    # Esta funcion es para imprimir el recorrido en profundidad
    def DFS_aux(self, v, visited):
        visited.add(v)
        print(v, end=' ')
 
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFS_aux(neighbour, visited)

    def DFS(self, v):
        visited = set()
        self.DFS_aux(v, visited)

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 2)
g.addEdge(4, 3)
g.addEdge(4, 1)
 
for i in range(5):
    print ("El siguiente es el recorrido del grafo en profundidad"
                  " (empezando desde el vertice " + str(i) + ")")
    g.DFS(i)
    print()




 
