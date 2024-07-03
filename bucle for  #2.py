#2 Escribe un programa que sume todos los números pares del 1 al 100 usando un ciclo for.

suma= 0

x= 0

for x in range(1,100+1):
    if x % 2 == 0:
        print(x)
        suma= suma + x
print("___________________________________________")
print(f"= La suma de los numeros pares es : {suma}") 