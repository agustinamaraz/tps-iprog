# 13. Mediante un menú de opciones el usuario debe poder seleccionar una opción (1, 2 ó 3). Si elige una opción
# incorrecta, se debe informar del error. Volver a mostrar las tres opciones luego de ejecutada cada opción,
# permitiendo volver a elegir. Si elige las opciones 1 muestre un texto de Bienvenida, 2 mostrar el mayor de
# cinco valores numéricos ingresados. Si elige la opción 3, el programa finalizará

band=True
max=-100

while band:
    print("\n----------------- MENU -------------------")
    print("1) Recibir bienvenida")
    print("2) Calcular el mayor de cinco numeros")
    print("3) Salir del Programa\n")
    opcion = int(input("Ingrese una opcion: "))

    if opcion == 1:
        print("\n *********** BIENVENIDO ************\n")
    elif opcion == 2:
        for i in range(5):
            n = int(input("ingrese un numero: "))
            if n>max:
                max=n
        print(f"el numero mayor entre todos es: {max}")
    elif opcion == 3:
        print("el programa finalizará")
        break
    else:
        print("NO EXISTE ESA OPCION")
            