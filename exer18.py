# conversor de medidas
#faça um programa que receba uma medida em centímetros e o usuário escolha a medida de conversão
#

from os import system
system('cls')
titulo = 'CONVERSOR DE MEDIDAS'
print(titulo.center(40,'*'))

medida = float(input('Informe a medida em centimetros: '))

print('\nEscolha para qual unidade deseja converter')
print('1 - Polegada\n2 - Pé \n3 - Jarda')

menu = input('Opção: ')

valorPolegada = 2.54
valorPe = 30.48
valorJarda = 91.44

if menu == '1':
    polegada = medida/valorPolegada
    resultado = str(f'{medida:.4f} centimetros correspondem a {polegada:.4f} Polegadas')
elif menu == '2':
    pes = medida/valorPe
    resultado = str(f'{medida:.4f} centimetros correspondem a {pes:.4f} Pés')
elif menu == '3':
    jarda = medida/valorJarda
    resultado = str(f'{medida:.4f} centimetros correspondem a {jarda:.4f} Jardas')    
else:    
    resultado =str('Você não escolheu uma das opções válidas!')
print(resultado)





