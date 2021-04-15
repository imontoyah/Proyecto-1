
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
        if data < actual.data:
            if actual.left == None:
               actual.left = Nodo(data)
            else:
                self.__insertar_aux(data,actual.left)
        else:
            if actual.right == None:
                actual.right = Nodo(data)
            else:
                self.__insertar_aux(data,actual.right)
   
    def buscar(self, data):
        return self.__buscar_aux(data, self.root)

    def __buscar_aux(self, data, actual):
        if actual == None:
           return False
        if actual.data == data:
            return True
        if data < actual.data:
            return self.__buscar_aux(data,actual.left)   
        return self.__buscar_aux(data,actual.right)

    def borrar(self, key):
        self.__borrar_aux(key, self.root)
    
    def __borrar_aux(self, data, actual):
        if actual is None:
            return  
        if data > actual.data:
            actual.right = self.__borrar_aux(data, actual.right)
        elif data < actual.data:
            actual.left = self.__borrar_aux(data, actual.left)
        else:
            if actual.left is None:
                temp = actual.right
                return temp
            elif actual.right is None:
                temp = actual.left
                return temp
            else:
                temp = self.__minValueNode(actual)
                actual.data = temp.data
                actual.right = self.__borrar_aux(temp.data, data)
        return actual
    
    def __minValueNode(self, actual):
        temp = actual
        while(temp.left is not None):
            temp = temp.left 
    
        return temp

    def imprimir(self):
        self.__imprimir_aux(self.root)
        
    def __imprimir_aux(self, actual):
        if actual is not None:
            self.__imprimir_aux(actual.left)
            print(actual.data)
            self.__imprimir_aux(actual.right)

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

