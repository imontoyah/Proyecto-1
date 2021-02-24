from time import time 
import random
import matplotlib.pyplot as plt 
 
def array_generator(len):
    array = [0] * len
    for i in range(len):
        array[i] = random.randrange(0,100)
    return array
 
def sumaArray(arr): 
    suma = 0 #c1
    for i in range(0,len(arr)): #c2*n 
        suma = suma + arr[i] #c3 * n 
    print(suma) #c4
    
    #T(n) = c1 + c2*n + c3*n + c4
    #T(n) = n*(c2+c3)
    #T(n) = n*c
    #T(n) = O(n)
 
times = []
 
def plot(times,n,lab):
    plt.xlabel('Dimension del problema')
    plt.ylabel('Tiempo de complejidad')
    plt.plot(range(1,n),times,label=lab)
    plt.grid()
    plt.legend()
    plt.show()
 
for i in range(0,10000,500):
    array = array_generator(i)
    inicio=time()
    sumaArray(array)
    fin=time()
    total=fin-inicio
    times.append(total)
plot(times,21,"SumaArray")