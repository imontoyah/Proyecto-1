import math

class Grafo:
    def __init__(self):
        self.vertices = []
        self.matriz = [[None]*0 for i in range(0)]
        
    def contains_vertice(self,v):
        if self.vertices.count(v) ==0:
            return False
        return True
    
    def agregar_vertice(self,v):
        if self.contains_vertice(v):
            return False
        self.vertices.append(v)
        
        filas = columnas = len(self.matriz)
        matriz_aux = [[None]*(filas+1) for i in range (columnas+1)]
        
        for i in range(filas):
            for j in range(columnas):
                matriz_aux[i][j] = self.matriz[i][j]
        
        self.matriz = matriz_aux
        return True
    
    def agregar_arista(self, inicio, fin, valor, dirigida):
        if not(self.contains_vertice(inicio) or not (self.contains_vertice(fin))):
            return False
        self.matriz[self.vertices.index(inicio)][self.vertices.index(fin)] = valor
        
        if not dirigida:
            self.matriz[self.vertices.index(fin)][self.vertices.index(inicio)] = valor
        return True  
    
    def getSuccessors(self, vertex):
        succs = []
        for k, v in enumerate(self.matriz[vertex]):
            if v != 0:
                succs.append(v)
            else:
                succs.append(0)
        return succs
    
    def imprimir(self, matriz):
        cadena = '\n'
        
        for i in range(len(matriz)):
            cadena += '\t'+str(self.vertices[i])
        cadena += '\n ' 
        
        for i in range(len(matriz)):
            cadena += '\n' + str(self.vertices[i]) + " "
         
            for j in range(len(matriz)):
                if i == j and (matriz[i][j] is None or matriz[i][j]==0):
                    cadena += '\t' + '0'
                else:
                    if matriz[i][j] is None:
                        cadena += '\t' + '0'
                    elif math.isinf(matriz[i][j]):
                        cadena += '\t' + 'm'
                    else:
                        cadena += '\t' + str(matriz[i][j])                        
        cadena += '\n' 
        print(cadena)

class main:
    g = Grafo()
    for i in range(6):
       g.agregar_vertice(i)
 
    g.agregar_arista(0, 1, 5, True)
    g.agregar_arista(0, 3, 7, True)
    g.agregar_arista(0, 4, 2, True)
    g.agregar_arista(1, 2, 3, False)
    g.agregar_arista(2, 3, 8, False)
    g.agregar_arista(3, 4, 1, True)
   
    g.imprimir(g.matriz)
    print(g.getSuccessors(0))
        
                        
                    
        
