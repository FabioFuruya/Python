#faça um programa que receba dois números e informe qual número é o maior

from os import system
system('cls')

num1 = input('informe o primeiro número: ')
num2 = input('informe o segundo número: ')

if num1.isalpha() or num2.isalpha():
    print('inserir números válidos!')
else:
    if int(num1) > int(num2):
        print('o número {} é maior que {}'.format(num1,num2))
    else:
        print('o número {} é maior que o número {}'.format(num2,num1))