# Verificar se o número é par

from os import system
system('cls')

num = (input('digite um número: '))

if num.isalpha() :
    print('não é um número!')
else:
    if int(num) % 2 == 0:   #resto da divisão por 2
        print(num , 'é um número par!')
    else:
        print(num , 'é um nùmero impar!')