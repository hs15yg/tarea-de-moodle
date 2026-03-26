lista =[]

n = int(input("ingrese el tamano de la lista: "))
m = int(input("ingrese el numero de la pocision: "))

for i in range(n):
    entrada = input("ingrese una letra: ")
    lista.append(entrada)
    
    for i in range(m):
        lista2 = input("ingrese el letra de la sublista: ")
        lista.insert(0,lista2)
    