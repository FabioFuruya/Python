# Tupla

numeros = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove')
print(numeros[0])
print(numeros.index('dois'))
print(numeros.count('dois'))
print(len(numeros))

dez = ('dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove')
dezenas = ('','','vinte','trinta','quarenta','cinquenta','sessenta','setenta','oitenta','noventa')

from os import system
system('cls')

indice = int(input('Digite um número entre 0 e 99: '))
if indice < 10:
    extenso = numeros[indice]
elif indice < 20:
    extenso = dez[indice-10]
elif indice <= 99:
    dezena = int(indice / 10)
    numeral = indice % 10       # resto da divisão de 'indice' por 10
    if numeral > 0:
        extenso = dezenas[dezena] + ' e ' + numeros[numeral]
    else:
        extenso = dezenas[dezena]
print(extenso)




