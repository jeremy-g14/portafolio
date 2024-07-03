#5 Pide al usuario un número entero positivo y muestra todos los
# números impares del 1 hasta ese número usando un ciclo for.

n=int(input("Ingrese un numero positivo : "))
print("______________________________")
c= 0

for i in range(1,n):
    if i % 2 == 1:
        print(i)
        c= c + 1
print("________________________________________________")        
print(f"el numero de impares que hay entre {1} y {n} es de {c}")