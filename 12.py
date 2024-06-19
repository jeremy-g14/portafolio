sbruto = float(input("Ingrese su salario bruto: "))

if sbruto > 2000:
    sneto = sbruto * 0.8
else:
    sneto = sbruto

print(f"Su salario neto es: {sneto: }")