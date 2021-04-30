class Person:
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender

class Nodo:
    def __init__(self, data):
        self.left = None                    
        self.right = None
        self.data = data

    def __repr__(self):
        return f'{self.data}'
        
class BinaryTree:
    def __init__(self, head):
        self.root = Nodo(head)
        self.child = []

    def insert(self, data, head):   
        subTree = self.search(head)
        self.__insert_aux(data, subTree) 

    def __insert_aux(self, data, actual):
        if data.gender == "F":                                         
            if actual.left == None:                                      
               actual.left = Nodo(data)                                  
            else:
                self.__insert_aux(data,actual.left)                    
        elif data.gender == "M":
            if actual.right == None:                                    
                actual.right = Nodo(data)                              
            else:
                self.__insert_aux(data,actual.right)

    def preOrden(self, root):
        if root is not None:
            print(root.data.name)
            self.preOrden(root.left)
            self.preOrden(root.right)

    def search(self, person):
        return self.__search_aux(person, self.root)

    def __search_aux(self, person, actual):
        if actual.data == None:
           return person.name + " doesnt found in the binary tree"
        if actual.data.name == person.name:
            return actual
        if  person.gender == "F":
            return self.__search_aux(person,actual.left)   
        return self.__search_aux(person,actual.right)

    ##The fuction insert and search were taken from: https://github.com/imontoyah/ST0245-002/blob/master/talleres/taller10/BinaryTree.py
    
    def findGrandMa(self, person):
        foundPerson = self.search(person)
        if(foundPerson.left != None):
            if(foundPerson.left.left == None):
                return person.name + " doesn't have grandma"
            else:
                return person.name + "´s grandma is: " + foundPerson.left.left.data.name
        else:
            return person.name + " has not mother"

#M = Male and F = Female
class main:
    p1 = Person("Wilkenson", "M")
    p2 = Person("Joaquina", "F")
    p3 = Person("Sufranio", "M")
    p4 = Person("Eustaquia", "F")
    p5 = Person("Eustaquio", "M")
    p6 = Person("Florinda", "F")
    p7 = Person("Jovin", "M")
    p8 = Person("Piolina", "F")
    p9 = Person("Piolin", "M")
    p10 = Person("Wilberta", "F")
    p11 = Person("Usnavy", "M")

    b = BinaryTree(p1)
    b.insert(p2, p1 )
    b.insert(p3,p1)
    b.insert(p4, p2)
    b.insert(p5, p2)
    b.insert(p6, p4)
    #b.insert(p7, p5)
    b.insert(p8, p3)
    b.insert(p9, p3)
    #b.insert(p10, p8)
    b.insert(p11,p9)
  
    b.preOrden(b.root)
    print(b.findGrandMa(p1))
    print(b.findGrandMa(p2))
    print(b.findGrandMa(p3))
    print(b.findGrandMa(p4))
    #print(b.findGrandMa(p5))





