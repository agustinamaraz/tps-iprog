lista_a = [
    ['100', 'Juan Perez' , 8.5], 
    ['200', 'Maria Lopez' , 7],
    ['600', 'Jorge Muñoz' , 8.00], 
    ['300', 'Anna Loaiza' , 4.5], 
    ['400', 'Tomas Araoz' , 3.5]
]

lista_b = [
    ['300', 'Anna Loaiza' , 6.5],
    ['600', 'Jorge Muñoz' , 10.00],
    ['100', 'Juan Perez' , 8.0],
    ['500', "Paula Stair", 6.5]
]
# 1. Modificar en la Lista A la nota de todos los estudiantes que también se 
# encuentre en la lista B, asignándoles la mayor nota entre ambas listas y emitir 
# un mensaje “Se ha modificado la nota” (40 puntos)
def modificar_lista_a():
    maxima_nota = -1
    
    print("LISTA A ORIGINAL:")
    for item in lista_a:
        print(item)
    
    for itemB in lista_b:
        for itemA in lista_a:
            if itemA[0] == itemB[0]:
                if itemA[2] > itemB[2]:
                    maxima_nota = itemA[2]
                    itemA[2] = maxima_nota
                elif itemA[2] < itemB[2]:
                    maxima_nota = itemB[2]
                    itemA[2] = maxima_nota
                    
    if maxima_nota != -1:
        print("se ha modificado la nota")
                    
    print("LISTA A ACTUALIZADA:")
    for item in lista_a:
        print(item)
        
# 2. A todos los estudiantes de la lista A cuya nota sea menor al promedio de las notas 
# de la lista B aumentarles 5 puntos siempre que no supere la nota 10, si supera 
# la nota 10 emitir un mensaje “no es posible realizar la operación” (20 puntos)

def calcular_promedio_nota_b():
    suma=0
    for item in lista_b:
        suma+=item[2]

    return (suma/len(lista_b))

def aumentar_nota():
    promedio = calcular_promedio_nota_b()
    
    print("LISTA A ORIGINAL:")
    for item in lista_a:
        print(item)
    
    for item in lista_a:
        if item[2] < promedio:
            nota_aumentada = item[2]
            nota_aumentada += 5
            if nota_aumentada > 10:
                print("no es posible realizar operacion")
            else:
                item[2] = nota_aumentada
                
    print("LISTA A ACTUALIZADA:")
    for item in lista_a:
        print(item)

# 3. Eliminar de la lista B, el estudiante cuya nota sea el máximo (20 puntos)
def eliminar_lista_b():
    maximo = -1
    pos=-1
    
    for i,item in enumerate(lista_b):
        if item[2] > maximo:
            maximo = item[2]
            pos=i
           
    print("estudiante a eliminar: ",lista_b[pos]) 
    resp = input("confirma eliminacion? s/n: ")        
    if resp == "s":
        # del lista_b[pos]
        eliminado = lista_b.pop(pos)
        print("estudiante eliminado: ",eliminado)
        
        
        
#principal
# modificar_lista_a()
# aumentar_nota()
eliminar_lista_b()