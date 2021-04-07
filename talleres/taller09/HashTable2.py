dic = {'Google': 'Estados Unidos', 
        'La Locura': 'Colombia', 
         'Nokia': 'Finlandia',
          'Sony': 'Japon',}

#Punto 2
#Metodo para imprimir las empresas con su  determinado pais
def imprimirDic(dic):
    for key, value in dic.items():
        print("La empresa " + key, "queda en " + value)

#Punto 3
#Metodo para buscar en que pais se ubica una empresa determinada
def buscarEmpresa(key):
    if key in dic:
        print ("La empresa se encuentra ubicada en "+ dic[key])
    else:
        print ('No se encontro la empresa')

#Punto 4
#Metodo para obtener la key del dic
def get_key(val):
    for key, value in dic.items():
         if val == value:
             return key
    return "No existe la llave asociada a ese valor"

#Metodo para buscar que empresa se encuentra en un pais especifico   
def buscarPais(val):
    paises = dic.values()
    if val in paises:
        print ("En "+ val + " se encuentra " + get_key(val))               
    else:
        print ("No hay empresas en ese pais") 
        
imprimirDic(dic)
buscarEmpresa('Google')
buscarEmpresa('Motorola')
buscarPais('India')
buscarPais('Estados Unidos')

