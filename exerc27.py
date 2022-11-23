# Lista de compras

from os import system
system('cls')

titulo ='Calcular lista de compras'
print(titulo.center(80,'*'))

produtosDesc = []
produtosPreco = []
NumeroItens = int(input('Informe o número de item desejados: '))
for i in range(0,NumeroItens):
    NomeProduto = input(f'Nome do Produto{i}: ')
    PrecoProduto = float(input(f'Preço do {NomeProduto}: '))
    produtosDesc.append(NomeProduto)
    produtosPreco.append(PrecoProduto)

total = 0
for i in range(0,NumeroItens):
    print(f'{produtosDesc}[i] - R$ {produtosPreco} ')
    total += produtosPreco[i]
print(f'Total: R$ {total}')    

print(produtosDesc)
print(produtosPreco)

