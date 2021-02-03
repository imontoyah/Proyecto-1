def euclides(a,b):
    minimo = min(a,b)
    maximo = max(a,b)

    if minimo == 0:
        return maximo

    elif minimo == 1:
        return 1
        
    else :
        return euclides(minimo, maximo % minimo)