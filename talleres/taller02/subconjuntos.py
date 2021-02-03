def subconjuntos(s):
    subconjuntosBase("", s)

def subconjuntosBase(base, s):
    if len(s) == 0:
        print(base)
    else:
        x = s[1:]
        subconjuntosBase(base+ s[:1], x)
        subconjuntosBase(base, x)

print(subconjuntos("abcd"))
