import random
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
letras='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numero_secreto = random.randint(1, 3)
contador_veces_que_se_uso_abrir_cerradura=0
while True:
    nombre_agente= input("Ingrese su nombre de agente: ")
    if nombre_agente.strip():
        if nombre_agente.isalpha():
            break
        else:
            print("El nombre debe contener solo letras y sin espacios. Por favor, intente nuevamente.")
while cerraduras_abiertas < 3 and not alarma and tiempo > 0:
    print(f"\n{'='*50}")
    print("bienvenido agente", nombre_agente)
    print(f"\n{'='*50}")
    print("1. Abrir cerradura")
    print("2. Hackear panel")
    print("3. descansar")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
       
            if energia >= 41:
             energia -= 20
             tiempo -= 2
             cerraduras_abiertas += 1
            
             print(f"Cerradura abierta. Energía restante: {energia}. Cerraduras abiertas: {cerraduras_abiertas}.")
             contador_veces_que_se_uso_abrir_cerradura += 1
            if energia < 41 and contador_veces_que_se_uso_abrir_cerradura > 2:
                print ("Hay riesgo de que se active la alarma si abres otra cerradura. ¿Deseas continuar? (Si/No)")
                respuesta = input().lower()
                if respuesta == "si":
                    print("Decidiste abrir otra cerradura.")
                    contador_veces_que_se_uso_abrir_cerradura += 1
                    
                    opcion_cerradura = input("elija un numero del 1 al 3 para abrir la cerradura: ")

                    if opcion_cerradura.isdigit():  # Verificar que sea un número
                      opcion_cerradura = int(opcion_cerradura)
                      if opcion_cerradura == numero_secreto:
                         print(f"¡Cerradura {opcion_cerradura} abierta exitosamente!")
                      else:
                         print(f"La cerradura correcta era la {numero_secreto}. Intenta de nuevo.")
                    else:
                      print("Debe ingresar un número válido.")
                elif respuesta == "no":
                        print("Decidiste no abrir otra cerradura.")
                        break
            if contador_veces_que_se_uso_abrir_cerradura >= 3:
                print("¡Alerta! Has abierto demasiadas cerraduras. La alarma se ha activado.")
                alarma = True
                break
       
        
    
       
# opcion 2 aca tengo que hacer que el usuario ingrese letras y que se acumulen en un codigo parcial, y que si llega a 8 letras se abra una cerradura automaticamente.
    if opcion == "2":
        energia -= 10
        tiempo -= 3
        contador_veces_que_se_uso_abrir_cerradura -= 1
            
        for i in range(4):  # 4 intentos
    # Pedir letras al usuario
         entrada = input(f"Paso {i+1}/4 - Ingrese letras: ").upper().strip()
    
    # Validar que solo sean letras
         if not entrada.isalpha():
           print("   Entrada inválida. Solo se permiten letras. Intente nuevamente.")
                  
    
    # acumular las letras (no reemplazar)
         codigo_parcial += entrada
    
         print(f"   Código parcial actual: {codigo_parcial}")
         print(f"   Longitud: {len(codigo_parcial)} letras")
    
    # Verificar si llegó a 8 letras
        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
              cerraduras_abiertas += 1
              print(f"   ¡Cerradura {cerraduras_abiertas} abierta automáticamente!")
        else:
         print("   Hackeo parcial. Continúa intentando.")
    
    print("-"*40)




    if opcion == "3":
        energia += 30
        tiempo -= 1
        contador_veces_que_se_uso_abrir_cerradura -= 1
        print(f"Descansaste. Energía recuperada: {energia}. Tiempo restante: {tiempo}.")
else: 
  if cerraduras_abiertas == 3:
             print("Ya has abierto todas las cerraduras disponibles VICTORIA.")
  else:
        print("Se activo la alarma, has sido atrapado. GAME OVER.")

# Resultado final
print("="*50)
print("RESULTADO DEL HACKEO:")
print(f"   Código final: {codigo_parcial}")
print(f"   Longitud final: {len(codigo_parcial)} letras")
print(f"   Cerraduras abiertas: {cerraduras_abiertas}/{3}")
print(f"   Energía restante: {energia}")
print(f"   Tiempo restante: {tiempo}")
print("="*50)



    

