import os
import sys
import numpy as np
import pandas as pd

#para que funcione multicomputador sin tener que cambiar la ruta
ganado_enfermo = os.getcwd()+"/archivosCSV/ganado enfermo CSVs"   
ganado_sano=os.getcwd()+"/archivosCSV/ganado sano CSVs"

def leer_archivos(ruta):
    fille = os.listdir(ruta)
    for i in range(len(fille)):
        direccion = ruta +"/"+ fille[i]
        data = pd.read_csv(direccion,header=None)
        data_array = np.asarray(data)
        print(data_array)

#Llamado a la funcion
leer_archivos(ganado_enfermo)
