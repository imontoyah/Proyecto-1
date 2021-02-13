import numpy as np
import glob
from PIL import Image

def matriz_csv(n_archivo_csv):
    matriz_csv_image = np.loadtxt(open(n_archivo_csv, "rb"), delimiter=",").astype(int)

    return matriz_csv_image

#Para probar si lee el archivo bien
#Imprime la imagen
csv_files = glob.glob('*.csv')
matriz_csv_var = matriz_csv(csv_files[0])
image = Image.fromarray(matriz_csv_var)
image.show()
