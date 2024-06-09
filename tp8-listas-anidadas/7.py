# 7. Diseñar un programa modular que permita gestionar los productos de un comercio, las funcionalidades
# solicitadas son:
# 1. Registrar productos: para cada uno se debe solicitar, código, descripción, precio y stock. Agregar las
# siguientes validaciones:
    # a. El código no se puede repetir
    # b. Todos los valores son obligatorios
    # c. El precio y el stock no pueden ser negativos
# 2. Mostrar el listado de productos
# 3. Mostrar los productos cuyo stock sea menor a un valor dado
# 4. Incrementar el stock de un producto
# 5. Mostrar el producto de menor precio
# 6. Buscar el precio más alto de la lista de productos y a continuación listar los productos que lo poseen

def mostrar_mayor_precio(lista):
    maximo = -1
    
    for i in range(len(lista)):
        if lista[i][2] > maximo:
            maximo = lista[i][2]
            mayores_posiciones = []
            mayores_posiciones.append(i)
            
        elif lista[i][2] == maximo:
            mayores_posiciones.append(i)
            
            
    print("el precio mas alto encontrado fue de: $",maximo)
    
    for i in range(len(lista)):
        if i in mayores_posiciones:
            print("el producto que lo posee es: ",lista[i])
    

def mostrar_menor_precio(lista):
    minimo = 1000
    pos = -1
    for i in range(len(lista)):
        if lista[i][2] < minimo:
            minimo = lista[i][2]
            pos = i
            
    print("el prodcto con el menor precio es: ", lista[pos][1], " precio: ",minimo)

def incrementar_stock(lista):
    codigo = int(input("ingresar el codigo del producto para incrementar su stock: "))
    
    for i in range(len(lista)):
        if lista[i][0] == codigo:
            incremento = int(input("ingresar incremento: "))
            
            while incremento<=0:
                incremento = int(input("ingresar incremento VALIDO: "))
                
            lista[i][3] += incremento
            
    mostrar(lista)

def mostrar_producto_stock(lista):
    print("Mostrar los productos cuyo stock sea menor a un valor dado")
    stock = int(input("ingresar stock: "))
    for i in range(len(lista)):
        if lista[i][3] < stock:
            print(lista[i])

def es_valido(lista,codigo):
    
    if len(lista) > 0:
        for i in range(len(lista)):
            if lista[i][0] == codigo:
                return False
    
    return True

def mostrar(listado):
    for i,item in enumerate(listado):
        print(item)
            
        
def registrar():
    lista = []
    while True:
        
       
        codigo = int(input("ingresar codigo: "))
        while es_valido(lista,codigo) == False:
            print("Codigo existente, ingrese otro")
            codigo = int(input("ingresar codigo: "))
            
        while True:
            descripcion = input("ingresar descripcion, es obligatorio: ")
            if descripcion != "":
                break
            
        while True:
            precio = float(input("ingresar precio: "))
            if precio >= 0:
                break
            
        while True:
            stock = int(input("ingresar stock: "))
            if stock >= 0:
                break
        
        lista.append([codigo,descripcion,precio,stock])
        
        seguir = input("desea seguir cargando productos? s/n")
        
        if seguir != "s":
            return lista
        
#principal
listado = registrar()
mostrar(listado)
incrementar_stock(listado)
mostrar_producto_stock(listado)
# mostrar_menor_precio(listado)
# mostrar_mayor_precio(listado)