from collections import deque    
class TecladoRoto():

    def teclado(self,string):
        texto = deque()                                                                 #C1
        acc = 0     #0 - agregar al final / 1 - agrgar al inicio                        #C2
        aux = ''                                                                        #C3
        for i in range (len(string)):                                                   #C3.0*n  - - > where n is the string´s length
            if string[i] != '[' and string[i] != ']':                                   #C4
               aux = aux + string[i]                                                    #C5
            if string[i] == '[':                                                        #C6
                if acc == 0:                                                            #C7
                    texto.append(aux)                                                   #C7.0 - - > because append in a LinkedList is a constant
                    aux = ''                                                            #C8
                else:
                    texto.extendleft(aux)                                               #C9
                    aux = ''                                                            #C10
                acc = 1                                                                 #C11
            if string[i] == ']':                                                        #C12
                if acc == 1:                                                            #C13
                    texto.extendleft(aux)                                               #C15
                    aux = ''                                                            #C16
                acc = 0                                                                 #c17
            if i == len(string)-1:                                                      #C18
                if acc == 0:                                                            #C19
                    texto.append(aux)                                                   #C19.0  - - > because append in a LinkedList is a constant
                    aux = ''                                                            #C20
                else:
                    texto.extendleft(aux)                                               #C21           
                    aux = ''                                                            #C22
        return (texto)                                                                  #C23*m - - > where m is the List´s length
    
teclado = TecladoRoto()
print(TecladoRoto.teclado(TecladoRoto,'asd[gfh[[dfh]hgh]fdfhd[dfg[d]g[d]d'))
"""
1.T(n) = C + C23*m  + C3.0*n 
2.T(n) = C23*m  + C3.0*n                     ---> Sum law,   m=n
3.T(n)= (C23 + C3.0)*n                       ---> Common factor
4.T(n) = n                                   ---> Product law 
O(n)  where n is the list's length 
"""
