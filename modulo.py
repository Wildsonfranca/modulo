#

def exibir_menu():
    print('1 calcular quadrilatero')
    print('2 calcular círculo')
    print('3 calcular triangulo')
    print('4 calcular trapézio')
    print('5 sair do programa ')

def calcular_quadrilatero(b, h):
    a = b * h
    return a 

# função da circunferencia 
def calcular_circulo(r):
    a = 3.14 *r**2
    return a
#função triangulo
def calcular_triangulo(b, h):
    a = (b * h)/2
    return a 
#trapezio
def calcular_trapezio(b_menor,b_maior, h):
    a = ((b_menor + b_maior)*h)/2
    return a
