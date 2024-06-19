# 6  Escribe un programa que solicite la edad del usuario y clasifique la edad en una de las 
# siguientes categorías: "Infantil" (0-12), "Adolescente" (13-19), "Adulto" (20-59) y "Adulto 
# mayor" (60 o más).
print("programa que solicite la edad del usuario y clasifique la edad")
print("===============================================================")
edad=float(input("ingrese la edad : "))

if edad <= 0 or edad <= 12:
    print("Infantil")
    
elif edad <= 13 or edad <= 19:
    print("es adolecente")

elif edad <= 20 or edad <= 59:
    print("es adulto")
    
elif edad >= 60:
    print("es mayor")
    
else :
    print("edad no registrada")
    