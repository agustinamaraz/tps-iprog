def menu():
    print("-------------- BIENVENIDO ----------")
    print("1) Ingresar dos valores a y b validando que estén en el intervalo [0,9] y mostrarlos en letras separados por una serie de asteriscos")
    print("2) Ingresar dos valores a y b, si son pares intercambiar los valores y mostrarlos en letras")
    print("3) Salir")


def validar_valores():
    while True:
                a=input("Digite a: ")
                b=input("Digite b: ")

                if((int(a) >=0  and int(a) <=9) and (int(b)>=0 and int(b)<=9)):
                    return a,b
                else:
                    print("Los valores deben estar dentro del rango [0,9]!!!")

#principal

while True:
    menu()
    opcion = int(input("Ingresar opcion: "))

    if opcion==1:

        a,b = validar_valores()

    elif opcion==2:
        v=3
    elif opcion==3:
        break
    else:
        print("ingrese una opcion valida")