edad = int(input("Ingrese su edad: "))

if edad >= 16 and edad <= 17:
    licencia = "Licencia de menor"
if edad >= 18 and edad <= 65:
    licencia = "Licencia de adulto"
else:
    licencia = "Licencia de adulto mayor"

print(f"aplica para: {licencia}")