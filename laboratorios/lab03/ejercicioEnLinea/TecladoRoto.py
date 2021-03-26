from collections import deque    
class TecladoRoto():
    def teclado(self,string):
        texto = deque()                                                                 #C1
        acc = 0     #0 - agregar al final / 1 - agrgar al inicio                        #C2
        aux = ''
        stringFinal = ''                                                                        #C3
        for i in range (len(string)):                                                   #T1(n) = n  - - > where n is the string´s length
            if string[i] != '[' and string[i] != ']':                                   #C4
               aux = aux + string[i]                                                    #C5
            if string[i] == '[':                                                        #C6
                if acc == 0:                                                            #C7
                    texto.append(aux)                                                   #T2(n) = m - - > where m is the List´s length
                    aux = ''                                                            #C8
                else:
                    texto.insert(0,aux)                                               #C9
                    aux = ''                                                            #C10
                acc = 1                                                                 #C11
            if string[i] == ']':                                                        #C12
                if acc == 1:                                                            #C13
                    texto.insert(0,aux)                                               #C15
                    aux = ''                                                            #C16
                acc = 0                                                                 #c17
            if i == len(string)-1:                                                      #C18
                if acc == 0:                                                            #C19
                    texto.append(aux)                                                   #T3(n) = m - - > where m is the List´s length
                    aux = ''                                                            #C20
                else:
                    texto.insert(0,aux)                                               #C21           
                    aux = '' 
                    
                for i in range(len(texto)):
                    stringFinal += texto.popleft()

        return stringFinal                                                    #C22
                                                                                  #T4(n) = m - - > where m is the List´s length
    
teclado = TecladoRoto()
print(TecladoRoto.teclado(TecladoRoto,'This_is_a_[Beiju]_text'))

"""
1.T(n) = C + C23*m  + C3.0*n 
2.T(n) = C23*m  + C3.0*n                     ---> Sum law,   m=n
3.T(n)= (C23 + C3.0)*n                       ---> Common factor
4.T(n) = n                                   ---> Product law 
O(n)  where n is the list's length 
"""
