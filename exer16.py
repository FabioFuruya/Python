# faça um programa que pergunte em que turno vc estuda 
#peça para digitar:
# M - matutino , V = vespertino , N = noturno
# e imprimir a mensagem:
#Bom dia, Boa tarde, Boa noite

from os import system
system('cls')

print('Qual periodo você estuda?')
print('M=Matutino, V=Vespertino, N=Noturno')
periodo = (input('digite a letra: ')).upper()

if periodo != 'M' or periodo != 'V' or periodo != 'N':
    print('Digite uma opção válida!')
elif periodo == 'M':
    print('Bom dia!')
else:
    if periodo == 'V':
        print('Boa tarde!')
    else:
        print('Boa noite!')   


