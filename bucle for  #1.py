#1 Pide al usuario un número entero positivo y muestra su tabla de
# multiplicar del 1 al 10 usando un ciclo for.

N=int(input("Ingrese un numero entero : "))

print("______________________________")

for i in range(1,10+1):
    R= i * N
    print(N,"X",i, "=",R)
    
print(f"fin de la tabla de multiplicar del {N}")