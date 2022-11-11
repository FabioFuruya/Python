from os import system
import random
system('cls')

# print(random.randint(0,100))

# número escolhido é par ou impar?
# o número escolhido é maior que 50 ou menor
#  (mais perto de 100 ou do 0)
# o número escolhido é primo

num = random.randint(0,100)

print(num)

if num % 2 == 0:
    print(' O número é par! ')
else:
    print(' o número é impar ')

if num > 50:
    print(' o número é maior que 50 ')
else:
    print(' o número é menor que 50 ')



