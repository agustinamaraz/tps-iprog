nro=7

flag = not nro !=0 or nro <= 7

print(flag)

suma = 0

for i in range(1,nro,2):
    if flag:
        suma += i
    else:
        suma += nro
    flag = not flag

print(suma)