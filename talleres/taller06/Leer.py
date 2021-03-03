
import math

def invertir(array):
    n = len(array)-1                           #c1=2
    for i in range(0, math.floor(n / 2)):      #T(n) = C2 + (n/2)
            temp = array[i]
            array[i] = array[n]
            array[n] = temp
            n = n-1

    return array

arr = []                                 # C3
n = int(input("Ingrese un numero"))

while n != -1:                          # T(n) = C4 + (n) ,   --> T(n) = C4 + n*n
    arr.append(n)                       # T(n) = (n)          --> T(n) = C4 + n^2
    n = int(input("Ingrese un numero")) 
    
print(arr)                             #C3
print(invertir(arr))                   # T(n) = C2 + (n/2)   , "Complejidad de la funcion invertir"

"""
Complejidad total
T(n) = C2 + n/2 + C4 + n^2
T(n) = n/2 + n^2   ---> Regla de la suma
T(n) = n^2         ---> Como se estan suma, lo que hago es tomar el caso que me da una mayor complejidad
O(n^2) 
"""
