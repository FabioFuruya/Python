from os import system
import random
system('cls')

titulo ='JOGO DA ADIVINHAÇÃO'
print(titulo.center(50,'*'))

num = random.randint(1,10)
# print(num)

#chute = int(input('Chute um número: '))    <> é !=
#while chute 

tentativa = int(input('Adivinhe o número de 1 a 10: (0 para sair)'))
while tentativa > 0:
    if tentativa > num:
        print('o número é menor, tente novamente')
    elif tentativa < num:
        print('o número é maior, tente de novo')    
    else:
        print('Você acertou. PARABÉNS!')
        break    
    tentativa = int(input('Adivinhe o número de 1 a 10: (0 para sair)'))        
