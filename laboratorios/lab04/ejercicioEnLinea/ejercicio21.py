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
#The time complexity for the worst case of building tree is O(n*m)

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
    
    #The time complexity for the worst case of insert an element is O(m)
    #The function insert were taken from: https://github.com/imontoyah/ST0245-002/blob/master/talleres/taller10/BinaryTree.py
    
    def posOrden(self, root):                   
        if root is not None:                                                #O(1)
            self.posOrden(root.left)                                        #O(m) , where m is the number of nodes of the BinaryTree
            self.posOrden(root.right)                                       #O(m)
            print(root.data)                                                #O(1)
    #The function posOrden has a time complexity for the worst case of O(m)
	
            
    def sort(self, arr):
        self.buildingTree(arr)                                              #O(n*m), what is the complexity of the building tree function 
        print("PosOrder")                                                   #O(1)
        self.posOrden(self.root)                                            #O(n) , what is the posOrder complexity                                         
        print()                                                             #O(1)
   #The function sort has a time complexity for the worst case of O(n*m)



arr = ["Wilkenson", "Joaquina", "Eustaquia", "Florinda", "Eustaquio", "Jovín", "Sufranio", "Piolina", "Wilberta", "Piolín", "Usnavy"]
#arr1 = [45, 23, 2, 7, 38, 65, 52, 48, 96]
arbol = BinaryTree()
arbol.sort(arr)

#Complexity for the worst case of posOrder a given array
# O(n*m) + O(m) + O(m) + O(n*m)             --> Sum law
# O(n*m) , due to n = m, the complexity for the worst case will be O(n^2)




