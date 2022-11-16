#Faça um programa que peça dois números e imprima o maior deles
from os import system
system('cls')

num1 = (input('Digite o primeiro número: '))
num2 = (input('Digite o segundo número: '))

if num1 > num2:
    print('O número {} é maior que o número {}'.format(num1, num2))
else:
    print('O número {} é maior que o número {}'.format(num2, num1))
   