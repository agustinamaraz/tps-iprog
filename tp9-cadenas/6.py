# 6. Solicitar el ingreso de una palabra clave por teclado. Controlar que la cadena ingresada tenga más de 6
# caracteres y al menos un número y un caracter en mayúsculas para que sea válido, en caso contrario mostrar
# un mensaje de error

# def validar_clave(clave):
#     # Verificar si la longitud de la clave es mayor a 6 caracteres
#     if len(clave) <= 6:
#         print("La clave debe tener más de 6 caracteres.")
#         return
    
#     # Verificar si la clave contiene al menos un número
#     if not any(char.isdigit() for char in clave):
#         print("La clave debe contener al menos un número.")
#         return
    
#     # Verificar si la clave contiene al menos una letra mayúscula
#     if not any(char.isupper() for char in clave):
#         print("La clave debe contener al menos una letra mayúscula.")
#         return
    
#     print("Clave válida.")

# Solicitar el ingreso de una clave por teclado
clave = input("Ingresar una clave: ")

# Validar la clave ingresada
# validar_clave(clave)

haynumero = False
for i,item in enumerate(clave):
    if item.isdigit():
        haynumero=True
        
if haynumero:
    print("hay un numero")
    
else: 
    print("no hay numero")

hayMayuscula = False    
for i,item in enumerate(clave):
    if item.isupper():
        hayMayuscula=True
        
if hayMayuscula:
    print("hay un mayuscula")
else: 
    print("no hay mayuscula")
    
if len(clave) <= 6:
    print("La clave debe tener más de 6 caracteres.")
else:
    print("cuenta con los mas de 6 caracteres")