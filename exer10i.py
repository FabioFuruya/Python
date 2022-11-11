from os import system
system('cls')

num1 = input('digite o valor: ')
divisor = input('digite o valor div: ')

if num1.isalpha():
    print('não é número!')

if int(divisor) > 0 :
    print('Posso dividir!')
    divisao = int(num1) / int(divisor)
    print(f'Resultado da divisão é: {divisao}')
    print('2. Resultado da divisão é: {:.2f}'.format(divisao))
else:
    print('valor 0. Não pode ser dividido!')
