datos=[1,2,5,3,7,1,9,5,3]
lista = []

for i in range(len(datos)):
    if datos[i] not in lista:
        lista.append(datos[i])

print("Lista sin elementos repetidos:", lista)
