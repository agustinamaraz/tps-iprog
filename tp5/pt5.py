op=0
i=0
band=True
total_impresoras=0
en_uso=0
en_mantenimiento=0

while band:
    i+=1
    print(f"Impresora n° {i}")

    cant_impresiones=int(input("Ingrese cantidad de impresiones: "))
    cant_dias_ult_revision=int(input("Ingrese cantidad de dias desde su ultima revision: "))

    if cant_dias_ult_revision<=30:
        if cant_impresiones < 500: 
            print(f"La impresora puede seguir en uso")
            en_uso+=1

        elif cant_impresiones >= 500 and cant_impresiones <=700:
            print("llamar al servicio técnico dentro de 10 días")
            en_uso+=1

        else: #cant_impresiones > 700
            print("llevar al servicio tecnico para realizar mantenimiento")
            en_mantenimiento+=1

    else:
        if cant_impresiones < 500:
            print("puede seguir en uso")
            en_uso+=1

        else:
            print("llevar al servicio tecnico para realizar mantenimiento")
            en_mantenimiento+=1


    total_impresoras+=1
    respuesta = input("Desea ingresar otra impresora?: (si/no)")

    if respuesta == "si":
        band=True
    else:
        band=False

print(f"total de impresoras revisadas: {total_impresoras}")
print(f"porcentaje de impresoras en uso: {(en_uso*100)/total_impresoras}")

