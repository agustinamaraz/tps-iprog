monto_total = 0
monto_max=-1
empresa_max=""
negativo=True

for i in range(1,5+1,1):
    negativo=True
    print(i)
    empresa = input("ingrese el nombre de la empresa: ")
    
    while negativo:
        monto = int(input("ingrese el monto"))
        if monto < 0:
            print("el monto no puede ser negativo ni 0")
            negativo=True
        else:
            negativo=False

    monto_total +=  monto
    
    if monto > monto_max:
        monto_max = monto
        empresa_max = empresa

print(f"el monto total es: {monto_total}")
print(f"La empresa que mas dono fue: {empresa_max}")
print(f"el maximo monto donado es: {monto_max}")

# prueba de escritorio-- h=5. RESULTADO = 18

# h = int(input('Ingrese valor: '))
# suma = 0
# i = 5
# while i!=0:
#     if i == 1:
#         suma+= 4
#     elif i > 3:
#         suma+= h
#     else:
#         suma+= 2
#     i-=1
# print(suma)