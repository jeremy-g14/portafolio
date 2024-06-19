#programa 10

print("programa que solicite dos números y determine cuál es mayor o si son iguales")
print("============================================================================")
N1=float(input("Ingrese el primer numero : "))
N2=float(input("Ingrese el segundo numero : "))

if N1 == N2:
    print("los dos numeros son iguales")
    
elif N1 > N2:
    print(f'{N1} es mayor que {N2}')
    
elif N2 > N1:
    print(f'{N2} es mayor que {N1}')
    
