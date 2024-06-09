# Un club de pescadores realizó una competencia de pesca. Por cada participante se registrará la cantidad total
# de peces atrapados. Para ello, se tiene dos listas que almacenan el nombre del participante y las cantidades de
# peces por participante. Diseñar un algoritmo modular, que mediante un menú de opciones resuelve:
# 1. Dar la bienvenida al concurso de pesca
# 2. Cargar las listas con una cantidad n de participantes. La mínima cantidad de participantes es 10 y la
# máxima es 50. La cantidad de peces debe ser mayor o igual a 0.
# 3. Mostrar el promedio de peces capturados.
# 4. Mostrar la mayor cantidad de peces capturados y el nombre del ganador (pueden haber empates).
# 5. Disminuir x peces al participante que está en la posición z.
# 6. Despedirse y salir

def disminuir(participantes,peces):
    mostrar_listas(participantes,peces)
    menos_peces = int(input("ingresar numero de peces a disminuir: "))
    posicion = int(input("ingresar la posicion del participante a diminuirle los peces: "))

    #for para verificar que esa posicion existe
    existe=False
    for i,item in enumerate(participantes):
        if posicion == i: 
            existe=True
            break
        
    #disminuir si es que existe
    if existe:
        peces[posicion] -= menos_peces
        print(peces)
        print(participantes)
    else:
        print("esa posicion no existe")
    
def mayor(participantes,peces):
    max_peces = -1
    ganadores = []
    
    for i in range(len(peces)):
        if peces[i] > max_peces:
            max_peces = peces[i]
            
            #forma 1 es lo mismo que la 2 pero en menos lineas xd
            ganadores = []
            ganadores.append(participantes[i])
            
            #forma 2
            # ganadores = [participantes[i]]
        elif peces[i] == max_peces:
            ganadores.append(participantes[i])
    
    print(f"La mayor cantidad de peces capturados es: {max_peces}")
    print(f"El/los ganador(es) son: ",ganadores)

        
    
    
    

def promedio(listaPeces):
    suma =0
    for i,cantPeces in enumerate(listaPeces):
        suma+=cantPeces

    print("\n\nPromedio de peces capturados: ", suma/len(listaPeces))
    

def carga():
    lista_participantes = []
    lista_peces = []
    
    cant_participantes = int(input("ingrese la cantidad de participantes: "))
    while cant_participantes<10 and cant_participantes>50:
        cant_participantes = int(input("ingrese la cantidad de participantes [10,50]: "))
        
    for i in range(cant_participantes):
        lista_participantes.append((input("ingrese nombre del participante: ")))
        
        peces = int(input("ingrese la cantidad de peces: "))
        while peces<=0:
            peces = int(input("ingresas la cantidad de peces: "))        
        
        lista_peces.append(peces)
        
    return lista_peces,lista_participantes

def mostrar_listas(participantes,peces):
    for i in range(len(participantes)):
        print("participante: ",i,participantes[i], "peces: ", peces[i])

#Principal
peces,participantes = carga()
mostrar_listas(participantes,peces)
promedio(peces)
mayor(participantes, peces)
disminuir(participantes, peces)