# Faça um programa que receba 3 números e informe qual número é o maior e qual é o menor

# REVISAR !!! TÁ COM ERRO !!!

from os import system
system('cls')

num1 = input('informe o primeiro número: ')
num2 = input('informe o segundo número: ')
num3 = input('informe o terceiro número: ')

if num1.isalpha() or num2.isalpha() or num3.isalpha():
    print('inserir números válidos!')
else:
    if int(num1) < int(num2) and int(num1) < int(num3):
        print(num1,' é o menor')
        if int(num2) > int(num3):
            print(num3,' é o maior')
    elif int(num2) > int(num3):
        print(num2,' é o maior')
        print(num3,'é o menor')
    else:
        print(num3,' é o maior')
        print(num2,'é o menor')    
            