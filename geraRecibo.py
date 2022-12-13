from Recibo import Recibo
from os import system
system('cls')

novoRecibo = Recibo('Adolfo')
novoRecibo.valor = 1258.99
novoRecibo.descricao('desenvolvimento de sistemas em Python')

#print(novoRecibo.nome, novoRecibo.valor, novoRecibo._descricao)
print(novoRecibo)