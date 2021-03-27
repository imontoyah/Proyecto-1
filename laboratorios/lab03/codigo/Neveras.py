import queue
from queue import LifoQueue
from collections import deque
class Nevera():
    def __init__(self, n, cod):                                              
        self.num = n                                                        #C0
        self.cod = cod                                                      #C0.1
    def getNum(self):
        return self.num                                                     #C1
    def getCod(self):
        return self.cod                                                     #C2
        
class Almacen():
    def __init__(self, nom, cant):
        self.nom = nom                                                      #C3                 
        self.cant = cant                                                    #C3.1 
        self.lista = list()                                                 #C3.2
    def getNom(self):
        return self.nom                                                     #C4
    def getCant(self):
        return self.cant                                                    #C5
    def getList(self):
        return self.lista                                                   #C6

class main():
    #Creo una pila que me almacene las neveras (con su codigo y su numero)
    def inventario(self,n):                                                
        stack = LifoQueue()                                                 #C7
        for i in range(n):                                                  #C7.1*n , means  O(n) where n is the amount of refrigerators that have been received
            print("Ingrese un codigo y un numero: ")                        #C7.2
            cod = str(input())                                              #C7.3
            num = int(input())                                              #C7.4
            nevera = Nevera(num, cod)                                       #C7.5
            stack.put(nevera)                                               #C7.6   (add an element in a stack is constant)
        return stack                                                        #C7.7
    
    #Creo una cola que me almacene los pedidos(con el nombre del almacen y la cantidad de neveras)
    def solicitudes(self,n):
        q = queue.Queue()                                                   #C8
        for i in range(n):                                                  #C8.1*m , means  O(m) where m is the amount of requests that have been received
            print("Ingrese el nombre del  alamcen y la cantidad de neveras: ")   #C8.2
            nom = str(input())                                              #C8.3
            cant = int(input())                                             #C8.4
            pedido = Almacen(nom, cant)                                     #C8.5 
            q.put(pedido)                                                   #C8.6 (add an element in a queue is constant)
        return q                                                            #C8.7
    
    #Debo de hacer la asignacion de neveras a cada almacen 
    def asignarNevera(self,stack:LifoQueue(), queue:queue.Queue()):
        lista_de_Almacenes = list()                                         #C9
        for i in range(queue.qsize()):                                      #C9.1*m , where m is the queue's length with the number of requests
            almacen = queue.get()                                           #C9.2
            for j in range(almacen.getCant()):                              #C9.3*n*m , where n is the stack's length with the number of refrigerators
                if(stack.empty()):                                          #C9.4
                    break                                                   #C9.5
                almacen.getList().append(stack.get())                       # append en las listas en O(n) o O(1) ??
            lista_de_Almacenes.append(almacen)
        return lista_de_Almacenes
  
    def __init__(self, num1, num2):
        stack1 = self.inventario(num1)                                      #C10
        #for i in range(2):
        #    print(stack1.get().getCod())
          
        queue1 = self.solicitudes(num2)                                     #C10.1
        #for i in range(2):
        #    print(queue1.get().getNom())
      
        lista_de_Almacenes = self.asignarNevera(stack1, queue1)             #C10.2
        for almacen in lista_de_Almacenes:                                  #C10.3*m, where m is the queue's length with the number of requests
            neveras = almacen.getList()                                     #C10.4
            print("- "+almacen.getNom()+" -")                               #C10.5
            for nevera in neveras:                                          #C10.6*n*m , where n is the stack's length with the number of refrigerators
                print(nevera.getCod())                                      #C10.7

main(3, 2)
"""
Complexity for the worst case
T(n, m) = C + C7.1*n + C8.1*m + C9.1*m + C9.3*n*m + C10.3*m + C10.6*n*m
T(n, m) = C7.1*n + (C8.1 + C9.1 + C10.3)*m + (C9.3 + C10.6)*n*m              ---> Sum law and common factor
T(n, m) = n + m + n*m                                                        ---> Product law
T(n, m) = n*m   , let's p = m*n                                             ---> Sum law
T(p) = p
O(p) ,   where p = m*n and m is the queue's length with the number of requests and n is the stack's length with the number of refrigerators
"""
