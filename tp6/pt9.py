def menu():
    print("\n-------------- BIENVENIDO ----------")
    print("1) calcular la suma de 2 fracciones")
    print("2) calcular la resta de 2 fracciones")
    print("3) calcular la multiplicacion de 2 fracciones")
    print("4) calcular la division de 2 fracciones")
    print("5) Salir")

def ingresar_valores():
    while True:
                a=int(input("Digite numerador: "))
                b=int(input("Digite denominador: "))

                if b>0:
                    return a,b
                else:
                    print("El denominador no puede ser 0")

def mcd(n, d):
    menor = n
    mayor = d
    if n > d:
        menor = d
    mcd = 1

    for i in range(2, menor + 1):
        while n % i == 0 and d % i == 0:
            mcd = mcd * i
            n = n / i
            d = d / i
        if n < i or d < i:
            break

    return mcd

def simplificar(n, d):
    maxcomdiv = mcd(n, d)

    n = n // maxcomdiv
    d = d // maxcomdiv

    if d == 1:
        print(f"El resultado es: {n}")
    else:
        print(f"El resultado es: {n}/{d}")


def sumar(n1,d1,n2,d2):
    numerador = n1*d2+n2*d1
    denominador = d1*d2

    simplificar(numerador,denominador)

#Pricipal

while True:
    menu()
    opcion = int(input("Ingresar opcion: "))

    if opcion==5:
         break
    else:
        numerador,denominador = ingresar_valores()
        numerador2,denominador2 = ingresar_valores()
         
        if opcion==1:
            sumar(
                 numerador,
                 denominador,
                 numerador2,
                 denominador2
            )
        elif opcion==2:
            v=3
        else:
            print("ingrese una opcion valida")