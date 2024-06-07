# 7. Escribir el código que permita:
# ● Cargar una lista con N valores aleatorios (random.randint(a,b)), los valores aleatorios deben
# encontrarse entre 0 y 100. El valor N es el tamaño de la lista ingresado por el usuario.
# ● Mostrar el sector de la lista deseada, ingresar el inicio el fin y el paso.
# ● Copiar la lista a una denominada listaInversa en donde el orden de los elementos se encuentra en
# orden inverso a la lista original. Muestre ambas listas.
# ● Eliminar de listaInversa los valores duplicados. Mostrar ambas listas

from random import randint

def eliminar(lista):
    lista.reverse()
    print("lista invertida: ", lista)
    # for item in lista:
    #     if item not in lista_sin_duplicados:
    #         lista_sin_duplicados.append(item)
    lista_sin_repetidos = [elemento for elemento in lista if lista.count(elemento) == 1]
    print("lista sin repetidos: ", lista_sin_repetidos)
    
def mostrar(lista):
#     # ['', '', ''] ::
#     # ['1', '2', '3'] 1:2:3
#     # ['1', '2', ''] 1:2:
#     # ['1', '', ''] 1::
#     # ['', '2', ''] :2:
#     # ['', '', '3'] ::3
#     # ['1', '', '3'] 1::3
#     # ['', '2', '3'] :2:3
#     # ['1'] 1
    
#     rebanada = (input("ingresar la rebanda o el indice que quiere ver: "))
    
#     rebanada_lista = (rebanada.split(":")).copy()

#     for i,item in enumerate(len(rebanada_lista)):
        
#         if (i==0):
#             x=item
#         if (i==2) 

    print(lista)

def cargar():
    lista = []
    tamanio_lista = int(input("Ingresar tamanio de la lista: "))
    
    for i in range(tamanio_lista):
        random = randint(0,100)
        lista.append(random)
    
    return lista
    
#PRINCIPAL

lista = cargar()
# mostrar(lista)

eliminar(lista)