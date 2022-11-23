# Estrutura de repetição usando FOR

compras = ['Arroz','Feijão','Macarrão','Carne','Queijo']

for  item in compras:
    print(item)

for i in range(0,10):
    print(i)

# lista_numerica = [1,2,3,4]
# x == 0
# for x in range(0,10):
#    print()

multiplicador = int(input('Informe o valor do multiplicador: '))
for i in range(1,11):
    print(f'{multiplicador} x {i} = {multiplicador*i}')

for i in range(0,101,2):             # 2 é o incremento
    print(i)

for i in range(101,0,-2):             # -2 é o decremento
    print(i)

num = [9,2,1,5,7,6,3,4,8]
soma = 0
for i in num:
    soma += i       # soma = soma + i
print(soma)    




