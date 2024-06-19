peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    clasificacion = "Bajo peso"
if imc >= 18.5 and imc < 24.9:
    clasificacion = "peso normal"
if imc >= 25 and imc < 29.9:
    clasificacion = "Sobrepeso"
else:
    clasificacion = "Obesidad"

print(f"Su Índice de Masa Corporal (IMC) es: {imc: }")
print(f"Usted tiene: {clasificacion}")
