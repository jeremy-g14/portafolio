# programa 9

print("programa que solicite un carácter al usuario y determine si es una letra o un digito")
print("=====================================================================================")
caracter =input("Ingrese el caracter : ")
    
if 'A' <= caracter <= 'Z' or 'a' <= caracter <= 'z':
    print("Es un digito")
    
if '0' <= caracter <= '9': 
    print(" es una letra")