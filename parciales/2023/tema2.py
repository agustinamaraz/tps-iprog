# a todas las letras de la cadena que sean igual a la (letra ingresada por el usuario) cambiarla a MAYUSCULAS o MINISCULAS segun como estén
def cambiar_letra(cadena,letra):
    lista = list(cadena)
    
    for i,item in enumerate (lista):
        if item == letra.lower(): #si la letra esta en minuscula la cambia a mayus. en el caso de que la letra del parametro esté en miniscula ej. "a"
            lista[i] = item.upper()
        if item == letra.upper(): #si la letra esta en mayuscula la cambiar a minus. en el caso de que la letra del parametro esté en mayuscula ej, "A"
            lista[i] = item.lower()
    print("cadena cambiada: ")
    for item in lista:
        print(item,end="")
            
#principal
cambiar_letra("agustinA marAz","a")