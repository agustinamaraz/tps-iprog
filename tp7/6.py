# 6. Diseñar un algoritmo que permita realizar lo siguiente:
# ● Cargar una lista con valores numéricos hasta que el usuario ingrese cero. No debe permitir que se
# carguen valores duplicados en la lista.
# ● Mostrar la lista completa con la cantidad de elementos
# ● Agregar un elemento al final de la lista
# ● Insertar un elemento preguntando la posición al usuario. Valide que el valor no se encuentre cargado.
# ● Eliminar un elemento indicado por el usuario. Si no se encuentra debe informar con un mensaje.
# ● Copiar los valores pares a otra lista de nombre listaPares. Mostrar ambas listas.
def es_par(num):
    if num % 2 == 0:
        return True
    return False

def copiar_lista_pares(lista):
    listaPares = []
    
    for i,item in enumerate(lista):
        if es_par(item):
            listaPares.append(item)
            
    print("Lista original: ", lista)
    print("Lista con valores pares: ", listaPares)

def eliminar(lista):
    n = int(input("valor a eliminar de la lista: "))
    
    while True:
        if n in lista:
            lista.remove(n)
            print(lista)
            break
        else:
            print("ese numero no esta en la lista, ingresar otro")

def insertar(lista):
    n = int(input("ingresar numero: "))
    pos = int(input("ingresar una posicion: "))
    
    while True:
        if n not in lista:
            lista.insert(pos,n)
            print(lista)
            break
        else:
            print("ese numero ya esta en la lista, ingresar otro")

def agregar(lista):
    n = int(input("ingresar numero: "))
    
    while True:
        if n not in lista:
            lista.append(n)
            print(lista)
            break
        else:
            print("ese numero ya esta en la lista, ingresar otro")

def mostrar(lista):
    print("Lista: ", lista)
        
    print("cantidad de elementos: ", len(lista))

def cargar():
    lista = []
        
    while True:
     
        numero = int(input("ingresar valor numerico, 0 para terminar: "))
        
        if numero == 0:
            break
        if numero not in lista:
            lista.append(numero)
        else:
            print("ese numero ya esta en la lista, ingresar otro")
            
      
    return lista
    
#PRINCIPAL

lista = cargar()
mostrar(lista)
agregar(lista)
insertar(lista)
eliminar(lista)
copiar_lista_pares(lista)