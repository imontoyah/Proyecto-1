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
