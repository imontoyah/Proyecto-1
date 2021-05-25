from huffman import HuffmanCoding
from fft import *
import numpy as np
from PIL import Image
from numpy import savetxt
from time import time 
from memory_profiler import profile


def load_img(n_archivo_csv):
    
        """This function loads the image from a matrix to a numpy´s matrix, with the purpose of reducing the memory consumption
        :type n_archivo_csv: matrix of pixels
    
        :rtype: a numpy´s matrix 
        """
        matriz_csv_imagen = np.loadtxt(open(n_archivo_csv, "rb"), delimiter=",").astype(int)

        return matriz_csv_imagen


def show_img(img_matrix):
    
    """Show_img makes a transformation to the matrix to modify the number of bits, then it shows the image with the method .show() of the library PIL
        :type img_matrix: numpy´s matrix 
    
        :rtype: Image in PNG format
    """
    imagenplot =  Image.fromarray(np.int32(img_matrix))
    imagenplot.show()

def main():

    """ In this function we read the folder healthy_cow where are store the csv files that contains the matrix of pixels of the images and we selected an specific file.
    At first, we applied a compression with FFT and it returns a csv file, which will be compress again using the huffman method and will return a binary file.
    Followed by this, we decompress the binary file with the huffman method and it returns a csv file that will be decompress with FFT.
    Finally, using the library PIL, we show the original imagen and the decompress image.

    :raises: file not found

    :rtype: Image in PNG format
    """
    directory_sick_cow = "/Users/isabella/Documents/Segundo Semestre/Estructura de Datos /Proyecto/ganado_enfermo_csv"
    directory_healthy_cow = "/Users/isabella/Documents/Segundo Semestre/Estructura de Datos /Proyecto/Entrega 3/Codigo/huffman-coding-master/Vacas_Enferma"
     
    directory = directory_healthy_cow
    cont = os.listdir(directory)

    matriz_csv_var = load_img(directory+'/'+cont[0])

    fft_compression(matriz_csv_var, 0.05)
    h = HuffmanCoding("compressFFT.csv")
    output_path = h.compress()
    print("Compressed file path: " + output_path)


    decom_path = h.decompress(output_path)
    print("Decompressed file path: " + decom_path)
    img_fft_descompress = fft_descompression(decom_path)


    show_img(matriz_csv_var)
    show_img(img_fft_descompress)


    savetxt('dataff.csv', matriz_csv_var, delimiter=',')

main()



