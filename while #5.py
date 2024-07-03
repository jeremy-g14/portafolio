# 5 Escribe un programa que elija un número aleatorio entre 1 y 10 y
#permita al usuario adivinarlo, dándole pistas de "mayor" o "menor" hasta que acierte. Usa un ciclo while.

import random

random_N = random.randint(1, 10)

print("Adivina el número entre 1 y 10")

numero= int(input("Ingresa tu numero: "))

while numero != random_N:
    
    if numero < random_N:
        print("¡El número es mayor!")
        
    else:  
        print("¡El número es menor!")
    
    numero= int(input("Inténtalo de nuevo: "))

print(f"¡Felicidades! Adivinaste el número {random_N}.")