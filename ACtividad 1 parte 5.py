Nombre_jugador=""
vida_jugador=100
vida_enemigo=100
pociones_de_vida=3
daño_base_ataque_pesado=15
daño_base_enemigo=12
turno_gladiador=True
daño_ataque_rafaga = 5

while True:
    Nombre_jugador = input("Ingrese su nombre: ").strip()
    if Nombre_jugador:
        if Nombre_jugador.replace(" ", "").isalpha():
            break
        else:
            print("El nombre debe contener solo letras y sin espacios. Por favor, intente nuevamente.")
    else:
        print("El nombre no puede estar vacío. Por favor, intente nuevamente.")

while vida_jugador > 0 and vida_enemigo > 0:
    print(f"\n{'='*50}")
    print(f"¡Bienvenido al combate, {Nombre_jugador}!")
    print(f"\n{'='*50}")
    print(f"Vida del jugador: {vida_jugador}")
    print(f"Vida del enemigo: {vida_enemigo}")
    print(f"Pociones de vida restantes: {pociones_de_vida}")
    print(f"\n{'='*50}")
    print("1. Ataque pesado")
    print("2. Ataque rafaga veloz")
    print("3. Usar poción de vida")
    print(f"\n{'='*50}")

    opcion = input("Seleccione una opción: ")

    if opcion == "1": 
        
        vida_enemigo -= daño_base_ataque_pesado
        print(f"Has realizado un ataque pesado causando {daño_base_ataque_pesado} de daño al enemigo.")
       
    if vida_enemigo <= 20:
        daño_base_ataque_pesado = daño_base_ataque_pesado*1.5
        vida_enemigo -= daño_base_ataque_pesado
        print(f"¡Ataque crítico! Has realizado un ataque pesado causando {daño_base_ataque_pesado} de daño al enemigo.")
        
    if opcion == "2":
       for i in range(3):
            vida_enemigo -= daño_ataque_rafaga
            print(f"Has realizado un ataque ráfaga causando {daño_ataque_rafaga} de daño al enemigo.")
            

    if opcion == "3" :
        if pociones_de_vida > 0:
            vida_jugador += 20
            pociones_de_vida -= 1
            print("Has usado una poción de vida. Tu vida ha aumentado en 20 puntos.")
            vida_jugador -= daño_base_enemigo
           
        else:
            print("No tienes más pociones de vida disponibles.")
    vida_jugador -= daño_base_enemigo
    print(f"El enemigo te ha atacado causando {daño_base_enemigo} de daño.")
if vida_jugador <= 0:
    print(f"\n{'='*50}")
    print("¡Has sido derrotado! GAME OVER.")
    print(f"\n{'='*50}")
if vida_enemigo <= 0:
    print(f"\n{'='*50}")
    print("¡Felicidades! Has derrotado al enemigo. ¡Victoria!")
    print(f"\n{'='*50}")
    Salir = input("Presiona Enter para salir del juego.")
    


