# Programa que verifica se uma letra digitada é vogal ou consoante

from os import system
system('cls')

vogais = ['a','e','i','o','u']          #variável LISTA

letra = input('Digite uma letra: ')
if letra.lower() in vogais:
    print('Você digitou uma vogal!')
else:
    print('Você digitou uma Consoante!')        