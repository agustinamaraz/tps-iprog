# 10. Una fábrica necesita un programa para calcular el salario y mostrar el detalle de sus empleados, los mismos
# tienen un sueldo básico común y se adiciona un 10% por cada aumento de categoría, un 5% por cada año de
# antigüedad. A todos los empleados se les descuenta un 11% por aportes jubilatorios y un 4% por obra social
# ambos del sueldo básico, y finalmente un aumento fijo de $200 en concepto de salario familiar por cada hijo
# menor de 18 años.


cantidad_empleados = int(input("ingrese la cantidad de empleados: "))
sueldo_basico = float(input("ingrese el sueldo_basico basico comun: "))

for i in range(1,cantidad_empleados+1):

    salario=sueldo_basico

    salario=sueldo_basico-sueldo_basico*0.15

    aumentocategoria = input(f"el empleado {i} aumento de categoria (si/no): ").lower()

    if aumentocategoria == "si":
        salario=salario+sueldo_basico*0.10

    aniodeantiguedad = input(f"el empleado {i} está proximo a cumplir otro año en la empresa? (si/no): ").lower()

    if aniodeantiguedad == "si":
        salario = salario+sueldo_basico*0.05

    cant_hijos = int(input(f"el empleado {i} ¿cuantos hijos menores de 18 años tiene?: "))

    salario=salario+200*cant_hijos

    print(f"\nel empleado {i} cobra un salario de: ${salario}")
    



