from time import time 
import random
import matplotlib.pyplot as plt 

def rectangles(n):
    if(n<=2):
        return n
    return rectangles(n-1) + rectangles(n-2)

times = []

def plot(times,n,lab):
    plt.xlabel('Dimension del problema')
    plt.ylabel('Tiempo de complejidad')
    plt.plot(range(1,n),times,label=lab)
    plt.grid()
    plt.legend()
    plt.show()

for i in range(100,500):
    inicio=time()
    n = random.randrange(0,100)
    rectangles(n)
    fin=time()
    total=fin-inicio
    times.append(total)
plot(times,12,"Rectangles")
