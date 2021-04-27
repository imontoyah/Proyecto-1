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
    
    def buildingTree(self, arr):     
        for i in range(len(arr)):                                          #O(n*m), where n is the array´s length and m is the number of nodes of the BinaryTree
            self.insert(arr[i])                                            #O(m),  m is the number of nodes of the BinaryTree

    def insert(self, data):
        if self.root is None:
            self.root = Nodo(data)
        else:
            self.__insert_aux(data, self.root)

    def __insert_aux(self, data, actual):                                   
        if data < actual.data:                                              #O(1)
            if actual.left == None:                                         #O(1)
               actual.left = Nodo(data)                                     #O(1)
            else:
                self.__insert_aux(data,actual.left)                         #O(m) where m is the number of nodes of the BinaryTree
        else:                                                               
            if actual.right == None:                                        #O(1)
                actual.right = Nodo(data)                                   #O(1)
            else:
                self.__insert_aux(data,actual.right)                        #O(m)  , where m is the number of nodes of the BinaryTree

    #The fuction insert were taken from: https://github.com/imontoyah/ST0245-002/blob/master/talleres/taller10/BinaryTree.py
    
    def posOrden(self, root):                   
        if root is not None:                                                #O(1)
            self.posOrden(root.left)                                        #O(m) , where m is the number of nodes of the BinaryTree
            self.posOrden(root.right)                                       #O(m)
            print(root.data)
            
    def sort(self, arr):
        self.buildingTree(arr)                                              #O(n*m), what is the complexity of the building tree function 
        print("PosOrder")                                                   #O(1)
        self.posOrden(self.root)                                            #O(n) , what is the posOrder complexity                                         
        print()                                                             #O(1)



arr = ["Wilkenson", "Joaquina", "Eustaquia", "Florinda", "Eustaquio", "Jovín", "Sufranio", "Piolina", "Wilberta", "Piolín", "Usnavy"]
#arr1 = [45, 23, 2, 7, 38, 65, 52, 48, 96]
arbol = BinaryTree()
arbol.sort(arr)




