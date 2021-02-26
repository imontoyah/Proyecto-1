def rectangulos(n):
    if(n<=2):
        return n
    return rectangulos(n-1) + rectangulos(n-2)

print(rectangulos(5))