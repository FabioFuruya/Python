#faça um programa que receba três números e informe qual número é o maior

from os import system
system('cls')

num1 = input('informe o primeiro número: ')
num2 = input('informe o segundo número: ')
num3 = input('informe o terceiro número: ')

if num1.isalpha() or num2.isalpha() or num3.isalpha():
    print('inserir números válidos!')
else:
    if int(num1) > int(num2) and int(num1) > int(num3):
        print('o número {} é o maior'.format(num1))
    elif int(num2) > int(num3):                         # else + if
        print('o número {} é o maior '.format(num2))
    else:
        print('o número {} é o maior'.format(num3))    
