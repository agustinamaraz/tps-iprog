#PUNTO 1

#estas listas obvio no estaban en el enunciado, 
# pero el profe mencionó que se suponia que ya habia datos precargados entonces se puede hacer:
codigos = ["1","2","3"]
precios = [100.00,200.00, 300.00]
stocks = [5,0,0]

def validar_codigo(codigo):
    for item in codigos:
        if item == codigo:
            return False
    return True

def agregar_articulo():
    while True:
        codigo = input("ingresar codigo: ")
        if validar_codigo(codigo):
            break

    precio = float(input("ingresar precio: "))
    stock = int(input("ingresar stock: "))

    codigos.append(codigo)
    precios.append(precio)
    stocks.append(stock)

    for i in range(len(codigos)):
        print("codigos: ",codigos[i])
        print("precios: ", precios[i])
        print("stocks: ",stocks[i])

def sumatoria():
    sumatoria=0
    for i,item in enumerate(stocks):
        sumatoria+=(item*precios[i])

    print("sumatoria: ",sumatoria)

def mostrar_aumento_stock(codigo,aumento):
    for i,item in enumerate(codigos):
        if item == codigo:
            stocks[i] += aumento

    print("stock aumentado: ", stocks)

#PUNTO 2
def contar_palabras(cad):
    palabras = cad.split(" ")
    print("cantidad de palabras: ",len(palabras))

#principal
agregar_articulo()
mostrar_aumento_stock("2",5)
sumatoria()
contar_palabras("hola mundo")