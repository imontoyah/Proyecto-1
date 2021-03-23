class Pila(object):
    
    def __init__(self):
        self.items=[]

    def apilar(self, dato): #REALIZA ACCIÓN DE APILAR
        self.items.append(dato)

    def desapilar(self): #SACA ELEMENTOS DE LA PILA
        if self.esta_vacia():
            return None
        else:
            return self.items.pop()

    def esta_vacia(self): #VERIFICA SI LA PILA ESTÁ VACIA
        if len(self.items)==0:
            return True
        else:
            return False
        
    def ver_pila(self): #VER ELEMENTOS DE LA PILA
        print(self.items)

class RPN():
    prefija = []
    pila = Pila()

    def __init__(self, prefija):
        self.prefija = prefija

    def rpn(self):
        elem_D = ""
        elem_Iz = ""

        for i in range(0,len(prefija)):
            if self.esOperador(self.prefija[i]):
                elem_D = self.pila.desapilar()
                if self.pila.esta_vacia() :
                    raise IndexError("Error, elemento faltante")
                else:
                    elem_Iz = self.pila.desapilar()
                    resultado = self.operar(elem_Iz,self.prefija[i],elem_D)
                    self.pila.apilar(resultado)
            else:
                self.pila.apilar(self.prefija[i])

        return self.pila.ver_pila()

    def esOperador(self,token):
        if(token == "+" or token == "-" or token == "*" or token == "/" or token == "%" or token == "**"):
            return True
        else: 
            return False

    def operar(self,elem_Iz,token,elem_D):
        a = float(elem_Iz)
        b = float(elem_D)

        if token == "+":
            return a + b
        elif token == "-":
            return a - b
        elif token == "*":
            return a * b
        elif token == "/":
            return a / b 
        elif token == "%":
            return a % b
        elif token == "**":
            return a ** b

prefija = ['6','5','-','4','+']
calculadora = RPN(prefija)
print(calculadora.rpn())
