import pandas as pd
import BinaryTree as bt

class Persona:
    
    def __init__(self, name, lastName, phone):
        self.name = name
        self.lastName = lastName
        self.phone = phone
        self.data = name +' '+ lastName + ' ' + phone

    
    def toString(self):
        print(self.name, self.lastName, self.phone)
        

class main:
    datos = pd.read_csv("/Users/isabella/Documents/Segundo Semestre/Estructura de Datos y Algoritmos/Talleres/Códigos/Taller 10/personas-en-situacion-de-vulnerabilidad.csv")
    datosLimpios = datos.drop(["MI", "Agency", "Room", "Building"], axis = 1)
    arbol = bt.BinaryTree()

    for i in range(len(datosLimpios)):
        #print(datosLimpios["FirstName"].values[i], datosLimpios["LastName"].values[i], datosLimpios["PhoneNumber"].values[i])
        person = Persona(datosLimpios["FirstName"].values[i], datosLimpios["LastName"].values[i], datosLimpios["PhoneNumber"].values[i])
        arbol.insertar(person.data)
        
    arbol.borrar("wanda 301-504-7271 \n")    
    arbol.imprimir()
    print(arbol.buscar('vivian brooks 301-504-1758'))
    print(arbol.buscar('Isabella Montoya 314-816-6711'))
    print(arbol.dibujar())


        


        

