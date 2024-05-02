# def acelerar():
#     global v
#     global tiempo
#     tiempo=1
#     v+=5


# v= float(input("Velocidad?: "))
# print(f"Velocidad actual: {v} km/h")
# print("Aumento de velocidad!")
# acelerar()
# print(f"Velocidad: {v} km/h")
# print(f"Tiempo : {tiempo}")

#otra forma de que v no sea global
# def acelerar(v):
#     tiempo=1
#     v+=5
#     return v,tiempo


# v= float(input("Velocidad?: "))
# print(f"Velocidad actual: {v} km/h")
# print("Aumento de velocidad!")
# print(acelerar(v))
# v,t= acelerar(v)
# print(f"Velocidad: {v} km/h")
# print(f"Tiempo : {t}")

def dos(s):
    s = s + 5
    print('Dos:', s)
def uno(s):
    s = s + 10
    dos(s)
    print('Uno:', s)
    return s

#principal
s = int(input('Inicial:'))#1
s = s + uno(s)
print('Global:',s)