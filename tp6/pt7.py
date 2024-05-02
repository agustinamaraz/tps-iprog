def validar_exponente():
    while(True):
        exponente = int(input("ingrese exponente: "))

        if exponente>=0:
            return exponente
        else:
            return 0

def pms (base,exponente):
    if exponente==0:
        potencia=0
    else:
        potencia=1

        for i in range(exponente):
            potencia*=base
    
    return potencia


#principal

base = float(input("ingresar base: "))
exponente = validar_exponente()

potencia = pms(base,exponente)
print(f"La potencia de {base} elevado a {exponente} es: {potencia}")
