# 5. Muestre todos los números primos que hay en un intervalo [inicial, final]
inicial = int(input("ingresar el primer numero del intervalo: "))
final = int(input("ingresar el ultimo numero del intervalo: "))

print("Números primos en el intervalo [", inicial, ",", final, "]:")
for num in range(inicial, final + 1):
    if num > 1:
        es_primo = True
        for i in range(2, num):
            if (num % i) == 0:
                es_primo = False
                break
        if es_primo:
            print(num)



    

