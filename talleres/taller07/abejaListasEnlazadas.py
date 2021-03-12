class Nodo():
    def __init__(self, obj=None, nxt = None):
        self.obj = obj                                      #C1 = 2                   
        self.nxt = nxt                                      
 
    def __str__(self):
        return "" + self.obj                                #C2 = 2
 
class Lsimple(): 
    def __init__(self):
        self.first_Node = None                              #C3 = 3
        self.last_Node = None
        self.size = 0
 
    def size(self):
        return self.size                                        #C4 = 1
    
     def get(self, index):
        if index < 0 and index>=self.size:                      #C0 = 5
            raise IndexError("La posición no existe")           #C0.1 = 7
        else:
            temp = self.first_Node                              #C0.3 = 1
            for i in range(index):                              #T(n) = n*C0.4
                temp = temp.nxt                                 #T(n) = n*C0.5
            return temp.obj                                     #C0.6 = 1
    
   def contains(self, element):                                 #C5 = 2
        cont = 0
        aux = self.first_Node
        while aux != None:                                         #T(n) = C6*n
            cont+=1                                                #C7 = 2 
            if(aux.obj == element):                                #C8 = 3
                return "La abeja esta en la posicion " + str(cont) #C8.0 = 3 
            aux = aux.nxt                                          #C9 = 2
        return "La abeja no esta en la lista"                      #C10 = 1
 
    def insertIndex(self, element, index):
        nuevo = Nodo(element)                               #C11 = 2

        if (index > self.size) or (index < 0):              #C12 = 5 
            raise IndexError("Posicion invalida")
        elif index == 0:                                    #C13 = 1
            nuevo.nxt = self.first_Node                     #C13.0 = 3
            self.first_Node = nuevo                         #C13.1 = 1
        else:
            n_ant = self.first_Node                         #C14 = 1
            for i in range(1,index):                        #T(n) = n*C15
                n_ant = n_ant.nxt                           #T(n) = n*C16 
            nuevo.nxt = n_ant.nxt                           #C17 = 1
            n_ant.nxt = nuevo                               #C18 = 1
        self.size +=1                                       #C19 = 1
    
    def removeIndex(self, index): 
        if index == None:                                   #C0 = 1
            index = self.size - 1                           #C0 = 2         
            self.size -= 1                                  #C0 = 1
            if index == 0:                                  #C0 = 2
                self.first_Node = self.first_Node.nxt       
            else:
                pre = self.first_Node                       #C0 = 1
                actual = pre.nxt                            #C0 = 1
                for i in range(1, index):                   #T(n) = n*C0
                    pre = actual                            #C0 = 1
                    actual = pre.nxt                        #C0 = 1
                pre.nxt = actual.nxt                        #C0 = 1                        
        elif (index < 0) or (index >= self.size):           #C0 = 3
            raise IndexError("Indice fuera de rango")       #C0 
        elif index == 0:                                    #C0 = 1
            self.first_Node = self.first_Node.nxt           #C0 = 1
            self.size -= 1                                  #C0 = 1
        else:
            pre = self.first_Node                           #C0 = 1
            n_act = pre.nxt                                 #C0 = 1
            for i in range(1, index):                       #T(n) = n*C0
                pre = n_act                                 #C0 = 1
                n_act = pre.nxt                             #C0 = 1
            pre.nxt = n_act.nxt                             #C0 = 1         
            self.size -= 1                                  #C0 = 1
     

class bee():
    def __init__(self, x, y, z): 
        self.x = x                                          #C0 = 1
        self.y = y                                          #C0 = 1
        self.z = z                                          #C0 = 1

            
class __main__():
    lista = Lsimple()
    bee1 = bee(4,1,3)
    bee2 = bee(2,3,1)
    bee3 = bee(1,3,6)
    bee4 = bee(2,8,4)
    lista.insertIndex(bee1, 0)
    lista.insertIndex(bee2, 1)
    lista.insertIndex(bee3, 2)
    lista.removeIndex()
    print(lista.contains(bee3))
    print(lista.get)
    
"""
Complejidad de agregar abejas en una posicion i para el peor de los casos
T(n) = C9 + C10 + C11 + C12 + C13 + C14 + C15*n + n*C16 + C17 + C18
T(n) = (C15 + C16)*n                                ---> Regla de la suma y factor comun
T(n) = n                                            ---> Regla del producto
O(n)
"""





   
