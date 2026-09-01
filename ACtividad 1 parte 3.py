
cant1=4
cant2=3
opcion=0
nombres_lunes=[]
nombres_martes=[]

while True: 
    nombre = input("Ingrese su nombre: ")
    if nombre.strip():
        if nombre.isalpha():
            break
        else:
            print("El nombre debe contener solo letras y sin espacios. Por favor, intente nuevamente.")
    else:
        print("El nombre no puede estar vacío. Por favor, intente nuevamente.")

while True:
    print(f"\n{'='*50}")
    print(f"\n--¡Bienvenido al sistema de turnos!")
    print(f"\n{'='*50}")
    print("1. Reservar Turno")
    print("2. Cancelar turno")
    print("3. Ver agenda del dia")
    print("4. Ver resumen general")
    print("5. Salir")
    print(f"\n{'='*50}")
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        print("Elija una fecha para reservar su turno")
        print("1. Lunes")
        print("2. Martes")
        print(f"\n{'='*50}")
        opcion_fecha = input("Seleccione una fecha: ")
        
        if opcion_fecha == "1":
            if len(nombres_lunes) < cant1:
                nombre_turno = input("Ingrese su nombre para el turno del lunes: ")
                nombre_turno = nombre_turno.strip()
                nombre_turno = nombre_turno.capitalize()
                if nombre_turno:
                    nombres_lunes.append(nombre_turno)
                    print(f"Turno reservado para el lunes. Quedan {cant1 - len(nombres_lunes)} turnos disponibles.")
                else:
                    print("El nombre no puede estar vacío. Por favor, intente nuevamente.")
            else:
                print("No hay turnos disponibles para el lunes.")
                
        elif opcion_fecha == "2":
            if len(nombres_martes) < cant2:
                nombre_turno = input("Ingrese su nombre para el turno del martes: ")
                nombre_turno = nombre_turno.strip()
                nombre_turno = nombre_turno.capitalize()
                if nombre_turno:
                    nombres_martes.append(nombre_turno)
                    print(f"Turno reservado para el martes. Quedan {cant2 - len(nombres_martes)} turnos disponibles.")
                else:
                    print("El nombre no puede estar vacío. Por favor, intente nuevamente.")
            else:
                print("No hay turnos disponibles para el martes.")
        else:
            print("Opción inválida. Por favor, intente nuevamente.")
            
    elif opcion == "2":
        print("Ingrese la fecha del turno que desea cancelar:")
        print("1. Lunes")
        print("2. Martes")
        opcion_fecha = input("Seleccione una fecha: ")
        if opcion_fecha == "1":
            if nombres_lunes:
                nombre_cancelar = input("Ingrese el nombre del turno a cancelar: ")
                nombre_cancelar = nombre_cancelar.strip().capitalize()
                if nombre_cancelar in nombres_lunes:
                    nombres_lunes.remove(nombre_cancelar)
                    print(f"Turno del lunes cancelado. Quedan {cant1 - len(nombres_lunes)} turnos disponibles.")
                else:
                    print("No se encontró ese nombre en los turnos del lunes.")
            else:
                print("No hay turnos reservados para el lunes.")
        elif opcion_fecha == "2":
            if nombres_martes:
                nombre_cancelar = input("Ingrese el nombre del turno a cancelar: ")
                nombre_cancelar = nombre_cancelar.strip().capitalize()
                if nombre_cancelar in nombres_martes:
                    nombres_martes.remove(nombre_cancelar)
                    print(f"Turno del martes cancelado. Quedan {cant2 - len(nombres_martes)} turnos disponibles.")
                else:
                    print("No se encontró ese nombre en los turnos del martes.")
            else:
                print("No hay turnos reservados para el martes.")
        else:
            print("Opción inválida. Por favor, intente nuevamente.")
            
    elif opcion == "3":
        # AGENDA DEL DÍA - Mostrar turnos en orden con "(libre)" si está vacío
        print(f"\n{'='*50}")
        print("AGENDA DEL DÍA")
        print(f"{'='*50}")
        
        # Mostrar turnos del LUNES
        print(f"\nLUNES ({cant1} turnos totales):")
        for i in range(1, cant1 + 1):
            if i <= len(nombres_lunes):
                print(f"  Turno {i}: {nombres_lunes[i-1]}")
            else:
                print(f"  Turno {i}: (libre)")
        
        # Mostrar turnos del MARTES
        print(f"\nMARTES ({cant2} turnos totales):")
        for i in range(1, cant2 + 1):
            if i <= len(nombres_martes):
                print(f"  Turno {i}: {nombres_martes[i-1]}")
            else:
                print(f"  Turno {i}: (libre)")
        
        print(f"\n{'='*50}")
        
    elif opcion == "4":
        # RESUMEN GENERAL
        print(f"\n{'='*50}")
        print("RESUMEN GENERAL")
        print(f"{'='*50}")
        
        # Calcular estadísticas
        ocupados_lunes = len(nombres_lunes)
        disponibles_lunes = cant1 - ocupados_lunes
        ocupados_martes = len(nombres_martes)
        disponibles_martes = cant2 - ocupados_martes
        
        total_ocupados = ocupados_lunes + ocupados_martes
        total_disponibles = disponibles_lunes + disponibles_martes
        
        # Mostrar por día
        print(f"\nLUNES:")
        print(f"  Turnos ocupados: {ocupados_lunes}")
        print(f"  Turnos disponibles: {disponibles_lunes}")
        if ocupados_lunes > 0:
            print(f"  Nombres: {', '.join(nombres_lunes)}")
        else:
            print("  Nombres: (sin turnos)")
        
        print(f"\nMARTES:")
        print(f"  Turnos ocupados: {ocupados_martes}")
        print(f"  Turnos disponibles: {disponibles_martes}")
        if ocupados_martes > 0:
            print(f"  Nombres: {', '.join(nombres_martes)}")
        else:
            print("  Nombres: (sin turnos)")
        
        # Día con más turnos (o empate)
        print(f"\n{'='*50}")
        print("DÍA CON MÁS TURNOS:")
        
        if ocupados_lunes > ocupados_martes:
            print("  Lunes tiene más turnos ocupados.")
            if disponibles_lunes > disponibles_martes:
                print("  Lunes también tiene más turnos disponibles.")
            elif disponibles_lunes < disponibles_martes:
                print("  Martes tiene más turnos disponibles.")
            else:
                print("  Ambos días tienen la misma cantidad de turnos disponibles.")
        elif ocupados_martes > ocupados_lunes:
            print("  Martes tiene más turnos ocupados.")
            if disponibles_martes > disponibles_lunes:
                print("  Martes también tiene más turnos disponibles.")
            elif disponibles_martes < disponibles_lunes:
                print("  Lunes tiene más turnos disponibles.")
            else:
                print("  Ambos días tienen la misma cantidad de turnos disponibles.")
        else:  # Empate en ocupados
            if ocupados_lunes == 0 and ocupados_martes == 0:
                print("  Ambos días están vacíos (empate).")
            else:
                print("  Empate en turnos ocupados entre Lunes y Martes.")
                if disponibles_lunes > disponibles_martes:
                    print("  Lunes tiene más turnos disponibles.")
                elif disponibles_martes > disponibles_lunes:
                    print("  Martes tiene más turnos disponibles.")
                else:
                    print("  También hay empate en turnos disponibles.")
        
        # Totales generales
        print(f"\n{'='*50}")
        print("TOTALES GENERALES:")
        print(f"  Total de turnos ocupados: {total_ocupados}")
        print(f"  Total de turnos disponibles: {total_disponibles}")
        print(f"  Total de turnos: {total_ocupados + total_disponibles}")
        print(f"{'='*50}")
        
    elif opcion == "5":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción del 1 al 5.")