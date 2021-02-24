from time import time 
import random
import matplotlib.pyplot as plt 

def array_generator(len):
    array = [0] * len
    for i in range(len):
        array[i] = random.randrange(0,100)
    return array

def tablas_multiplicar(n):
    for i in range(0, n+1): #c1*n
        for j in range(0, 10): #c2*n*n
            multiplicacion = i*j #c3*n*n
            print( str(i)+"*"+str(j)+"="+str(multiplicacion))  #c4*n*n
            
#T(n)=C1*n+C2*n^2+C3*n^2+C4*n^2
#T(n)=n^2*(C1+C3+C4)+C'-->Regla de las sumas y producto
#T(n)=n^2*C'---->Se quitan los productos y se simplifica la suma
#T(n)=O(n^2)

times = [ ]

def plot(times,n,lab):
    plt.xlabel('Dimension del problema')
    plt.ylabel('Tiempo de complejidad')
    plt.plot(range(1, n), times,label=lab)
    plt.grid()
    plt.legend()
    plt.show()

for i in range(0, 110,5):
    inicio=time()
    tablas_multiplicar(i)
    fin=time()
    total=fin-inicio
    times.append(total)
plot(times, 23, "Tablas de multiplicar")