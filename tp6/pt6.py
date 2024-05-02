def crear_dibujo(ancho,altura,caracter):
    for i in range(altura): #i = filas
        for j in range(ancho):#j = columnas
            print(caracter,end=' ')
        print("\n")

#principal

while True:
    ancho = int(input("Digite el ancho: "))
    altura = int(input("Digite la altura: "))

    if(ancho > 0 and altura > 0):
        break
    else:
        print("digite valores positivos")

caracter=input("ingrese caracter: ")

crear_dibujo(ancho,altura,caracter)

