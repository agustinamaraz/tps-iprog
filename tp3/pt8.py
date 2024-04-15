# 8. Realizar el código de un programa que solicite al usuario un número entero positivo (debe validar que cumpla
# ésta condición) y muestre por pantalla todos los números impares desde 1 hasta ese número. Resuelto lo
# anterior, comente las líneas de código y agregue otras que muestre los impares en forma decreciente desde el
# número ingresado hasta 1.

import sys

num = int(input("ingrese un numero entero positivo: "))

if num < 0:
    print("el numero debe ser positivo!!")
    sys.exit()

for i in range(1,num+1,2):
    print(f"impar: {i} ")
    
print("\n\n")

for i in range(num,0,-1):
    if i%2!=0:
        print(f"impar: {i}")