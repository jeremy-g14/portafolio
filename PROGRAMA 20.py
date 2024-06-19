# 20 programa que solicite la distancia recorrida en kilómetros y calcule la tarifa
#del taxi. La tarifa es $2.50 por kilómetro para los primeros 10 kilómetros y $2.00 por
#kilómetro adicional.

print("calcular la tarifa de un taxi")
print("-----------------------------")

ki=float(input("ingrese el monte:"))

if ki < 10:
    tarifa=ki * 2.50
else:
    tarifa= 10 * 2.50 +( ki -10) *2.00
    print (f"tarifa del taxi :", ki)