# 5. Diseñar un algoritmo que permita realizar lo siguiente:
# ● Cargar una lista con valores de tipo caracter a pedido del operador.
# ● Mostrar la lista desde el último valor ingresado hasta el primero.
# ● Solicitar un valor al usuario y buscar en la lista devolviendo la posición del primer valor encontrado. En
# caso que no se encuentre devolver -1
# ● Indicar la cantidad de vocales de la lista.

def contar_vocales(lista):
    vocales = ['a','e','i','o','u','A','E','I','O','U']
    contador = 0
    
    for i,item in enumerate(lista):
        if item in vocales:
            contador+=1        

    print("cantidad de vocales en la lista: ", contador)

def buscar_valor(lista):
    valor = input("ingresar valor a buscar: ")
    
    if valor in lista:
        index = lista.index(valor)
        return index
    else:
        return -1

def cargar():
    lista = []
    while True:
        c = input("ingresar caracter: ")
        lista.append(c)
        
        respuesta = input("desea seguir cargando? s/n")
        
        if respuesta != "s":
            break
        
    return lista

def mostrar_ultimo_primero(lista):
    # alternativa 1
    # lista.reverse()
    # print("lista invertida: ",lista)
    
    #alternativa 2
    print("lista invertida: ", lista[::-1])
    
    
    
    
#principal
lista = cargar()
print(lista)

mostrar_ultimo_primero(lista)

pos = buscar_valor(lista)

if pos != -1:
    print("el valor esta en la posicion: ", pos)
else:
    print("posicion no encontrada", pos)
    

contar_vocales(lista)