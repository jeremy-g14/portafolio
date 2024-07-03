#9 Pide al usuario un número entero positivo NNN y dibuja
# un triángulo de asteriscos de altura NNN usando un ciclo for.

N=int(input("Ingrese un número entero positivo N para la altura del triángulo: "))

if N <= 0:
    print("Por favor ingrese un número entero positivo.")
    
else:
    print(f"Triángulo de asteriscos de altura {N}:")
    
    for i in range(1, N + 1):
             print('*' * i)