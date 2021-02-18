#para python:
from time import time
 
#codigo a calcular
def groupSum_aux(list, start, target):
    if start < len(list): #C1
        if target == 0: #C2
            return True #C3
        else:
            return groupSum_aux(list,start+1, target) or groupSum_aux( list,start+1, target-list[start]) #T(n) = T(n-1) + T(n-1)  O(2a la n)

def groupSum(list, target):
    return groupSum_aux(list, 0, target)
 
inicio = time()
print(groupSum([354,789,425,7646,546,821,23665,41561,7165,1651,544,3252,46,5465,67687,4465,741,2884,2583,544,64,5165,544,645,7586,74123,698,241,321,7123],83902002345))
fin = time()
total = fin-inicio
print(total)