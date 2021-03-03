class ArrayList:

    __elements = []    #C1=1
    length = len(elements)
    
    def __init__(self):
        self.__elements = []  #C2=1

    def size(self):
        return length   #C3=1

    def get(self, index):
        return self.__elements[index]

    def add(self, object):
        self.__elements.append(object)

    def addInIndex(self, index, object):
        self.__elements.insert(index, object)

    def removeInIndex(self,index):
       self.__elements.pop(index)
    
arr = ArrayList()
arr.add(23)
print(arr.get(0))
