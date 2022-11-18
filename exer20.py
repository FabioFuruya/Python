# Faça um programa que receba três números e mostre-os em ordem decrescente

from os import system
system('cls')

num1 = float(input('digite o primeiro número: '))
num2 = float(input('digite o segundo número: '))
num3 = float(input('digite o terceiro número: '))

if num1 > num2 and num1 > num3:
    maior = num1
elif num2 > num3: 
    maior = num2
else:
    maior = num3

if num1 < num2 and num1 < num3:
    menor = num1
elif num2 < num3:
    menor = num2
else:
    menor = num3

if (num1 < num3 and num1 > num2) or (num1 < num2 and n)
  

