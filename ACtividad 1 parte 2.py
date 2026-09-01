usuario_correcto="alumno"
clave_correcta="python123"

for intento in range(3):
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == usuario_correcto and clave == clave_correcta:
        print("¡Bienvenido!")
        while True: 
             print("Ingrese una opcion: ")
             print("1. Ingresar ver estado de la inscripcion")
             print("2. Cambiar clave")
             print("3. mensaje de motivacion")
             print("4. Salir")
             if usuario == usuario_correcto and clave == clave_correcta:
                opcion = input("Ingrese su opcion: ")
                if opcion == "1":
                    print("Su inscripcion esta activa")
                elif opcion == "2":
                    nueva_clave = input("Ingrese su nueva clave: ")
                    if len(nueva_clave) >= 6:
                        clave_correcta = nueva_clave
                        confirmar_clave = input("confirmar su nueva clave: ")
                        if confirmar_clave == nueva_clave:
                            print("La clave ha sido cambiada exitosamente.")
                            break
                        else:
                            print("Las claves no coinciden. La clave no ha sido cambiada.")
                            break
                    else:
                        print("La clave debe tener al menos 6 caracteres.")
                        break
                elif opcion == "3":
                    print("dale que se puede locooo")
                elif opcion == "4":
                    print("Saliendo del programa. ¡Hasta luego!")
                    break
                else:
                    print("Opción inválida. Por favor, intente nuevamente.")
        
    else:
        print(f"Usuario o clave incorrectos. Intento {intento + 1} de 3.")

print("Se han agotado los intentos. cuenta bloqueada.")
    
  