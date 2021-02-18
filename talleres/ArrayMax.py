from time import time
import random
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
    
tiempo_inicial = time()
array_i = array_generator(95)
print(ArrayMax(array_i,95))
tiempo_final = time()
tiempo_total = tiempo_final - tiempo_inicial
print(tiempo_total)