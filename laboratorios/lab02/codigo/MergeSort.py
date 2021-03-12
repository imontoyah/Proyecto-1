from time import time 
import random
import matplotlib.pyplot as plt 
 
def array_generator(n):
    array = [0] * n
    for i in range(n):
        array[i] = n-i
    return array
 
def mergeSort(arr):   
    if len(arr) > 1:              # O(1)
        mid = len(arr)//2         # O(1)
        L = arr[:mid]             # O(1)
        R = arr[mid:]             # O(1)
 
        mergeSort(L)              # 1. O(log(n))
        mergeSort(R)              # O(log(n))
        i = j = k = 0             # O(1)
 
        while (i < len(L) and j < len(R)):   # O(log(n))
            if L[i] < R[j]:                  # O(1)
                arr[k] = L[i]                # O(1)
                i += 1                       # O(1)
            else:
                arr[k] = R[j]                # O(1)
                j += 1                       # O(1)
            k += 1                           # O(1)

        while i < len(L):          # 2. O(n)
            arr[k] = L[i]          # O(1)
            i += 1                 # O(1)
            k += 1                 # O(1)
        while j < len(R):          # O(n)
            arr[k] = R[j]          # O(1)
            j += 1                 # O(1)
            k += 1                 # O(1)
""" 
Complexity for the worst case
1. O(logn + 1) ---> (logn + 1) for a given n 
2. O(n) + O(1) = O(n) --->   (cn)

--> Complexity is (logn + 1)*(cn)
O(n*log(n))  where n is the array`s length
"""
 
 
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
 
 
times = []
 
def plot(times,n,lab):
    plt.xlabel('Dimension del problema')
    plt.ylabel('Tiempo de complejidad')
    plt.plot(range(1,n),times,label=lab)
    plt.grid()
    plt.legend()
    plt.show()
 
for i in range(1000,12401,600):
    array = array_generator(i)
    inicio=time()
    mergeSort(array)
    fin=time()
    total=fin-inicio
    times.append(total)
plot(times,21,"MergeSort")