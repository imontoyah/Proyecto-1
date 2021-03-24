from collections import deque
from queue import LifoQueue
---------------------- Atencion_en_un_bar_con_colas-----------------------
def barCola(n):
    my_queue = deque()
    
    for i in range(n):
        my_queue.append(input())
 
    for i in range(n):
        print ("Atendiendo a: "  + my_queue.popleft())
        
barCola(3)
------------------- Invertir_orden_de_una_pila--------------
stack = LifoQueue()
stack.put(1)
stack.put(2)
stack.put(3)
 
def inversoLista(stack):
    lista = LifoQueue()
    
    for i in range(stack.qsize()):
        n = stack.get()
        lista.put(n)
        
    for i in range(3):
        print(lista.get())
    
inversoLista(stack)
