class Cola:
    def __init__(self):                           #C0, means O(1)
        self.items = []     

    def estaVacia(self):                           #C1, means O(1)
        return self.items == []

    def agregar(self, item):                       # C2, means O(1)
        self.items.insert(0,item)

    def avanzar(self):                             # C3, means O(1)
        return self.items.pop()

    def tamano(self):                              #C4, means O(1)
        return len(self.items)

class Banco:
    def __init__(self, s1, s2, s3, s4):            #C0, means O(1)
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4
    
    def get_fila1(self):                           #C1, means O(1)
        return self.s1
    
    def get_fila2(self):                           # C2, means O(1)
        return self.s2
    
    def get_fila3(self):                          # C3, means O(1)
        return self.s3
     
    def get_fila4(self):                          #C4, means O(1)
        return self.s4

class main:

    def is_empty(data_structure):                       #C1, means O(1)
        if data_structure:                              #C2
            return False                                #C3
        else:
            return True                                 #C4
           
    def atender(banco, fila):
        while(banco.get_fila1().estaVacia()!=True or banco.get_fila2().estaVacia()!=True or banco.get_fila3().estaVacia()!=True or banco.get_fila4().estaVacia()!=True):  # C + n, means O(n) where n is the most large file`s length
            if(banco.get_fila1().estaVacia() != True):                                    #C5
                fila.agregar(banco.get_fila1().avanzar())                                 #C5.0
            if(banco.get_fila2().estaVacia() != True):                                    #C6                                                                                      
                fila.agregar(banco.get_fila2().avanzar())                                 #C6.0
            if(banco.get_fila3().estaVacia() != True):                                    #C7
                fila.agregar(banco.get_fila3().avanzar())                                 #C7.0
            if(banco.get_fila4().estaVacia() != True):                                    #C8
                fila.agregar(banco.get_fila4().avanzar())                                 #C8.0
        return fila                                                                       #C9
    
    def imprimirCajero(queue):                             
        cajero1 = "cajero 1 esta atendiendo a: "                                          #C10
        cajero2 = "cajero 2 esta atendiendo a: "                                          #C10.0
        for i in range(queue.tamano()):                                                   #C11+m, means O(m) where m is the queue's length
            if(i%2==0):                                                                   #C12
                print(cajero1 + queue.avanzar())                                          #C12.0
            else:
                print(cajero2 + queue.avanzar())                                          #C13
    

    s1 = Cola()
    s1.agregar("Isabella")
    s1.agregar("Felipe")
    s2 = Cola()
    s2.agregar("Kevin")
    s2.agregar("Maria")
    s3 = Cola()
    s3.agregar("Claudia")
    s4 = Cola()
    s4.agregar("Luisa")
    s4.agregar("Bayron")
    
    banco = Banco(s1, s2, s3, s4)
    fila = Cola()
            
    orden = atender(banco, fila)
    imprimirCajero(orden)

"""
The complexity for the worst case of Cajeros is:
T(n, m) = C + n + m                       ---> Sum law
T(n,m) = n+m  , let's p = m+n
T(p) = p
O(p),  where p is n+m
"""
