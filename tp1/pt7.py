from math import pi

angrad = int(input("ingrese angulo en radianes: "))
sexa=round(angrad*180/pi,2)
cent=angrad*200/pi

print(f"valor en sexadecimal: {sexa}")
print(f"valor en centesimal:  {round(cent,2)}")