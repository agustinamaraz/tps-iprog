def mayores_que(x,lista):
    repeticion=0
    for i in range(len(lista)):
        if (lista[i] > x):
            repeticion=repeticion+1
        
    print(f"cantidad de veces que se repitio {x} : {repeticion}")
    
    
#principal
lista=[7, 8, 6, 0, 4, 5, 10]

x = int(input("ingrese numero: "))

mayores_que(x,lista)















































































