# jogo papel-pedra-tesoura

from os import system
import random

system('cls')

titulo = ' | Pedra | Papel | Tesoura | '
print(titulo.center(80,'*'))

opcao = 'S'
contadorJogadas = 0
contadorJogador = 0
contadorComputador = 0

while opcao.upper() =='S':
    system('cls')
    computador = random.randint(0,2)
    jogador = int(input('''Escolha uma opção para se jogar
    [0] Pedra
    [1] Papel
    [2] Tesoura
    Digite sua escolha: '''))
    if jogador > 3:
        resultado = f'Você não escolheu uma opção válida'
    else:
        contadorJogadas += 1
        pecas = ('Pedra','Papel','Tesoura')
        print(f'Você escolheu {pecas[jogador]}')
        print(f'Computador escolheu {pecas[computador]}')
        tabela = ((0,1,-1),(-1,0,1),(1,-1,0))
        jogada = tabela[computador][jogador]
        if jogada == 0:
            resultado = f'empate'
        elif jogada == 1:
            resultado = f'você ganhou'
            contadorJogador += 1
        elif jogada == -1:
            resultado = f'o computador ganhou'
            contadorComputador += 1
    print(resultado)
    opcao = input('Jogar novamente? (S) para Sim!')
system('cls')
print('Resumo do jogo'.center(60,'*'))
print(f'Quantidade de jogadas: {contadorJogadas}')
print(f'Você ganhou: {contadorJogador} jogada(s)')
print(f'Computador ganhou: {contadorComputador} jogada(s)')         #somar qto cada um ganhou e subtrair da qtde de jogadas = empates
                                                                    #pode ser que dê número negativo



    





