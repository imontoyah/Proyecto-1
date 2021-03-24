import queue
from queue import LifoQueue
from collections import deque
class Nevera():
    def __init__(self, n, cod):
        self.num = n                              
        self.cod = cod
    def getNum(self):
        return self.num
    def getCod(self):
        return self.cod
        
class Almacen():
    def __init__(self, nom, cant):
        self.nom = nom                             
        self.cant = cant
        self.lista = list()
    def getNom(self):
        return self.nom
    def getCant(self):
        return self.cant
    def getList(self):
        return self.lista

class main():
    #Creo una pila que me almacene las neveras
    def inventario(self,n):
        stack = LifoQueue()
        for i in range(n):
            print("Ingrese un codigo y un numero: ")
            cod = str(input())
            num = int(input())
            nevera = Nevera(num, cod)
            stack.put(nevera)
        return stack
    #Creo una cola que me almacene los pedidos(con el nombre del almacen y la cantidad de neveras)
    def solicitudes(self,n):
        q = queue.Queue()
        for i in range(n):
            print("Ingrese el nombre del  alamcen y la cantidad de neveras: ")
            nom = str(input())
            cant = int(input())
            pedido = Almacen(nom, cant)
            q.put(pedido)
        return q      
    
    #Debo de hacer la asignacion de neveras a cada almacen 
    def asignarNevera(self,stack:LifoQueue(), queue:queue.Queue()):
        lista_de_Almacenes = list()
        for i in range(queue.qsize()):
            almacen = queue.get()
            for j in range(almacen.getCant()):
                if(stack.empty()):
                    break
                almacen.getList().append(stack.get())
            lista_de_Almacenes.append(almacen)
        return lista_de_Almacenes
  
    def __init__(self):
        stack1 = self.inventario(2)
        #for i in range(2):
        #    print(stack1.get().getCod())
          
        queue1 = self.solicitudes(2)
        #for i in range(2):
        #    print(queue1.get().getNom())
      
        lista_de_Almacenes = self.asignarNevera(stack1, queue1)
        for almacen in lista_de_Almacenes:
            neveras = almacen.getList()
            print("- "+almacen.getNom()+" -")
            for nevera in neveras:
                print(nevera.getCod())

main()