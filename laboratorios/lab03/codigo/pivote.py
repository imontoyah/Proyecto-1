import math

def pivote(arr):
    sumL = 0                                 #C1
    sumR = 0                                 #C2
    auxArr = [0]*len(arr)                    #C3
    sumAux = 0                               #C4
    
    for i in range(len(arr)):                #C5*n , means O(n) where n is the array's length
        auxArr[i] = arr[i]+sumAux            #C5.0
        sumAux += arr[i]                     #C5.1
    
    minimum = math.inf                       #C6
    for j  in range(1, len(arr)):            #C7*(n-1) , means O(n) where n is the array's length
        sumL = auxArr[j-1]                   #C7.0
        sumR = auxArr[len(auxArr)-1] - auxArr[j]  #C7.1
        difference = abs(sumL - sumR)             #C7.2
        if(difference<minimum):                   #C7.3
            minimum = difference                  #C7.5
            pivote = j                            #C7.6
    
    return pivote                                 #C8

"""
Complexity for the worst case
T(n) = C + C5*n  + C7*(n-1)
T(n)  = C5*n  + C7*(n-1)       --->Sum law
T(n) = n + (n-1)               --->Product law
T(n) = n                       --->Sum law
O(n) where n is the array's length
"""

arr = [10,20,5,3,30]
print(pivote(arr))

arr1 = [16,4,3,7,20,1]
print(pivote(arr1))

            
 
 

