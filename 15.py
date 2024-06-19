Aexp = int(input("Ingrese los años de experiencia: "))

if Aexp < 2:
    categoria = "Junior"
elif Aexp >= 2 and Aexp <= 5:
    categoria = "Semi-Señor"
else:
    categoria = "Señor"

print(f"La categoría del trabajador es: {categoria}")