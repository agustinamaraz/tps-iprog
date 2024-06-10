# Se cuenta con una lista A cargada con la información de las materias de una carrera universitaria 
# privada donde, para cada una de ellas. se registra el código, nombre, año de cursada (1 a 5), 
# precios, cupo (valor entero que representa la cantidad máxima de alumnos a inscribir), y cantidad 
# de inscriptos actuales. Diseñar los módulos necesarios para resolver lo siguiente:
# 1. (30 PUNTOS) Realizar la inscripción de un alumno en una materia. Para ello, se debe 
# solicitar y guardar el código de materia, DNI y nombre de alumno en la lista B. Para hacer 
# la inscripción se debe validar que el código de materia exista en la lista A y que el cupo 
# máximo de la misma no se haya superado; en caso contrario en caso contrario informar con 
# el mensaje correspondiente. A medida que se realiza una nueva inscripción es necesario 
# actualizar la cantidad de inscriptos de la materia en la lista A.
# 2. (15 PUNTOS) A partir de la información de la lista A, Mostrar el importe total recaudado por 
# una materia Dando su código. Para el cálculo se debe considerar la cantidad total de 
# alumnos que se inscribieron en la misma.
# 3. (20 PUNTOS) crear una lista C que contenga la información de las materias cuyo precio sea 
# menor al precio promedio de todas las materias.
# 4. (15 PUNTOS) Informar la cantidad de alumnos cuyo nombre contenga las subcadena 
# “María”
# 5. (20 PUNTOS) Disminuir el precio de todas las materias de primer año en un 5%
# importante solo debe diseñar los módulos necesarios e incluir las llamadas con el mismo desde el 
# programa principal coma no debe diseñar el menú de opciones debe trabajar con lista anidadas y 
# considere la siguiente guía para el análisis de problemas


# código, nombre, año de cursada (1 a 5), precios, cupo, y cantidad de inscriptos actuales. 
M1=[1001,"FISICA",2,3000,5,2]
M2=[1002,"IPROG",1,4000,4,1]
M3=[1003,"ALGEBRA",1,5000,6,1]

lista_a = [M1,M2,M3]

# Código de materia, DNI y nombre de alumno
A1=[1001,44949820,"AGUSTINA"]
A2=[1001,44949822,"MAXI"]
A3=[1002,44949823,"María"]
A4=[1003,44949824,"María ELENA"]

lista_b = [A1,A2,A3,A4]

# solicitar y guardar el código de materia, DNI y nombre de alumno en la lista B. Para hacer 
# la inscripción se debe validar que el código de materia exista en la lista A y que el cupo 
# máximo de la misma no se haya superado; en caso contrario en caso contrario informar con 
# el mensaje correspondiente. A medida que se realiza una nueva inscripción es necesario 
# actualizar la cantidad de inscriptos de la materia en la lista A.
def validar_codigo_materia(codigo):
    existe_codigo = False
    for item in lista_a:
        if item[0] == codigo:
            existe_codigo = True
            break
    
    if not existe_codigo:
        print("el codigo de esa materia no existe")    
        
    return (existe_codigo)

def inscripcion():
    
    print(lista_a)
    print(lista_b)
    
    
    nombre = input("ingresar nombre: ")
    dni = int(input("ingresar dni: "))
    
    while True:
        
        codigo = int(input("ingresar codigo: "))
        if validar_codigo_materia(codigo)==True:
            break
    
    for materia in lista_a:
        if codigo == materia[0]:
            if materia[5] >= materia[4]:
                print("no hay cupo disponible esa materia")
                break
            else:
                materia[5] += 1
                lista_b.append([codigo,dni,nombre])
    print("\nLISTAS ACTUALIZADAS: ----------")
    print(lista_a)
    print(lista_b)
        
# 2. (15 PUNTOS) A partir de la información de la lista A, Mostrar el importe total recaudado por 
# una materia Dando su código. Para el cálculo se debe considerar la cantidad total de 
# alumnos que se inscribieron en la misma.
def mostrar_importe_total():
    codigo = int(input("Ingresar codigo de la materia para calc el total recaudado: "))
    total = 0
    
    if validar_codigo_materia(codigo):
        for item in lista_a:
            if item[0] == codigo:
                total = item[3]*item[5]
        
        print("total: ", total)
        
        
# 3. (20 PUNTOS) crear una lista C que contenga la información de las materias cuyo precio sea 
# menor al precio promedio de todas las materias.
def crear_lista_c():
    lista_c = []
    total=0
    for item in lista_a:
        total+=item[3]
        
    promedio = total/len(lista_a)
    
    for item in lista_a:
        if item[3] < promedio:
            lista_c.append(item)
    
    print("lista c: ")
    for item in lista_c:
        print(item)
        
# 4. (15 PUNTOS) Informar la cantidad de alumnos cuyo nombre contenga las subcadena 
# “María”
def mostrar_maria():
    for item in lista_b:
        if item[2].find("María") != -1:
            print(item)
    
# 5. (20 PUNTOS) Disminuir el precio de todas las materias de primer año en un 5%

def disminuir_precio():
    for item in lista_a:
        if item[2] == 1:
            item[3]-=(5*item[3]/100)

#principal
# inscripcion()
# mostrar_importe_total()
# crear_lista_c()
# mostrar_maria()
disminuir_precio()
print(lista_a)