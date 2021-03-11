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
        return self.size                                     #C4 = 1
    
   
    def contains(self, element):
        aux = self.first_Node                               #C5 = 1
        while aux != None:                                  #C6 = 
            if(aux.obj == element):                         #C7 = 
                return True
            aux = aux.nxt
        return False  
 
    def insertIndex(self, element, index):
        nuevo = Nodo(element)                                #C = 

        if (index > self.size) or (index < 0):
            raise IndexError("Posicion invalida")
        elif index == 0:
            nuevo.nxt = self.first_Node
            self.first_Node = nuevo
        else:
            n_ant = self.first_Node
            for i in range(1,index):
                n_ant = n_ant.nxt
            nuevo.nxt = n_ant.nxt
            n_ant.nxt = nuevo
        self.size +=1
    
    def removeIndex(self, index): 
        if index == None:
            index = self.size - 1          
            self.size -= 1
            if index == 0:
                self.first_Node = self.first_Node.nxt
            else:
                pre = self.first_Node
                actual = pre.nxt
                for i in range(1, index):
                    pre = actual
                    actual = pre.nxt
                pre.nxt = actual.nxt
        elif (index < 0) or (index >= self.size):
            raise IndexError("Indice fuera de rango")
        elif index == 0:
            self.first_Node = self.first_Node.nxt
            self.size -= 1
        else:
            pre = self.first_Node
            n_act = pre.nxt
            for i in range(1, index):
                pre = n_act
                n_act = pre.nxt
            pre.nxt = n_act.nxt         
            self.size -= 1
     

class bee():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

            
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





   
