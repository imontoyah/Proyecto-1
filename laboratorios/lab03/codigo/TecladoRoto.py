class Nodo():
    def __init__(self, obj=None, nxt = None):
        self.obj = obj                                                         
        self.nxt = nxt                                      
 
    def __str__(self):
        return "" + self.obj                                
 
class Lsimple(): 
    def __init__(self):
        self.first_Node = None                              
        self.last_Node = None
        self.size = 0
 
    def size(self):
        return self.size                                    
    
    def imprimirLista(self,lista):
        current = lista.first_Node
        while current is not None:
            print(current.obj, end = "")
            current = current.nxt

    def add_at_end(self, data):
        if not self.first_Node:
            self.first_Node = Nodo(obj=data)
            return
        curr = self.first_Node
        while curr.nxt:
            curr = curr.nxt
        curr.nxt = Nodo(obj=data)   

    def get_first_node(self):
        node = self.first_Node
        return node.data

    def push(self,data):
        new_node = Nodo(obj=data,)
        new_node.nxt = self.first_Node
        self.first_Node = new_node

    def remove_last(self): 
        temp = self.first_Node
        while(temp.nxt is not None):
            prev  = temp
            temp = temp.nxt
        prev.nxt = None

    def delete_node(self, key):
        curr = self.first_Node.nxt
        prev = None
        while curr and curr.obj != key:
            prev = curr
            curr = curr.nxt
        if prev is None:
            self.first_Node.nxt = curr.nxt
        elif curr:
            prev.nxt = curr.nxt
            curr.nxt = None
    
class TecladoRoto():

    def teclado(self,string):
        texto = Lsimple()                                                               #C1
        acc = 0     #0 - agregar al final / 1 - agrgar al inicio                        #C2
        aux = ''                                                                        #C3
        for i in range (len(string)):                                                   # n  - - > where n is the string´s length
            if string[i] != '[' and string[i] != ']':                                   #C4
               aux = aux + string[i]                                                    #C5
            if string[i] == '[':                                                        #C6
                if acc == 0:                                                            #C7
                    texto.add_at_end(aux)                                               # m - - > where m is the List´s length
                    aux = ''                                                            #C8
                else:
                    texto.push(aux)                                                     #C9
                    aux = ''                                                            #C10
                acc = 1                                                                 #C11
            if string[i] == ']':                                                        #C12
                if acc == 1:                                                            #C13
                    texto.push(aux)                                                     #C15
                    aux = ''                                                            #C16
                acc = 0                                                                 #c17
            if i == len(string)-1:                                                      #C18
                if acc == 0:                                                            #C19
                    texto.add_at_end(aux)                                               # m - - > where m is the List´s length
                    aux = ''                                                            #C20
                else:
                    texto.push(aux)                                                     #C21           
                    aux = ''                                                            #C22
        return (texto.imprimirLista(texto))                                             #m - - > where m is the List´s length
    
teclado = TecladoRoto()
print(TecladoRoto.teclado(TecladoRoto,'asd[fgh[jkl'))
"""
->T(n) = C1 + C2 + C3 + n*(C4 + C5 + C6 + C7 + m + C8 + C9 + C10 + C11 +C12 + C13 + C14 + C15 + C16  + C18 + C19 + m + C20 + C21 + C22)+m
->T(n) = C1 + C2 + C3 + C4*n + C5*n + C6*n + C7*n + m*n + C8*n + C9*n + C10*n + C11*n +C12*n + C13*n + C14*n + C15*n + C16*n  + C18*n +
C19*n + m*n + C20*n + C21*n + C22*n+ m
->T(n)= C4*n + C5*n + C6*n + C7*n + m*n + C8*n + C9*n + C10*n + C11*n +C12*n + C13*n + C14*n + C15*n + C16*n  + C18*n +
C19*n + m*n + C20*n + C21*n + C22*n+ m
->T(n) = n + n+ n + n + m*n + n + n + n + n +n + n + n + n+ n  + n + n + m*n + n + n+ n + m
->T(n) = n + n*m + m
- > p = n+m
   O(p+ n*m)
"""
    
