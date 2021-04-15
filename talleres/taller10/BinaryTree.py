
class Nodo:
    def __init__(self, data):
	self.left = None
	self.right = None
	self.data = data

    def __repr__(self):
	return f'{self.data}'

class BinaryTree:
	
    def __init__(self):
        self.root = None
        self.size = 0

    def insertar(self, data):
        if self.root is None:
            self.root = Nodo(data)
        else:
            self.__insertar_aux(data, self.root)

    def __insertar_aux(self, data, actual):
        if data < actual.data:                                           #C1
            if actual.left == None:                                      #C2
               actual.left = Nodo(data)                                  #C3
            else:
                self.__insertar_aux(data,actual.left)                    #T(n) = T(n)*C3.0
        else:
            if actual.right == None:                                     #C4
                actual.right = Nodo(data)                                #C5
            else:
                self.__insertar_aux(data,actual.right)                   #T(n) = T(n)*C6
   
    def buscar(self, data):
        return self.__buscar_aux(data, self.root)

    def __buscar_aux(self, data, actual):
        if actual == None:                                              #C1
           return False                                                 #C2
        if actual.data == data:                                         #C3
            return True                                                 #C4
        if data < actual.data:                                          #C5
            return self.__buscar_aux(data,actual.left)                  #T(n)= T(n)*C6 
        return self.__buscar_aux(data,actual.right)                     #T(n)= T(n)*C7

    def borrar(self, key):
        self.__borrar_aux(key, self.root)
    
    def __borrar_aux(self, data, actual):
        if actual is None:                                                #C1
            return        
        if data > actual.data:                                            #C2
            actual.right = self.__borrar_aux(data, actual.right)          #T(n) = T(n)*C3
        elif data < actual.data:                                          #C4
            actual.left = self.__borrar_aux(data, actual.left)            #T(n) = T(n)*C5
        else:
            if actual.left is None:                                       #C5
                temp = actual.right                                       #C6
                return temp                                               #C7
            elif actual.right is None:                                    #C8
                temp = actual.left                                        #C9
                return temp                                               #C10
            else:
                temp = self.__minValueNode(actual)                       
                actual.data = temp.data                                  #C12
                actual.right = self.__borrar_aux(temp.data, data)        #T(n) = T(n)*C13
        return actual                                                    #C14

    def __minValueNode(self, actual):
        temp = actual
        while(temp.left is not None):
            temp = temp.left 
    
        return temp

    def __imprimir_aux(self, actual):
        if actual is not None:                                           #C1                 
            self.__imprimir_aux(actual.left)                             #T(n)= T(n)*C2
            print(actual.data)                                           #C3
            self.__imprimir_aux(actual.right)                            #T(n)= T(n)*C4


    def dibujar(self):
        return  f'digraph G {"{"} \n {self.__dibujar_aux(self.root)} \n{"}"}'
    
    def __dibujar_aux(self, actual):
        if actual is None:
            return 
        else:
            if actual.left is not None and actual.right is not None:
                return f'{actual} -> {actual.left} \n {actual} -> {actual.right}'
            if actual.left is not None:
                return f'{actual} -> {actual.left}'
            if actual.right is not None:
                return f'{actual} -> {actual.right}'
