from time import time
import random
import  matplotlib.pyplot as plt

def array_generator(len):
    array = [0] * len
    for i in range(len):
        array[i] = random.randrange(0,100)
    return array

def ArrayMax(arr,n):
    max = arr[n-1] #c1 = 1
    if n == 0: 
      return arr[0]
    if n != 0: #c2 = 1
      temp = ArrayMax(arr, n-1) #T(n)= c2 * T(n-1)
      if temp > max:
        max = temp
    return max  # T(n)= c2 * T(n-1)   T(n)= 1 + T(n-1)   O(n)

#Para graficarla
times = []

def plot(times,n,lab):
    plt.xlabel('Dimension del problema')
    plt.ylabel('Tiempo de complejidad')
    plt.plot(range(1,n),times,label=lab)
    plt.grid()
    plt.legend()
    plt.show()

for i in range(1001,1020):
    inicio=time()
    ArrayMax(array_generator(i), 1000)
    fin=time()
    total=fin-inicio
    times.append(total)
plot(times,20,"ArrayMax")
