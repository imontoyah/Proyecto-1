from pyparsing import OneOrMore, nestedExpr
from collections import Counter
def treeSum(value, tree):
    if not tree:                            #O(1)
        return value == 0                   #O(1)
    v1 = value - int(tree[0])               #O(1)
    for position in tree[1:]:               #O(n) , where n is the number of nodes in the binary tree
        if treeSum(v1, position):           #O(1)
            return True                     #O(1)
    return False                            #O(1)
    
inFile = open('input.txt')                  #O(1)
openBrac = 0                                #O(1)
currExp = ''                                #O(1)
for line in inFile:                         #O(m) , where m is the number of rows in the txt file
    line.strip()                            #O(1)  - Remove the spaces
    lineCounter = Counter(list(line))       #O(1) - Funcion de tablas hash que cuenta los elementos y los guarda como llaves de un diccionario y sus repeticiones como un valor
    if '(' not in lineCounter:              #O(1)
        lineCounter['('] = 0                #O(1)
    if ')' not in lineCounter:              #O(1)
        lineCounter[')'] = 0                #O(1)
    openBrac += lineCounter['('] - lineCounter[')']  #O(1)
    currExp += line                         #O(1)
    if openBrac != 0:                       #O(1)
        continue                            #O(1)
    else:
        row = currExp.split()               #O(1) - #a fila de datos que representa el arbol (dividida)
        currExp = ''                        #O(1)
        openBrac = 0                        #O(1)
        objective = int(row[0])             #O(1) -  el numero objetivo
        exp = ''.join(row[1:])              #O(1) -  tiene los numeros
        exp = OneOrMore(nestedExpr()).parseString(exp)  #O(1)
        # print value, exp
        if treeSum(objective, exp[0]):       #O(1)
            print ('yes')                    #O(1)
        else:
            print ('no')                     #O(1)
