# 1. Una institución bancaria tiene una aplicación que recibe una lista con los movimientos de las cuentas bancarias
# de sus clientes mediante un servicio externo. Para cada cuenta se recibe el número de cuenta, nombre y
# apellido del cliente, importe, fecha del movimiento y el tipo de movimiento (E=Extracción, D=Depósito). El
# formato de cada cuenta está dado por una cadena de caracteres donde cada atributo de una cuenta se
# encuentra separado por comas.
# Por ejemplo:
# 27200123456,MARIA FERNANDEZ,0000500000,30-05-2021,E
# 27200321654,CARLOS TORRES,0000400045,31-05-2021,D
# 27200987125,LAURA AQUINO,0000230000,30-05-2021,D
# 27200852369,MARTIN ESTRADA,0000700000,25-05-2021,E
# 27200123456,MARIA FERNANDEZ,0000250099,31-05-2021,E
# 27200795169,FLORENCIA ROBLES,0000350080,20-05-2021,D
# Tenga en cuenta que:
# - Los 2 últimos dígitos del importe corresponden a los centavos, o sea que el valor 0000500000 es
# equivalente a 5000 pesos.
# - La fecha solo tiene carácter informativo por lo que debe guardarse como un string.
# Se solicita lo siguiente:
# 1. Procesar la lista recibida y guardar los datos recibidos en una lista.
# 2. Mostrar la lista con las cuentas obtenidas.
# 3. Mostrar los movimientos correspondientes a depósitos y el total acumulado.
# 4. Mostrar los movimientos de una cuenta.
# Nota: utilice los datos del ejemplo para validar el programa

lista = [
    "27200123456,MARIA FERNANDEZ,0000500000,30-05-2021,E",
    "27200321654,CARLOS TORRES,0000400045,31-05-2021,D",
    "27200987125,LAURA AQUINO,0000230000,30-05-2021,D",
    "27200852369,MARTIN ESTRADA,0000700000,25-05-2021,E",
    "27200123456,MARIA FERNANDEZ,0000250099,31-05-2021,E",
    "27200795169,FLORENCIA ROBLES,0000350080,20-05-2021,D"
]

def encontrar_nombre(lista_nueva):
    nombre_a_buscar = input("ingresar nombre a buscar: ").upper() #si no esta el upper discrimina entre mayusculas y minusclas
    
    for i,item in enumerate(lista_nueva):
        if item[1].find(nombre_a_buscar) != -1:
            print("CUENTA ENCONTRADA: ",item)

def mostrar_cuenta(lista_nueva):
    numero_cuenta = input("Numero de cuenta a buscar: ")
    print("CUENTA SOLICITADA: ")
    for i,item in enumerate(lista_nueva):
        if item[0] == numero_cuenta:
            print(item)

def parsear_a_decimal (importe):
    return round(int(importe) / 100, 2)
    
def mostrar_segun_deposito(lista):
    print("MOSTRAR CUENTA SEGUN TIPO MOVIMIENTO DEPOSITO: ")
    total = 0
    for cuenta in lista:
        if cuenta[4] == "D":
            print(cuenta)
            total+=parsear_a_decimal(cuenta[2])
        
    print("total acumulado: ", total)
    
def cargar_nueva_lista():
    
    lista_nueva = []
    for i,item in enumerate(lista):
        lista_nueva.append(item.split(","))
        
    return lista_nueva
def mostrar_nueva_lista(lista_nueva):
    
    print("NUEVA LISTA:")
    for i,item in enumerate(lista_nueva):
        print(i,"CUENTA: ",item)
#principal
lista_nueva = cargar_nueva_lista()
mostrar_nueva_lista(lista_nueva)
mostrar_segun_deposito(lista_nueva)
mostrar_cuenta(lista_nueva)
encontrar_nombre(lista_nueva)