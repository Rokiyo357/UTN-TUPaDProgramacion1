lista =[]

import random

for i in range(15):
    numeros= random.randint(1,100)
    lista.append(numeros)

print ("Lista de números generados:", lista)

lista_pares = []
lista_impares = []

for numero in lista:
    if numero % 2 == 0:
        lista_pares.append(numero)
    else: 
        lista_impares.append(numero)

print ("Lista de números pares generados:", lista_pares)
print ("Lista de números impares generados:", lista_impares)

print(("cantidad de numeros pares generados:", len(lista_pares ) ))
print (("cantidad de numeros impares generados:", len(lista_impares) ))