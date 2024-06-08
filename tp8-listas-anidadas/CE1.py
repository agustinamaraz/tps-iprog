# 1. Diseñar un programa que, mediante un menú de opciones nos permite realizar:
    # 1. Generar N ternas de valores en forma aleatoria y agregarlas a una lista. Validar que los valores dentro
    # de cada terna no se repitan.
    # 2. Mostrar la lista de valores generados
    # 3. Calcular la suma de todos los valores generados
    # 4. Calcular la suma de los valores de una terna a elección del usuario
    # 5. Calcular el promedio de una columna (primera, segunda o tercera) de las ternas a elección del usuario
    # 6. Salir
    
import random
    
def generar_ternas():
    cant_ternas = int(input("ingresar cantidad de ternas a crear: "))
    
    lista = []

    for i in range(cant_ternas): 
        lista_random = []
        j=0
        while j<3:
            numero = random.randint(0,100)
            
            if numero not in lista_random:
                lista_random.append(numero)
                j+=1
        
        lista.append(lista_random)
        
    return lista
    
def mostrar(lista): 
    for i,item in enumerate(lista): #CUANDO USAMOS ENUMARATE NO VA LEN(LISTA) #CUANDO USAMOS RANGE SI VA LEN(LISTA)
        print("indice: ", i, "terna: ", item)

def calcular_suma(lista):
    total=0
    for terna in lista:
        for i,valor_terna in enumerate(terna):
            total+=valor_terna
            
        # for i in range(len(terna)):
        #     total = total + terna[i]
    return total

def calcular_suma_terna(lista):
    print("TERNAS: ")
    mostrar(lista)
    terna_elegida = int(input("Ingresar indice de la terna a calcular: "))
    total = 0
    
    for i,terna in enumerate(lista):
        if i == terna_elegida:
            for j,valor in enumerate(terna):
                total+=valor
        
    return total

def calcular_promedio_columna(lista):
    columna = int(input("Ingresar columna 1/2/3 : "))
    total = 0
    
    for i,terna in enumerate(lista):    
        for j,valor in enumerate(terna):
            if j == columna-1:
                total+=valor
        
    return (total/len(lista))

def menu():
    while True:
        print("1. Generar Ternas")
        print("2. Mostrar la lista de valores generados")
        print("3. Calcular la suma de todos los valores generados")
        print("4. Calcular la suma de los valores de una terna a elección del usuario")
        print("5. Calcular el promedio de una columna (primera, segunda o tercera) de las ternas a elección del usuario")
        print("6. Salir")

        opcion = int(input("Ingresar Opcion: "))
    
        if (opcion == 1):
            lista = generar_ternas()
        elif (opcion == 2):
            mostrar(lista)
        elif (opcion == 3):
            total = calcular_suma(lista)
            print("la suma de todos es: ", total)
        elif (opcion == 4):
            total = calcular_suma_terna(lista)
            print("la suma la terna eligda es: ", total)
        elif (opcion == 5):
            promedio = calcular_promedio_columna(lista)
            print("el promedio de la columna elegida es: ", promedio)
        elif (opcion == 6):
            print("saliendo del programa...")
            break
        else:
            print("ingresar una opcion valida")
            
            
#Principal
menu()

