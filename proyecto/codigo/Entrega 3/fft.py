
import scipy.sparse
import numpy as np
import os
from PIL import Image
from scipy.sparse import csr_matrix
from numpy import savetxt
from huffman import *


def load_img(n_archivo_csv):
    matriz_csv_imagen = np.loadtxt(open(n_archivo_csv, "rb"), delimiter=",").astype(int)
    
    return matriz_csv_imagen


def fft_compression(image,percent):
    f = np.fft.fft2(image)
    fsort = np.sort(np.abs(f.reshape(-1)))
    
    thresh = fsort[int(np.floor((1-percent)*(len(fsort))))]
    ind = np.abs(f) > thresh
    Atlow = f * ind 
    savetxt('compressFFT.csv', Atlow, delimiter = ',')
    
    return Atlow

"""
fft_compression receives a matrix of an image in grayscale and a percent of compression in order to
apply the FFT to the image matrix, then sort those values from the transformation and threshold the
select percent we want to keep
"""
#This funtion code is contributed by http://databookuw.com/

def fft_descompression(file_compress):
    fft_coef_thresh = np.loadtxt(open(file_compress, "r"), dtype = np.complex, delimiter=",")
    img_descompress = (np.fft.ifft2(fft_coef_thresh).real)
    
    return img_descompress,fft_coef_thresh

"""
fft_descompression receives a matrix of Fourier coefficients, the it load that matrix, apply the inverse
FFT in order to get back to the pixels domain, and only take the real part.
"""

