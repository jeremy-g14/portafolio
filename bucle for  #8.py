#8  Pide al usuario un rango de temperaturas en grados
# Celsius (inicio y fin) y muestra la conversión a Fahrenheit para cada grado en ese rango
# usando un ciclo for.

celsius_inicio = int(input("Ingrese el inicio del rango en grados Celsius: "))
celsius_fin = int(input("Ingrese el fin del rango en grados Celsius: "))

conversiones = []

for celsius in range(celsius_inicio, celsius_fin + 1):
    fahrenheit = (celsius * 9/5) + 32
    conversiones.append((celsius, fahrenheit))

print("\nConversion de Celsius a Fahrenheit:")
print("----------------------------------")
print("| Celsius\t| Fahrenheit\t|")
print("----------------------------------")

for celsius, fahrenheit in conversiones:
    print(f"| {celsius}\t\t| {fahrenheit:.2f}\t\t|")

print("----------------------------------")
