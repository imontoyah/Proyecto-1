from LZW import LZW
import os

ganado_enfermo = os.getcwd()+"/archivosCSV/ganado enfermo CSVs/04be43ab919b6b22d950d3b59834f4a1.csv"   
ganado_sano=os.getcwd()+"/archivosCSV/ganado sano CSVs"

compressor = LZW('/Users/mimar/OneDrive - Universidad EAFIT/UNIVERSIDAD/SEGUNDO SEMESTRE/ESTRUCTURAS/PROYECTO/04be43ab919b6b22d950d3b59834f4a1.jpg')
img = compressor.compress()

decompressor = LZW('/Users/mimar/OneDrive - Universidad EAFIT/UNIVERSIDAD/SEGUNDO SEMESTRE/ESTRUCTURAS/PROYECTO/Entrega 3/CompressedFiles/04be43ab919b6b22d950d3b59834f4a1Compressed.lzw')
decompressor.decompress()
