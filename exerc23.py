# número primo é aquele que é divisível por 1 e por ele mesmo!

from os import system
from re import I
system('cls')


while True:
    num = int(input('Digite um número inteiro: '))
    if num >= 2:
        break
    else:
        print(f'Informe um número maior ou igual a 2')

resultado = 'O número é primo!'
i = 2
while i < num:
    resto = num % i
    if resto == 0:
        resultado = 'O número não é primo!'
        break
    i += 1
print(resultado)






