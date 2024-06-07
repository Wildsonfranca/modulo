#import modulo
#importa somente a função e nãp o modulo
from modulo import *

# #esntrada de dados 
# b = int(input('Informe o valor da base :'))
# h = int(input('Informe o valor da altura :'))

# # exibe o resultado do quadrilateros 
# print(f'Àrea do quadrilatero: {modulo.cacular_quadrilateros(b, h)}.')

#entrada de dados
# r = str(input('Informe o valor do raio :')).replace(',','.')
# r = float(r)

# # exibe a área da circunferencia
# print(f'Àrea do circulo: {calcular_circulo(r)}.')
#import modulo
#if__name__ == '__name__':
while True:
    exibir_menu()
    opcao = input('Opção desejada:')
    

    match opcao:
        case '1':
            b = int(input('base do quadrilatero:'))
            h = int(input('altura do quadilatero:'))
            print(f'Àrea : {calcular_quadrilatero(b,h)}')
            continue
        case '2':
            r = int(input('raio do circulo:'))
            print(f'Àrea:{calcular_circulo(r)}')
            continue
        case '3':
            b = int(input('Informe a base do triangulo:'))
            h = int(input('Informe a altura do triangulo:'))
            print(f'Àrea:{calcular_triangulo(b,h)}')
            continue
        case '4':
            b_menor = int(input('Informe a base menor do trapézio:'))
            b_maior = int(input('Informe a base maior do  trapézio:'))
            h = int(input('Informe a altura do trapézio:'))
            print(f'Àrea: {calcular_trapezio(b_menor,b_menor,h)}')
            continue
        case '5':
            print(f'saindo do progrograma:')
            break

    
   

