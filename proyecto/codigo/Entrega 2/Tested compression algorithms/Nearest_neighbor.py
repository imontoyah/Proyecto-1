from PIL import Image 
import os
import matplotlib.pyplot as plt
import numpy as np 
from numpy import savetxt

#para que funcione multicomputador sin tener que cambiar la ruta
ganado_enfermo = os.getcwd()+"/archivosCSV/ganado enfermo CSVs"   
ganado_sano=os.getcwd()+"/archivosCSV/ganado sano CSVs"

def matriz_csv(n_archivo_csv):
    matriz_csv_imagen = np.loadtxt(open(n_archivo_csv, "rb"), delimiter=",").astype(int)
    return matriz_csv_imagen

def NN_interpolation(img,newH,newW):
    oldH, oldW= np.array(img).shape
    newimg = np.zeros((newH,newW),dtype=np.uint8)
    for i in range(newH-1):
        for j in range(newW-1):
            oldx = round(i*(oldH/newH))
            oldy = round(j*(oldW/newW))
            newimg[i,j] = img[oldx,oldy]
    return newimg
#This funtion code is contributed by https://www.programmersought.com/article/36124682709/#:~:text=The%20nearest%20neighbor%20interpolation%20method%20adds%20the%20value%20of%20the,significantly%2C%20often%20containing%20jagged%20edges.

def compression(image):
    newHgth,newWgt = np.array(image).shape
    compress = NN_interpolation(image,round(newHgth/2),round(newWgt/2))
    return compress

def decompression(image):
    newHgth,newWgt = np.array(image).shape
    final_interpolation = NN_interpolation(image,newHgth*2,newWgt*2)
    return final_interpolation

directorio = ganado_sano
contenido = os.listdir(directorio)
original_image = matriz_csv(directorio+'/'+contenido[1])

image_orig = Image.fromarray(original_image)
img_compress = compression(original_image)
finalC = Image.fromarray(img_compress)
img_descompress = decompression(img_compress)
finalD = Image.fromarray(img_descompress)

image_orig.show()
finalC.show()
finalD.show()

savetxt('dataOriginal.csv', original_image, delimiter=',')
savetxt('dataNN.csv',finalC, delimiter=',')
