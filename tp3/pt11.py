# 11. Diseñe un algoritmo que permita calcular las mediciones de temperaturas de una caldera, las mismas solo
# pueden ser mayores a 20 grados, si se ingresan valores inferiores a estos se debe volver a pedir el valor. Al final
# del proceso mostrar el promedio de todos los valores ingresados.

band = True
acumulador=0
contador=0

while band:
    respuesta = input("desea ingrear una temperatura? (si/no): ").lower()

    if respuesta == "si":
        temp = int(input("ingresar una temperatura: "))

        if temp <= 20:
            print("solo se permiten valores superiores a 20 grados")
        else:
            acumulador=acumulador+temp
            contador=contador+1
    else:
        band=False

    
print(f"promedio de todos los valores ingresados: {acumulador/contador}")

