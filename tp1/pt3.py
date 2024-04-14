# ------- calculo de interes compuesto -------
# Capital (C)=monto_ingresado
# ValorFinal (VF)=?
# tasa de interes(i) = 4% = 0.04
# Tiempo(t) = 1 año

# calculo
# VF = capital*(1+tasa de interes)^tiempo

monto_ingresado = int(input("ingrese la cantidad de dinero: "))
anio1 = monto_ingresado*(1+0.04)
anio2 = anio1*(1+0.04)
anio3 = anio2*(1+0.04)

print("cantidad de dinero que ingreso: ", monto_ingresado,
      "\n 1er año: ", anio1,
        "\n 2do año: ", anio2,
        "\n 3er año: ", anio3)
