# calculadora 

from os import system
system('cls')

titulo = 'Calculadora simples'
print(titulo.center(80,'#'))

num1 = float(input('digite o primeiro número: '))
num2 = float(input('digite o segundo número: '))

opcao = ''
while opcao != 's':
    print('Escolha uma das opções do menu')
    print('(+) - adição\ln(-) - subtração\ln(*) - multiplicação\ln(/) - divisão\ln(s) - Sair')
    opcao = input('Operação: ')
    
    if opcao == '+':
        resultado = num1 + num2
    if opcao == '-':
        resultado = num1 - num2    
    if opcao == '*':
        resultado = num1 * num2    
    if opcao == '/':
        resultado = num1/num2       #falta verificar se num2 = zero
    if opcao == 's':
        break   
    print(num1,opcao,num2,'=',resultado)





