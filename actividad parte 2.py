lista= []

for i in range(5):
    producto= input("Ingrese el nombre del producto: ")
    lista.append(producto)
lista_ordenada= sorted(lista)
print("Lista de productos ordenada alfabéticamente:", lista_ordenada)

while True:
    producto_aeliminar= input("Ingrese el nombre del producto que desea eliminar: ")
    if producto_aeliminar in lista_ordenada:
        lista_ordenada.remove(producto_aeliminar)
        print("Producto eliminado. Lista actualizada:", lista_ordenada)
    else:
        print("El producto no se encuentra en la lista.")