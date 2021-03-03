
import math

def invertir(array):
    n = len(array)-1                           #c1=2
    for i in range(0, math.floor(n / 2)):      #T(n) = C2 + T(n/2)
            temp = array[i]
            array[i] = array[n]
            array[n] = temp
            n = n-1

    return array

arr = [] 
n = int(input("Ingrese un numero"))

while n != -1:                          #T(n) = C3 + T(n) 
    arr.append(n)
    n = int(input("Ingrese un numero")) 
    
print(arr)
print(invertir(arr))
