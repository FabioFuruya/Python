# Digitar um número de 1 a 7 e retornar o dia da semana

diaSemana = ('segunda-feira','terça-feira','quarta-feira','quinta-feira','sexta-feira','sábado','domingo')
# print(diaSemana)

numero = int(input('Digite um número de 1 a 6, onde 0 = segunda-feira: '))
if numero <= 7:
    print(diaSemana[numero])


