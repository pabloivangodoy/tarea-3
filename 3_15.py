import random

def juego_adivinanza():
    # Generar un número aleatorio entre 1 y 100
    numero_objetivo = random.randint(1, 100)
    intento = None
    intentos_realizados = 0
    
    print("¡Bienvenido al juego de adivinanza!")
    print("Estoy pensando en un número entre 1 y 100.")
    
    # Bucle principal del juego
    while intento != numero_objetivo:
        # Solicitar al usuario un número
        intento = int(input("Adivina el número: "))
        intentos_realizados += 1
        
        # Proporcionar pistas
        if intento < numero_objetivo:
            print("El número es mayor.")
        elif intento > numero_objetivo:
            print("El número es menor.")
        else:
            print(f"¡Felicidades! Has adivinado el número en {intentos_realizados} intentos.")
            break

# Llamar a la función para iniciar el juego
juego_adivinanza()
