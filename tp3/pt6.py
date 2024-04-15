# 6. Leer números enteros, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los
# números positivos ingresados.
acumulador=0

while True: #simulador de do while
    num = int(input("ingresar un numero: "))

    if num > 0:
        acumulador=acumulador+num
    elif num == 0:
        break #para que termine el bucle

print(f"sumatoria: {acumulador}")