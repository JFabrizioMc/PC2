def menor_en_arreglo():
    n1 = int(input("Ingrese el primer numero\n"))
    n2 = int(input("Ingrese el segundo numero\n"))
    n3 = int(input("Ingrese el tercer numero\n"))
    n4 = int(input("Ingrese el cuarto numero\n"))
    n5 = int(input("Ingrese el quinto numero\n"))
    arreglo = [n1,n2,n3,n4,n5]
    
    if n1 < n2 and n1 < n3 and n1 < n4 and n1 < n5:
        menor = print("Menor numero del arreglo ", arreglo,"es",n1)
    elif n2 < n1 and n2 < n3 and n2 < n4 and n2 < n5:
        menor = print("Menor numero del arreglo ", arreglo,"es",n2)
    elif n3 < n1 and n3 < n2 and n3 < n4 and n3 < n5:
        menor = print("Menor numero del arreglo ", arreglo,"es",n3)
    elif n4 < n1 and n4 < n3 and n4 < n2 and n4 < n5:
        menor = print("Menor numero del arreglo ", arreglo,"es",n4)
    elif n5 < n1 and n5 < n3 and n5 < n4 and n5 < n2:
        menor = print("Menor numero del arreglo ", arreglo,"es",n5)
    
    return menor

rpta = menor_en_arreglo()
print (rpta)





