class ArrayList:

    __elements = []

    def __init__(self):               # T(n) = C1
        self.__elements = []

    def size(self):                   # T(n) = C2
        return len(self.__elements)

    def get(self, index):              #T(n)= C3
        return self.__elements[index]

    def add(self, object):               # T(n) = n
        self.__elements.append(object)

    def addInIndex(self, index, object):      # T(n) = n
        self.__elements.insert(index, object)

    def removeInIndex(self,index):    # T(n) = n
       self.__elements.pop(index)
    
arr = ArrayList()    # T(n) = C4
arr.add(23)         # T(n) = n
print(arr.get(0))    # T(n) = C3

"""
Complejidad 
T(n) = C4+ C3 + n
T(n) = n    ---> Regla de la suma 
O(n)
"""

-------------------------------------------------ABEJAS CON NUMPY-------------------------------------------------------

import numpy as np

class ArrayList:
    DEFAUTL_CAPACITY = 0     # - - >
    elements = np.zeros(1)   # - - >      c1 = 3
    size = 0                 # - - >
    
    def __init__(self, D ,size):    
        self.DEFAUTL_CAPACITY = D         # - - >
        self.elements = np.zeros(D)       # - - >  c2 = 3
        self.size = size                  # - - >

    def size(self):
        return self.size            # - - >  C3 = 1

    def get(self, index) :
        if index < 0 or index >= self.size:                                            # - - > C4 = 4 
            raise Exception("Index out of bounds exception, index = "+format(index))   # - - > C5
        else:
            return self.elements[index]                                                # - - > C6

    def add(self, n):
        if self.size == self.elements.size: # O(n)
            nuevo = np.zeros[self.elements.size+10] #por defecto, es *2.0
            for i in range(0,self.elements.size):                                       # - - >  n  
                nuevo[i] = self.elements[i] # copiar n elementos, se hace en n pasos    # - - > C8 * n 
            self.elements = nuevo                                                       # - - > C9
        else:
            self.elements[self.size] = n                                                # - - > C10
        self.size = self.size + 1                                                       # - - > C11
                                                                                        # - - > O(n)

    def addInIndex(self, index, object):
        if index > self.elements.size:                                                  # - - > C12 = 3
            raise Exception("Index out of bounds, index = "+format(index))              # - - > C13
        if index == self.elements.size:                                                 #?
            nuevo = np.zeros[self.elements.size+1]
            for i in range(0,self.elements.size):                                       # - - > n
                nuevo[i] = self.elements[i] # copiar n elementos, se hace en n pasos    # - - > C14
            nuevo[index] = object                                                       # - - > C15
            self.elements = nuevo                                                       # - - > C16
        else:
            self.elements[index] = object                                               # - - > C17
        self.size = self.size +1                                                        # - - > C18

    def removeInIndex(self,index):
        nuevo = np.zeros[self.elements.size-1]                                          # - - > C19
        for i in range(0, self.elements.size-1):                                        # - - > n-1
            if self.elements[i] != self.elements[index]:                                # - - > (C20)*n-1
                nuevo[i] = self.element[i]                                              # - - > (C21)*n-1
                                                                         

arr = ArrayList(10,0)
arr.add(23) 
arr.add(28)
arr.add(4)
arr.add(8)
arr.addInIndex(4,10)
print(arr.get(4))

"""
COMPLEJIDAD DEL ALGORITMO ABEJAS: 
O(n) 

"""
