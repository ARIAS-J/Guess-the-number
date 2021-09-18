import random
import sys

#Logica de la adivinacion
def adivinacion(x):

    print("======================")
    print(" Bienvenido al Juego! ")
    print("======================")

    print("\n""Tu objetivo es adivinar el numero generado por el computador.")

    # Variable que contiene el numero aleatorio
    numero_aleatorio = random.randint(1, x) # Numero aleatorio entre 1 y x.

    prediccion = 0

    while prediccion != numero_aleatorio:
        # El usuario debe ingresar un numero
        prediccion = int(input(f"Adivina el numero entre 1 y {x}: "))

        if prediccion < numero_aleatorio:
            print("Intenta otra vez. Este numero es muy pequeño.")
        elif prediccion > numero_aleatorio:
            print("Intenta otra vez. este numero es muy grande.")

    print("\n" f"Felicidades adivinaste el numero {numero_aleatorio} correctamente.")

adivinacion(100)
