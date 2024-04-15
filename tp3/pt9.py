# 9. Escribir un programa que solicite ingresar la cantidad de alumnos de un curso y cada nota de los mismos.
# Finalmente deberá mostrar cuántos tienen notas mayores o iguales a 7 y cuántos menores a 7. También calcule
# y muestre el promedio de todos los valores ingresados.


cant=int(input("cantidad de alumnos: "))
total=0
contA=0
contD=0

for i in range(1,cant+1):
    nota = int(input(f"ingresar nota del alumno {i}: "))
    total=total+nota

    if nota >= 7:
        print(f"el alumnos {i} tiene una nota mayor o igual a 7. Nota: {nota}")
        contA=contA+nota
    else:
        print(f"el alumnos {i} tiene una nota menor a 7. Nota: {nota}")
        contD=contD+nota
    
print(f"promedio de todas las notas: {total/cant}")
