# 12. Pida al usuario una cantidad N de puntos a representar en el plano cartesiano. Lea el par de valores que
# representan las coordenadas (x,y), para cada punto indique en qué cuadrante se encuentra. Muestre al final la
# cantidad de puntos ingresados para cada cuadrante. La figura muestra un caso ejemplo, con el ingreso de
# valores (x,y) para 3 puntos.

n = int(input("ingresar cantidad de puntos: "))
cont1=0
cont2=0
cont3=0
cont4=0

for i in range(1,n+1):
    x = int(input(f"Para el punto {i} ingrese las coordenadas de X: "))
    y = int(input(f"Para el punto {i} ingrese las coordenadas de Y: "))

    if x > 0 and y > 0:
        print(f"el punto {i} pertenece al cuadrante 1")
        cont1=cont1+1
    elif x < 0 and y > 0:
        print(f"el punto {i} pertenece al cuadrante 2")
        cont2=cont2+1
    elif x < 0 and y < 0:
        print(f"el punto {i} pertenece al cuadrante 3")
        cont3=cont3+1
    elif x > 0 and y < 0:
        print(f"el punto {i} pertenece al cuadrante 4")
        cont4=cont4+1
    else:
        print("el punto se encuentra en el origen")

print(f"cantidad de puntos en el cuadrante 1: {cont1}")
print(f"cantidad de puntos en el cuadrante 2: {cont2}")
print(f"cantidad de puntos en el cuadrante 3: {cont3}")
print(f"cantidad de puntos en el cuadrante 4: {cont4}")