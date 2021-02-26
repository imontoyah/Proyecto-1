from time import time
import matplotlib.pyplot as plt 
import random 
import string
string.ascii_letters = "abcdefghijqlmnokrstuvwxyz"

def subsecuencia(x , y):
    i = len(x) #c1
    j = len(y)  #c2
    if(i == 0 or j == 0): #c3 = 4
        return 0 #c5 = 1
    elif(x[i-1] == y[j-1]): #c6 = 2
        return 1 + subsecuencia(x[:i-1],y[:j-1]) # T(n)= c4 + T(n-1)
    else:
        return max(subsecuencia(x[:i-1],y),subsecuencia(x,y[:j-1])) #T(n)= c5 + T(n-1) + T(n-1)
"""
    T(n)= c5 + T(n-1) + T(n-1)
    Recurrence equation solution : c5 (2^n-1)+c1 2^n-1
    O(2^n)

"""

times = []

def plot(times,n,lab):
    plt.xlabel('Problem dimensions')
    plt.ylabel('Complexity time')
    plt.plot(range(1,n),times,label=lab)
    plt.grid()
    plt.legend()
    plt.show()

final = 1
for i in range (1,18):
    cadena1 = ""
    cadena2 = ""
    for j in range(1, final):
        cadena1 += random.choice(string.ascii_letters)
        cadena2 += random.choice(string.ascii_letters)
    final = final + 1
    inicio=time()
    subsecuencia(cadena1,cadena2)
    fin = time()
    total=fin-inicio
    times.append(total)
plot(times,18,"Subsecuence")


