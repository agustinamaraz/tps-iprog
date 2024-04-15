# 7. Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido
# (desde 1 hasta su edad). Por ejemplo si ingresa: 18, Debe mostrar: 1 año, 2 años, 3 años, …, 18 años

edad = int(input("ingrese su edad: "))


for i in range(1,edad+1):
    print(f"{i} años")