# Parcial EFC Tema 1
# Sucursal A y B
# Codigo stock precio fecha
# *Punto 1: agregar producto validar codigo no repetir. Puntos 30%
# *Punto 2: mostrar los datos de los productos repetidos de ambas sucursales. Puntos 30%
# *Punto 3: vender producto, introducir codigo y cantidad. Luego disminuir el stock. Puntos 20%
# *Punto : 4 Ingresar mensaje y regresar la cantidad de letras de cada palabra. Ejemplo: aguante el lobo jujeño. Puntos 20%

productos = [
    ["1", 10,100,"26-07-2003"], # 
    ["2", 20,200,"27-07-2003"], #
    ["3", 30,300,"28-07-2003"], #
]

productos2 = [
    ["4", 10,100,"26-07-2003"], # 
    ["2", 20,200,"27-07-2003"], # 
    ["1", 30,300,"28-07-2003"], #
]

def mostrar_no_repetidos():
    print("productos que no se repiten: ")
    no_repetidos = []

    for item in productos:
        repetido = False
        for item2 in productos2:
            if item[0] == item2[0]:
                repetido = True
                break
        
        if repetido==False:
            no_repetidos.append(item)
    print(no_repetidos)
    
    # # Agregar productos de la segunda lista que no están en la primera lista
    # for item2 in productos2:
    #     repetido = False
    #     for item in productos:
    #         if item2[0] == item[0]:
    #             repetido = True
    #             break
    #     if not repetido:
    #         no_repetidos.append(item2)
    
    # # Imprimir productos no repetidos
    # for item in no_repetidos:
    #     print(item)

def validar_codigo(codigo):
    for item in productos:
        if item[0] == codigo:
            return False 
    return True

def cargar_producto():
    while True:
        codigo = input("ingresar codigo: ")
        if validar_codigo(codigo):
            break
    
def contar_letras():
    mensaje = input("ingresar mensaje: ")
    cantidad = mensaje.split(" ")
    print(cantidad)
    print("cantidad de palabras: ", len(cantidad))
    
#principal
# cargar_producto()
# mostrar_repetidos()
# contar_letras()