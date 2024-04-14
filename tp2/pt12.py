# 12. Un instituto de enseñanza de inglés necesita un programa que le permita, cada día, procesar observaciones
# sobre las clases de ese día. El instituto dicta clases a estudiantes de distintos niveles y cada nivel tiene clases
# en un día de la semana diferente: los lunes se dicta el Nivel Inicial, los martes el Nivel Intermedio, los
# miércoles el Nivel Avanzado, los jueves son para Práctica Hablada y los viernes se dicta Inglés para Viajeros.
# El usuario ingresa la fecha actual en formato “día, DD/MM", donde [día] es un día de la semana
# (lun-mar-mie-jue-vie), DD es el número de día y MM es el número de mes. Si el usuario ingresa un día de la
# semana inexistente o una fecha cuyo día supere el rango 1-31 o el mes de 1 a 12, indique que se produjo un
# error. Debe permitirse que ingrese el día de la semana en minúsculas o mayúsculas indistintamente.
# Una vez indicada la fecha, el usuario necesita poder indicar si ese día se tomaron exámenes, pero eso sólo si se
# trata de los niveles Inicial, Intermedio o Avanzado, ya que las Prácticas Habladas y el Inglés para Viajeros no
# tienen exámenes. Si hubo exámenes, el usuario ingresará cuántos alumnos aprobaron y cuántos no, y el
# programa le mostrará el porcentaje de Aprobados.
# Si el día fue el correspondiente a práctica hablada, el usuario deberá ingresar el porcentaje de asistencia a
# clase y el programa le indicará "asistió la mayoría" en caso de que la asistencia sea mayor al 50% o "no asistió la
# mayoría" si no es así.
# Si se trata del inglés para viajeros y la fecha actual corresponde al día 1 de cualquier mes, se deberá imprimir
# "Comienzo de nuevo ciclo".

import sys

print("*********** día de la semana (lun-mar-mie-jue-vie), DD es el número de día y MM es el número de mes ************\n")
fecha = input("ingresar la fecha en formarto: dia, DD/MM: ").lower()

fecha_array = fecha.split(",")

if len(fecha_array) != 2: #len devuelve el tamaño del array
    print("Error: formato de fecha incorrecto.")
    sys.exit()

dia = fecha_array[0]

if len(dia) != 3:
    print("mal formato de dia solo se permite (lun-mar-mie-jue-vie)")
    sys.exit()

numeros_array =  fecha_array[1].split("/") #split divide a una cadena dado un separador "/", split devuelve un array con n elementos que separo el "/"

dd,mm = numeros_array[0],numeros_array[1]

if (int(dd) <= 31 and int(dd) > 0) and (int(mm)<=12 and int(mm)>0):
    if dia == "lun" or dia == "mar" or dia == "mier":
        huboExamen = input("Hubo examenes?: (si/no)").lower()
        if huboExamen == "si":
            alumnosA = int(input("alumnos aprobados: "))
            alumnosD = int(input("alumnos desaprobados: "))

            total = alumnosA+alumnosD
            print("porcentaje de alumnos aprobados: ", (alumnosA/total)*100, " %")
        else:
            print("dia tranqui no se tomaron examenes :D")

    elif dia == "jue":
        porcentaje = int(input("ingresar el porcentaje de la cantidad de chicos que asistieron: "))
        if porcentaje >= 50:
            print("asistió la mayoria")
        else:
            print("no asistio la mayoria :/")

    elif dia =="vie":
        if int(dd) == 1: #no funka con == "1" ya que dd es igual a " 1" tonce no pue, deberia ser "1" sin espacio pero q paja 
            print("comienzo de ciclo :ddd")
        else: 
            print("dia normal para los ingles viajeros")

    else:
        print("ese dia no hay clases bro")
else:
    print("mal formartode los dd y mm o uno de los dos perro")
    sys.exit()









