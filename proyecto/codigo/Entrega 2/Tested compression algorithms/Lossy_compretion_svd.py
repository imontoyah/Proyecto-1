
import numpy as np
import os
from PIL import Image
from numpy import savetxt


def load_img(n_archivo_csv):
    matriz_csv_imagen = np.loadtxt(open(n_archivo_csv, "rb"), delimiter=",").astype(int)
    
    return matriz_csv_imagen

def compression_svd(x):
    
    U, S, V = np.linalg.svd(x,full_matrices=False)
    aux = 0
    suma_s = np.cumsum(S)/np.sum(S)
    for i in suma_s:
        if i >= 0.5:
            r = int(aux)
            break
            
        aux = aux + 1
      
    Ur = U[:,:r]
    Sr = S[:r]
    Vr = V[:r,:]
    savetxt('dataur.csv', Ur, delimiter=',')
    savetxt('datasr.csv', Sr, delimiter=',')
    savetxt('datavr.csv', Vr, delimiter=',')
    
    
def descompression_svd(ur,sr,vr):
    Ur = np.loadtxt(open(ur, "rb"), delimiter=",")
    Sr = np.loadtxt(open(sr, "rb"), delimiter=",")
    Vr = np.loadtxt(open(vr, "rb"), delimiter=",")
    
    X_aprox = Ur * Sr @ Vr
    X_aprox = X_aprox.astype(int)
    
    return X_aprox

def show_img(img_matrix):
    imagenplot =  Image.fromarray(img_matrix)
    imagenplot.show()

directorio_vacas_enfermas = os.getcwd()+"/archivosCSV/ganado enfermo CSVs" 
directorio_vacas_sanas = os.getcwd()+"/archivosCSV/ganado sano CSVs"

directorio = directorio_vacas_sanas
contenido = os.listdir(directorio)
matriz_csv_var = load_img(directorio+'/'+contenido[1])

compression_svd(matriz_csv_var)

X_aprox = descompression_svd('dataur.csv', 'datasr.csv', 'datavr.csv')


show_img(matriz_csv_var)
show_img(X_aprox)

savetxt('datafff.csv', matriz_csv_var, delimiter=',')

