# 1. Analizar y ejecutar el programa adivina_numero que en menos de 7 intentos el usuario tiene que adivinar un
# número generado al azar que se encuentra en el rango de 1 a 100

from random import randint

num_random = randint(1,100)

cant_intentos = 0

for i in range(1,8): #va del 1 al 7
    print(f"intento {i}")

    numero = int(input("Ingrese un numero: "))

    if numero == num_random:
        print(f"Felicitaciones, adivinaste el numero {num_random}")
        break
    elif numero > num_random:
        print("El numero ingresado es mayor al numero a adivinar")
    else:
        print("El numero ingresado es menor al numero a adivinar")
    
