# 11. Diseñar un programa que permita realizar el registro a una aplicación de estudiantes de una universidad, cada
# estudiante cuenta con los siguientes atributos: dni, clave, nombre, eMail y número de celular. Se solicita
# desarrollar las siguientes funcionalidades:
# a. Registrarse en la aplicación: Se solicitan los datos del estudiante con las siguientes validaciones:
    # ○ dni: es de tipo string debe tener 8 dígitos numéricos, luego de ingresar este valor se debe verificar que
    # no exista actualmente.
    # ○ clave: debe tener como mínimo una longitud de 6 caracteres, al menos una mayúscula y un número
    # ○ nombre: no puede tener números ni caracteres especiales y al menos 3 caracteres
    # ○ eMail: debe verificar que tenga el @ y que no se encuentre al inicio ni al final de la cadena ingresada.
    # ○ Número de Celular: debe incluir el código de área más el número sin el 15 (por ejemplo 388-4800123),
# es decir:
# ■ Los primeros dígitos corresponden al código de área y los valores solo pueden ser 388, 3886,
# 3887 y 3888
# ■ El guión es obligatorio
# ■ Los restantes números corresponden al número de celular y su longitud debe ser de 7 dígitos.
# El registro de estudiantes debe realizarse utilizando una estructura de tipo lista de listas que estará
# inicializada con 10 estudiantes para facilitar las pruebas.
# b. Buscar un estudiante: el programa solicitará el nombre y en función de ello mostrará lo siguiente:
    # ● Si se ingresa un vacío (enter), el programa mostrará la lista completa de estudiantes registrados
    # ● Si se ingresa un nombre, el programa mostrará los estudiantes cuyos nombres contengan al valor
    # ingresado, por ejemplo si ingresa ana, mostrará Mariana, Analía, etc.
# c. Ingresar (Login): debe solicitar el dni y la clave y verificar que coincida con algún estudiante registrado, si no
# existe emitirá el mensaje “Usuario o Clave incorrectos”. Si los datos son correctos mostrará el mensaje
# “Ingreso exitoso” y también mostrará el nombre y correo electrónico del estudiante.

estudiantes = [
    ["44949820", "agustina26A", "agustina", "agus@com", "388-5056596"],
    ["44949821", "agustina26A", "daianaagustina", "agus@com", "388-5056596"],
    ["45855525", "maxi26A", "maximiliano", "maxi@com", "3886-8888885"]
]

def validar_celular(cel):
    # Número de Celular: debe incluir el código de área más el número sin el 15 (por ejemplo 388-4800123),
    # Los primeros dígitos corresponden al código de área y los valores solo pueden ser 388, 3886,
    # 3887 y 3888
    # ■ El guión es obligatorio
    # ■ Los restantes números corresponden al número de celular y su longitud debe ser de 7 dígitos.
    
    codigo_valido = False
    if cel.find("-") == -1:
        print("debe tener el guion -")
    else:
        codigo,numero = cel.split("-")
        cod_permitidos = ["388", "3886","3887","3888"]
        if codigo in cod_permitidos and len(numero) == 7:
            codigo_valido=True
        else:
            print("codigos permitidos: ",cod_permitidos)
            print("ingresar codigos permitidos y numero mas de 7 digitos")
        
    return ( codigo_valido )

def validar_email(email):
    # eMail: debe verificar que tenga el @ y que no se encuentre al inicio ni al final de la cadena ingresada.
    arroba_existe = False
    if "@" in email:
        arroba_existe=True
    else:
        print("el email debe tener @")
        
    arrobas_correcta = False
    if email[0] != "@" and email[-1] != "@":
        arrobas_correcta = True
    else:
        print("el caracter @ no puede estar ni al inicio ni al final")
    
    return (arroba_existe==True and arrobas_correcta==True)

def validar_clave(clave):
    # clave: debe tener como mínimo una longitud de 6 caracteres, al menos una mayúscula y un número
    if len(clave) < 6:
            print("debe tenr como minimo 6 caracteres la clave")
            
    if clave.islower():
            print("debe tener como minimo 1 mayuscula")
            
    hay_digito = False
    for item in clave:
        if item.isdigit():
            hay_digito = True
            
    if hay_digito == False:
        print("la clave debe tener al menos 1 numero")
        
    return (len(clave)>=6 and clave.islower() == False and hay_digito==True)

def validar_nombre(nombre):
    # nombre: no puede tener números ni caracteres especiales y al menos 3 caracteres
    
    hay_numero = False
    for item in nombre:
        if item.isdigit():
            hay_numero=True
            
            
    if hay_numero==True:
        print("el nombre no pued etener numeros")
            
    if len(nombre) < 3:
        print("el nombre debe tener 3 o mas caracteres")
        
    if not nombre.isalpha():
        print("el nombre debe tener solo letras")
        
    return hay_numero==False and len(nombre)>=3 and nombre.isalpha()

def validar_dni(dni):
    # dni: es de tipo string debe tener 8 dígitos numéricos, luego de ingresar este valor se debe verificar que
    # no exista actualmente.
    dni_valido=True
    if (len(dni) > 7 and len(dni) < 9) and (dni.isdigit()):
        
        for item in estudiantes:
            if item[0] == dni:
                dni_valido=False
        
    else:
        print("el dni debe tener solo 8 caracteres y debe tener solo numeros")
        dni_valido=False
        
    return dni_valido
    

def registrarse():
    while True:
        dni = input("ingresar dni: ")
        
        if validar_dni(dni):
            break
           
    while True:
        nombre = input("ingresar nombre: ")
        if validar_nombre(nombre):
            break
        
    while True:
        clave = input("ingresar clave: ")
        if validar_clave(clave):
            break 
    
    while True:
        email = input("ingresar email")
        
        if validar_email(email):
            break
    
    while True:
        cel = input("ingresar numero de telefono: ")
        
        if validar_celular(cel):
            break
        
# b. Buscar un estudiante: el programa solicitará el nombre y en función de ello mostrará lo siguiente:
    # ● Si se ingresa un vacío (enter), el programa mostrará la lista completa de estudiantes registrados
    # ● Si se ingresa un nombre, el programa mostrará los estudiantes cuyos nombres contengan al valor
    # ingresado, por ejemplo si ingresa ana, mostrará Mariana, Analía, etc.

def buscar_estudiante():
    buscado = input("ingresar nombre de estudiante a buscar: ")
    
    if buscado == "":
        for item in estudiantes:
            print(item)
    else:
        for item in estudiantes:
            #trae todas las coincidencias de nombres con el nombre dado
            if item[2].find(buscado) != -1:
                print(item)
            
            #solo trae a la persona que sse llame exactamente a la nombre dado    
            # if item[2] == buscado:
            #     print(item)
                
                
# c. Ingresar (Login): debe solicitar el dni y la clave y verificar que coincida con algún estudiante registrado, si no
# existe emitirá el mensaje “Usuario o Clave incorrectos”. Si los datos son correctos mostrará el mensaje
# “Ingreso exitoso” y también mostrará el nombre y correo electrónico del estudiante.

def login():
    print("login-------------")
    dni = input("ingresar dni: ")
    clave = input("ingresar clave: ")

    encontrado=False

    for item in estudiantes:
        if item[1] == clave and item[0] == dni:
            encontrado=True
            print("INGRESO EXITOSO")
            print("Nombre: ",item[2], "Correo: ", item[3])

    if not encontrado:
        print("usuario o clave incorrectos")

#principals
# registrarse()
buscar_estudiante()
login()