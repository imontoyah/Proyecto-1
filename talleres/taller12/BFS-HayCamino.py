from collections import defaultdict
 
# This class represents a directed graph using adjacency list representation
class Graph:

    # Constructor
    def __init__(self):
        self.graph = defaultdict(list) #default dictionary to store graph
 
    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)
 
    # Function to print a BFS of graph
    def BFS(self, s):
 
        visited = [False] * (max(self.graph) + 1)  # Mark all the vertices as not visited
        queue = []  # Create a queue for BFS
 
        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True
 
        while queue:
 
            # Dequeue a vertex from queue and print it
            s = queue.pop(0)
            print (s, end = " ")
 
            # Get all adjacent vertices of the dequeued vertex s. If a adjacent has not been visited, then mark it visited and enqueue it
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
 
 
# Create a graph given in the above diagram
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
 
for i in range(4):
    print ("El siguiente es el recorrido del grafo en amplitud"
                  " (empezando desde el vertice " + str(i) + ")")
    g.BFS(i)
    print()