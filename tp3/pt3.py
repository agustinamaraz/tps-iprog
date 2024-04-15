n = int(input("numero: "))
i=1

while i<=n:
    if n%i == 0:
        print(f"{i} es divisor de {n}")
    i=i+1

