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
        nuevo = Nodo(element)                                #C = 2

        if (index > self.size) or (index < 0):              #C0 = 5 
            raise IndexError("Posicion invalida")
        elif index == 0:                                    #C0 = 1
            nuevo.nxt = self.first_Node                     #C0 = 3
            self.first_Node = nuevo                         #C0 = 1
        else:
            n_ant = self.first_Node                         #C0 = 1
            for i in range(1,index):                        #C0 = n
                n_ant = n_ant.nxt                           #C0 = 1
            nuevo.nxt = n_ant.nxt                           #C0 = 1
            n_ant.nxt = nuevo                               #C0 = 1
        self.size +=1                                       #C0 = 1
    
    def removeIndex(self, index): 
        if index == None:                                   #C0 = 1
            index = self.size - 1                           #C0 = 2         
            self.size -= 1                                  #C0 = 1
            if index == 0:                                  #C0 = 2
                self.first_Node = self.first_Node.nxt       
            else:
                pre = self.first_Node                       #C0 = 1
                actual = pre.nxt                            #C0 = 1
                for i in range(1, index):                   #C0 = n
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
            for i in range(1, index):                       #C0 = n
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





   
