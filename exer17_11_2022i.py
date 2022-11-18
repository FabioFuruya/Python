# para copiar a linha onde está o cursor: Alt + Shift + seta para baixo

from os import system
system('cls')

nota1 = input('informe a nota1: ')
nota2 = input('informe a nota2: ')
nota3 = input('informe a nota3: ')
nota4 = input('informe a nota4: ')

if nota1.isalpha() or nota2.isalpha() or nota3.isalpha() or nota4.isalpha():
    print('inserir somente números!')
else:
    media = float((nota1 + nota2 + nota3 + nota4)/4)
    if media<7:
        print('Reprovado')
    elif media==10:
        print('Aprovado com Distinção')    
    else:    
        print('Aprovado')