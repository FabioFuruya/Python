nota1 = float(input('informe a nota1: '))
nota2 = float(input('informe a nota2: '))
nota3 = float(input('informe a nota3: '))

media = (nota1+nota2+nota3)/3

if media < 7:
    print('Reprovado')
elif media >= 7 and media < 10:
    print('Aprovado')
else:
    print('Aprovado com Distinção')
