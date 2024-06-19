# programa 5

print("programa que solicite una palabra al usuario y determine si tiene más de 5")
print("===========================================================================")
palabra=input("ingrese la palabra : ")

p=len(palabra.strip())

if p >= 5:
    print(f"la palabra {palabra} tiene mas de 5 letras")
else :
    print(f" la palabra {palabra} tiene menos de cinco letra ")