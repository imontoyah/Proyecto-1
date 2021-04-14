
import scipy.sparse
import numpy as np
import os
from PIL import Image
from scipy.sparse import csr_matrix
from numpy import savetxt


def load_img(n_archivo_csv):
    matriz_csv_imagen = np.loadtxt(open(n_archivo_csv, "rb"), delimiter=",").astype(int)
    
    return matriz_csv_imagen


def fft_compression(image,percent):
    f = np.fft.fft2(image)
    fsort = np.sort(np.abs(f.reshape(-1)))
    
    thresh = fsort[int(np.floor((1-percent)*(len(fsort))))]
    ind = np.abs(f) > thresh
    Atlow = f * ind
    sparce_matrix = csr_matrix(Atlow)
    scipy.sparse.save_npz('datafft', sparce_matrix)
    
    return fsort

#This funtion code is contributed by http://databookuw.com/

def fft_descompression(file_compress):
    img_compress = scipy.sparse.load_npz(file_compress)
    fft_coef_thresh = img_compress.todense()
    img_descompress = np.fft.ifft2(fft_coef_thresh).real
    
    return img_descompress

#This funtion code is contributed by http://databookuw.com/

def show_img(img_matrix):
    imagenplot =  Image.fromarray(img_matrix)
    imagenplot.show()
    

directorio_vacas_enfermas = os.getcwd()+"/archivosCSV/ganado enfermo CSVs" 
directorio_vacas_sanas = os.getcwd()+"/archivosCSV/ganado sano CSVs"

directorio = directorio_vacas_sanas
contenido = os.listdir(directorio)

matriz_csv_var = load_img(directorio+'/'+contenido[1])

fsort = fft_compression(matriz_csv_var,0.05)

img_fft_descompress = fft_descompression('datafft'+'.npz')


show_img(matriz_csv_var)
show_img(img_fft_descompress)


savetxt('dataff.csv', matriz_csv_var, delimiter=',')



        



