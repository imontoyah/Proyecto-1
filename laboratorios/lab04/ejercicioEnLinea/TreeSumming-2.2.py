from pyparsing import OneOrMore, nestedExpr
from collections import Counter

def treeSum(value, tree):
    if not tree:
        return value == 0
    v1 = value - int(tree[0]) # hace la resta recursiva 
    for position in tree[1:]:
        if treeSum(v1, position):
            return True
    return False

inFile = open('input.txt')
openBrac = 0
currExp = ''
for line in inFile:
    line.strip()  #Remueve los espacios
    lineCounter = Counter(list(line))  # Funcion de tablas hash que cuenta los elementos y los guarda como llaves de un diccionario y sus repeticiones como un valor
    if '(' not in lineCounter:
        lineCounter['('] = 0
    if ')' not in lineCounter:
        lineCounter[')'] = 0
    openBrac += lineCounter['('] - lineCounter[')']
    currExp += line
    if openBrac != 0:
        continue
    else:
        row = currExp.split()#la fila de datos que representa el arbol (dividida)
        currExp = ''
        openBrac = 0
        objective = int(row[0]) #el numero objetivo
        expression = ''.join(row[1:]) #tiene los numeros
        expression = OneOrMore(nestedExpr()).parseString(expression)
        if treeSum(objective, expression[0]):
            print ('yes')
        else:
            print ('no')
