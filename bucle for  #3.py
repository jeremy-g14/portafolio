#3 Pide al usuario que ingrese una cadena de texto y cuenta
# cuántas vocales hay en la cadena usando un ciclo for.

texto=input("Ingrese una cadena de texto : ")
print("________________________________")

vocales='a','e','i','o','u','A','E','I','O','U'

c= 0

for i in texto:
   if i in vocales :
       c = c + 1
       
print(f"en texto, hay un total de {c} vocales")
    
    
   