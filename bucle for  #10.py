#10 Pide al usuario una cadena de texto y un número entero positivo NNN.
# Muestra la cadena repetida NNN veces, cada vez en una nueva línea, usando un ciclo for.

texto=input("Ingrese una cadena de  texto : ")
n=int(input("Ingrese el numero de repeticiones : "))

for i in range(1,n+1):
    print(texto, i)
print("------")
print("|Final|")