# 4. Diseñar un algoritmo que permita realizar lo siguiente:
# ● Cargar una lista con N números enteros
# ● Mostrar los números ingresados y su posición
# ● Mostrar si los elementos de la lista se encuentran ordenados en forma descendente
# ● Mostrar los valores que superen el promedio de los valores ingresados
# ● Mostrar el mínimo de los valores ingresados y su posición
# ● Indicar qué elementos son valores primos
# ● El algoritmo debe considerar que si no se cargó la lista previamente, no se pueda realizar alguna de las
# acciones solicitadas.


def carga():
    lista = list()
    # lista = []
    
    while True:
        numero = int(input("Numero a agregar a la lista: "))

        if (numero not in lista):
            lista.append(numero)
        else:
            print("Ese numero ya está, agrega otro diferente")
            
        respuesta = input("Desea continuar en agregando elementos? s/n")
        
        if respuesta != "s":
            break
            
    return lista


def mostrar_num_pos(lista): #lista simple
    for i,item in enumerate(lista):
        print("posicion: ",i,"numero: ",item)

def mostrar_descendente(lista):
    for i,item in enumerate(lista):
        if i+1 < len(lista):
            if item < lista[i+1]:
                lista=[]
                break
        
    if len(lista) > 0:
        print("lista es descentende: ",lista)
    else:
        print("la lista no esta ordenada de forma descendente")
        
        
def mostrar_valores_que_superen_el_promedio (lista):
    promedio = 0
    total = 0
    
    for i,item in enumerate(lista):
        total += item
    
    promedio = total/len(lista)
    
    print("el promedio es: ", promedio)
    
    for i,item in enumerate(lista):
        if item > promedio:
            print("este valor supera el promedio: ", item)
            
def mostrar_minimo_y_posicion(lista):
    print("minimo: ", min(lista))
    print("indice: ",lista.index(min(lista)))
    
    
def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, numero): #numero=4; i=2 ; 2 < 3
        if numero % i == 0:
            return False
    return True

def mostrar_primos(lista):
    for i, item in enumerate(lista):
        if es_primo(item):
            print(f"El número {item} en la posición {i} es primo.")
        
    
#Principal
lista = carga()
print(lista)

mostrar_num_pos(lista)

mostrar_descendente(lista)

mostrar_valores_que_superen_el_promedio(lista)

mostrar_minimo_y_posicion(lista)

mostrar_primos(lista)

