def hanoi(n, origen,final,intermedio):
    if n == 1:
        print("De "+origen+" "+"Hasta "+final)
    else:
        hanoi(n-1,origen,intermedio,final)
        print("De "+origen+" "+"Hasta "+final)
        hanoi(n-1,intermedio,final,origen)

hanoi(3,"A", "C", "B")