import pandas as pd
import queue

datos1 = pd.read_csv('NOTAS ST0242.csv.txt')
datos2 = pd.read_csv('NOTAS ST0245.csv.txt')
datos3 = pd.read_csv('NOTAS ST0247.csv.txt')
final = pd.concat([datos1,datos2,datos3])

def consulta1():  #Dado un curso y un semestre mostrar todos los estudiantes y la nota final
        print("Ingrese el  curso y el semestre respectivamente")                                                #C1
        curso = str(input())                                                                                    #C2
        semestre = int(input())                                                                                 #C3

        filter1 = final[(final['Nom. Materia'] == curso) & (final['Semestre']==semestre)]                       #T1(n) = n  where n is the number of the rows
        print(filter1[['nombre','Nota Definitiva']])                                                            #C4

def consulta2(): #Dado un estudiante y semestre mostar que los cursos que matriculo y la nota final
        print("Ingrese el nombre del estudiante y el semestre")                                                 #C5
        nombre = str(input())                                                                                   #C6
        semestre = int(input())                                                                                 #C7

        filter1 = final[(final['nombre']==nombre) & (final['Semestre']==semestre)]                              #T2(n)= n where n is the number of the rows
        print(filter1[['nombre','Nom. Materia','Nota Definitiva']])                                             #C8

print("¿Qué tipo de colsulta quiere realizar?")                                                                 #C9
if str(input()) == 'consulta 1':                                                                                #C10
    print(consulta1())                                                                                          #C11
else:
    print(consulta2())                                                                                          #C12

"""
T(n) = C1 +C2 + C3 + n + C4 + C5 + C6 + n + C7 + C8 + C9 + C10 + C11 + C12
T(n) = n + n
O(n)
"""





