#1 Escribe un programa que solicite al usuario un número y determine si es positivo,
#negativo o cero.
numero= int(input(" escribe el numero : "))

if numero >0:
    print(f" el numero {numero} es positivo")
    
elif numero ==0:
    print(f" el numero {numero} es cero ")
    
else:
    print(f" el numero {numero} es negativo ")