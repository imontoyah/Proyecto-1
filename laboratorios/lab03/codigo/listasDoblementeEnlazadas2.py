class Node:
    def __init__(self,prev=None ,data=None ,next=None):
        self.prev = prev
        self.data = data
        self.next = next

    def __str__(self):
        return "" + str(self.data)

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def size(self):
        return self.size                                        #C0 = 1
      
    def get(self, index):
        if index < 0 and index>=self.size:                      #C0 = 5
            raise IndexError("La posición no existe")           #C0.1 = 7
        else:
            temp = self.head                                    #C0.3 = 1
            for i in range(index):                              #T(n) = n*C0.4
                temp = temp.next                                #T(n) = n*C0.5
            return temp.data                                    #C0.6 = 1
    """
    Complexity of get a element:
    T(n) = C + C0.4*n + n*C0.5 
    T(n) = (C0.4 + C0.5)*n                            ---> Sum law and common factor 
    T(n) = n                                          ---> Product law
    O(n)  where n is the linked list length
    """

    def append(self, data):
        new_node = Node(None, data, None)                       #C1 
        if self.head is None:                                   #C1.0 
            self.head = new_node                                #C1.1
            self.tail = self.head                               #C1.2
        else:
            new_node.prev = self.tail                           #C1.3
            self.tail.next = new_node                           #C1.4
            self.tail = new_node                                #C1.5
        self.size+=1                                            #C1.6
    
    def add(self, data, index):
        new_node = Node(None, data, None)                       #C2

        if self.head is None:                                   #C2.0
            self.head = new_node                                #C2.1
            self.tail = self.head                               #C2.2
            self.size+=1                                        #C2.3
        elif index == self.size:                                #C2.4
            self.append(data)                                   #C2.5*n, means O(n) where n is the list length
        elif index == 0:                                        #C2.6
            new_node.next = self.head                           #C2.7
            self.head = new_node                                #C2.8
            self.size+=1                                        #C2.9
        elif index<self.size:                                   #C2.10
            pre = self.head                                     #C2.11
            for i in range(index-1):                            # C2.12*n,  means O(n)  where n is the index value???
                pre = pre.next                                  #C2.13
            new_node.next = pre.next
            pre.next = new_node                                  #C2.14
            new_node.prev = pre                                  #C2.15
            pre.next.prev = new_node                             #C2.16
            self.size+=1                                         #C2.17
        else:
            print("Index not reachable")                         #C2.18
    
    """
    Complexity of add data in an index:
    T(n) = C + C2.5*n + n*C2.12 
    T(n) = (C2.5 + C2.12)*n                            ---> Sum law and common factor 
    T(n) = n                                           ---> Product law
    O(n)
    """

    def delete(self, index):
        if self.head is None:
            print("The list has no element to delete")
            return 
        if index == 0 and self.size == 1:
            self.head = None
            self.tail = None
            self.size-=1
        elif index == 0:
            self.head = self.head.next
            self.size-=1
        elif (index < 0) or (index >= self.size):           #C0 = 3
            raise IndexError("Indice fuera de rango")  
        elif index == self.size-1:
            pre=self.head
            for i in range(index-1):
                 pre=pre.next
            self.tail=pre
            pre.next=None
            self.size-=1
        elif index == self.size-2:
            pre=self.head
            for i in range(index-2):
                 pre=pre.next
            self.tail.prev=pre
            pre.next=self.tail
            self.size-=1
        else:
            pre=self.head
            for i in range(index-1):
                 pre=pre.next
            pre.next.next.prev=pre
            pre.next=pre.next.next
            self.size-=1
        """elif index==self.size-2:
            pre=self.head
            for i in range(index-1):
                pre=pre.next
            pre.next.next.prev=pre
            pre.next=pre.next.next
            pre.next.next=self.tail
            self.size-=1"""

    def contains(self, dato):                                 
        aux = self.head
        while aux != None:                                         #T(n) = C6*n
            if(aux.data == dato):                                  #C8 = 3
                return True                                        #C8.0 = 3 
            aux = aux.next                                         #C9 = 2
        return False                                               #C10 = 1
    
    """
    Complexity of search a data in the linked list:
    T(n) = C + C6*n 
    T(n) = C6*n                                       ---> Sum law 
    T(n) = n                                          ---> Product law
    O(n)  where n is the linked list length
    """
    
       

class main:
    lista = DoublyLinkedList()
    lista.add(1,0)
    lista.add(2,1)
    lista.add(3,2)
    lista.add(4,3)
    print(lista.contains(2))
    lista.delete(0)
    lista.add(5,3)
    lista.append(6)
    lista.delete(2)
    print(lista.contains(8))
    print(lista.get(0))
    print(lista.get(1))
    print(lista.get(2))
    print(lista.get(3))

