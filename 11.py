def Nprimo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True
numero= int(input("Ingrese un número: "))
if Nprimo(numero):
    
    
    print(f"{numero} es primo.")
else:
    print(f"{numero} no es primo.")