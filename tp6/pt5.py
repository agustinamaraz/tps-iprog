def factorial(numero):
    resultado_factorial=1

    for i in range(1,numero+1):
        resultado_factorial*=i
    
    return resultado_factorial

def potencia(base,potencia):
    return base**potencia

def sumatoria(cantidad_terminos,x):
    sumatoria=0
    for n in range(cantidad_terminos):
        sumatoria+=(potencia(x,n)/factorial(n))
        print((potencia(x,n)/factorial(n)))

    print(f"La sumatoria es: {sumatoria}")

def bienvenida(nombre):
    nro=20
    caracter="*"
    print(nro*caracter*3)
    print(nro*caracter,f"BIENVENIDO {nombre}", nro*caracter)
    print(nro*caracter*3)


#principal
# nombre = input("Ingrese su nombre: ")
# bienvenida(nombre)
x= int(input("ingrese la potencia de e: "))
cant_terminos = int(input("Ingrese la cantidad de terminos: "))
sumatoria(cant_terminos,x)

