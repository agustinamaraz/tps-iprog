# 14. Hacer un algoritmo que sea Idem Caso de Estudio 2 pero un cliente puede comparar más de un tipo de
# producto

# 2. En un supermercado se ingresa repetidamente el precio de un producto y el número de unidades a comprar por
# cliente (un ccliente puede comparar más de un tipo de
# producto). Validar que el precio del producto y el número de
# unidades no debe ser negativo ni cero. A partir de 5 unidades se realiza un descuento del 10% sobre el total de
# la compra. Los clientes se identifican por un número de orden consecutivo automático. Muestre el importe de
# dinero que debe pagar el cliente. El proceso finaliza al terminar la jornada laboral. Mostrar el número de
# orden del cliente que pagó el máximo importe y el total recaudado por el supermercado.


cant_cliente = int(input("Ingrese cantidad de clientes: "))
total_supermercado=0
max_importe=-100
cant_unidades=0
nro_orden=0

for i in range(1,cant_cliente+1):
    importe=0
    band=True
    print(f"N° de Orden: {i}")

    while band:
        respuesta = input("Desea comprar otro producto? (si/no): ").lower()

        if respuesta == "si":
            precio=float(input("Ingrese el precio del producto: "))
            unidades=int(input("Ingrese unidades: "))

            if precio>0 and unidades>0:
                importe = importe + precio*unidades
                cant_unidades=cant_unidades+unidades

                if cant_unidades >= 5:
                    total=total+(importe-importe*0.10)

                if importe > max_importe:
                    max_importe=importe
                    nro_orden=i

                print(f"Total a pagar: {total}")
                total_supermercado=total_supermercado+total
            else:
                print("los precios o unidades no pueden ser negativos")
        else:
            band=False

    print(f"El cliente que pagó el máximo importe es: {nro_orden}")
    print(f"Total recaudado por el supermercado: {total_supermercado}")


    


