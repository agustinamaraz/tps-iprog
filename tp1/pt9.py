# imc=peso en kg/ altura^2 en m
peso = float(input("peso en kg: "))
altura = float(input("altura: "))

imc = peso/pow(altura,2)

print("imc: ", round(imc,2))