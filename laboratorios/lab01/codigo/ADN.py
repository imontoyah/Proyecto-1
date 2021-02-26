from time import time
import matplotlib.pyplot as plt 
import random 
import string
string.ascii_letters = "abcdefghijqlmnokrstuvwxyz"

def subsequence(x , y):
    i = len(x) #T(n,m) = C1 donde C1 = 2
    j = len(y) #T(n,m) = C2 donde C2 = 2
    if(i == 0 or j == 0): #T(n,m) = C3 where C3 = 4  /  T(p) = C3  where p = m + n
        return 0 
    elif(x[i-1] == y[j-1]): ##T(n,m) = C4 + T(n-1, m-1)  / T(p) = C4 + T(p-1) where p = m + n
        return 1 + subsequence(x[:i-1],y[:j-1]) 
    else:
        return max(subsequence(x[:i-1],y),subsequence(x,y[:j-1])) #T(n,m)= C5 + T(n-1, m) + T(n,m-1)  /  T(p) = C5 + T(p-1) + T(p-1) where p = m + n
"""
    Worst case:
    T(n,m)= C5 + T(n-1, m) + T(n,m-1) ,
    Recurrence equation solution : -T(n-1, m) - T(n, m-1) + T(n,m)
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
    string1 = ""
    string2 = ""
    for j in range(1, final):
        cadena1 += random.choice(string.ascii_letters)
        cadena2 += random.choice(string.ascii_letters)
    final = final + 1
    start=time()
    subsequence(string1,string2)
    fin = time()
    total=fin-start
    times.append(total)
plot(times,18,"Subsequence")


