productos = []
while True: 
  nombre = input("Ingrese su nombre: ")
  if nombre.strip():
    if nombre.isalpha():
      break
    else:
        print("El nombre debe contener solo letras y sin espacios. Por favor, intente nuevamente.")
while True:
   cantidad = input("Ingrese la cantidad de productos: ")
   if cantidad.isdigit() and int(cantidad) > 0:
      cantidad = int(cantidad)
      break
   else:
        print("La cantidad debe ser un número entero positivo. Por favor, intente nuevamente.")
  
# Lista para almacenar (nombre, precio, descuento)
productos = []

for i in range(cantidad):
    print(f"\n--- Producto {i + 1} ---")
    
    # Validar nombre
    while True:
        producto = input(f"Ingrese el nombre del producto {i + 1}: ").strip()
        if not producto:
            print("El nombre no puede estar vacío.")
        elif producto.replace(" ", "").isalpha():
            break
        else:
            print("El nombre solo debe contener letras (sin números ni símbolos).")
    
    # Validar precio
    while True:
        try:
            precio = float(input(f"Ingrese el precio del producto {i + 1}: "))
            if precio > 0:
                precio = round(precio, 2)
                break
            else:
                print("El precio debe ser un número positivo.")
        except ValueError:
            print("Debe ingresar un número válido.")
    
    # Validar descuento
    while True:
        tiene_descuento = input(f"¿El producto {i + 1} tiene descuento? (Si/No): ").strip().lower()
        if tiene_descuento == "si":
            descuento = round(precio * 0.10, 2)  # 10% de descuento
            break
        elif tiene_descuento == "no":
            descuento = 0
            break
        else:
            print("Respuesta inválida. Responda 'Si' o 'No'.")
    
    # Guardar producto como tupla (nombre, precio, descuento)
    productos.append((producto, precio, descuento))

# Mostrar resumen
print(f"\n{'='*50}")
print(f"RESUMEN DE COMPRA PARA: {nombre.upper()}")
print(f"{'='*50}")

# Mostrar cada producto
print("\nDetalle de productos:")
print("-" * 50)
for idx, (nombre_prod, precio, descuento) in enumerate(productos, 1):
    precio_con_descuento = precio - descuento
    print(f"{idx}. {nombre_prod:15} | ${precio:8.2f} | Descuento: ${descuento:6.2f} | Total: ${precio_con_descuento:8.2f}")
print("-" * 50)

# para el calculo de totales
total_sin_descuento = sum(precio for _, precio, _ in productos)
total_descuento = sum(descuento for _, _, descuento in productos)
total_a_pagar = total_sin_descuento - total_descuento

print(f"Cantidad de productos: {cantidad}")
print(f"Total sin descuento: ${total_sin_descuento:.2f}")
print(f"Total descuento: ${total_descuento:.2f}")
print(f"{'='*50}")
print(f"TOTAL A PAGAR: ${total_a_pagar:.2f}")
print(f"{'='*50}")
