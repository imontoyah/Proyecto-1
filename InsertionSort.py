
from time import time 
import random
import matplotlib.pyplot as plt 

def array_generator(n):
    array = [0] * n
    for i in range(n):
        array[i] = n-i
    return array

def Insertion(arr):
    for i in range(1,len(arr)): #C1*n
        j=i;#n*C2
        while j > 0 and (arr[j-1]>arr[j]):#C3* n(n+1)/2
            temp=arr[j]#C4* n(n+1)/2
            arr[j]= arr[j-1]#C5* n(n+1)/2
            arr[j-1]=temp #C6* n(n+1)/2
            j= j-1 #C7* n(n+1)/2
    return arr #C8 * n(n+1)/2
    """
    T(n)=C1*n+n*C2+C3*n(n+1)/2+C4*n(n+1)/2+C5*n(n+1)/2+C6*n(n+1)/2+C7*n(n+1)/2
    T(n)=(n(n+1)/2*)(C3+C4+C5+C6)+C'-->Regla de las sumas y producto
    T(n)=(n^2+n)*1/2*C'---->Se quita la suma interna
    T(n)=n^2+n---->Se quitan los productos y la suma interna
    T(n)=O(n^2)
"""
    for i in range(len(arr)):
        print(arr[i])

"""
T(n) = 
"""

times = []

def plot(times,n,lab):
    plt.xlabel('Dimension del problema')
    plt.ylabel('Tiempo de complejidad')
    plt.plot(range(1,n),times,label=lab)
    plt.grid()
    plt.legend()
    plt.show()
   #plot(x, y, "o-")

for i in range(100,1000,100):
    array = array_generator(random.randrange(0,100))
    inicio=time()
    Insertion(array)
    fin=time()
    total=fin-inicio
    times.append(total)
plot(times,10,"InsertionSort")