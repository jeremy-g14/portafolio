#7 Pide al usuario un número entero positivo y determina si
# es primo usando un ciclo for.

N=int(input("Ingrese un numero entero positivo : "))
print("______________________________________")
cont= 0

for i in range(1,N+1):
    if N % i == 0:
        cont= cont + 1
        
if cont > 2:
    print(f"el numero {N} no es un numero primo")
    
else:
    print(f"el numero {N} si es un numero primo")