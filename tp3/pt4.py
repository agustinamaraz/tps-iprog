ddo = int(input("ingrese dividendo: "))
dsor = int(input("ingrese divisor: "))

cont = 0

while ddo >= dsor:
    ddo = ddo - dsor
    cont=cont+1
    
print(f"resultado: {cont}")