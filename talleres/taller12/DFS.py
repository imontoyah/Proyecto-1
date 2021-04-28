from collections import defaultdict

class Graph:
 
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
 
    # Esta funcion es para imprimir el recorrido en profundidad
    def DFS_aux(self, origen, visitado):
        visitado.add(origen)
        print(origen, end=' ')
 
        for vecino in self.graph[origen]:
            if vecino not in visitado:
                self.DFS_aux(vecino, visitado)

    def DFS(self, origen):
        visitado = set()
        self.DFS_aux(origen, visitado)

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




 




 
