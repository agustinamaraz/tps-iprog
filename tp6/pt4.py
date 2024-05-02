def bienvenida (n):
    nro = 20
    car = '-'
    print(car*nro)
    print('Hola ', n)
    print(car*nro)
    print('Este algoritmo calcula el seno ')
    print('de un ángulo en grado sexagesimal')
    print('con la serie de Taylor hasta un ')
    print('término determinado por Ud. ')
    print(car*nro)
def verificaP():
    while True:
        x = float(input('Ángulo en sexagesimales x>=0:'))
        if x >= 0:
            return x
    
def verificaMenor10():
    while True:
        m10 = int(input('N° de términos [1,10]:'))
        if m10 >= 1 and m10 <= 10:
            return m10

def factorial(x):
    p = 1
    for i in range(1, x+1):
        p *= i
    return p
def potencia(base, exponente):
    p = 1
    for i in range(exponente):
        p *= base
    return p


from math import pi,sin

#Principal
nombre = input('Ingrese su nombre:')
bienvenida(nombre)
a = verificaP()
x = a*pi/180 #radianes
m = verificaMenor10() #valor final términos
suma = 0
for n in range(m):
    t = 2*n+1
    suma += potencia(-1,n)/factorial(t)*potencia(x,t)
print('Seno calculado = ', suma)
print('Seno función interna = ',sin(x))
