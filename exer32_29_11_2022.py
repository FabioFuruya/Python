# Programa gerador de recibos

from exer32_RECIBO import Recibo
from os import system
system('cls')

novoRecibo = Recibo('Adolfo')
novoRecibo.valor = 1258.99
novoRecibo.descricao('desenvolvimento programas Python')


print(novoRecibo)

