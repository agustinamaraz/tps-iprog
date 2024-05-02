def menu():
    print("\n-------------- BIENVENIDO ----------")
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

def convertir_a_palabra(numero):

    if numero == "0":
        return "cero"
    if numero == "1":
        return "uno"
    if numero == "2":
        return "dos"
    if numero == "3":
        return "tres"
    if numero == "4":
        return "cuatro"
    if numero == "5":
        return "cinco"
    if numero == "6":
        return "seis"
    if numero == "7":
        return "siete"
    if numero == "8":
        return "ocho"
    if numero == "9":
        return "nueve"
    
def intercambiar_valores(a,b):
    if int(a)%2==0 and int(b)%2==0:
        aux=a
        a=b
        b=aux

    return a,b


#principal

while True:
    menu()
    opcion = int(input("Ingresar opcion: "))

    if opcion==1:

        a,b = validar_valores()

        a = convertir_a_palabra(a)
        b = convertir_a_palabra(b)

        print(f"{a}****{b}")

        #lo demas no puede ser xq no vimos listas aun

        # for i in range (len(a)):
        #     print(a[i],end="*")

        # print("\n")

        # for i in range (len(b)):
        #     print(b[i],end="*")


    elif opcion==2:
        a,b = validar_valores()

        a,b = intercambiar_valores(a,b)

        a = convertir_a_palabra(a)
        b = convertir_a_palabra(b)

        print(f"El valor de a es: {a} y el valor de b es: {b}")

    elif opcion==3:
        break
    else:
        print("ingrese una opcion valida")