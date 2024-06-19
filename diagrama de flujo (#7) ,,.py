# programa si el precio es mayor a 100 se aplica descuento

print("programa que solicite el precio de un producto y determine el precio final")
print("===========================================================================")
precio=float(input("Ingrese el precio del producto : "))

if precio > 100:
    d=(precio * 0.1)
    
    pf=(precio - d)
else:
    pf = precio

print(f"El precio final del producto es: {pf:.2f}")
