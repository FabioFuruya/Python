# Gera relatório

import io
from Arquivos import tabCat
from Arquivos import tabProd

cat = tabCat()
prod = tabProd()

dicCategoria = cat.dicCat()
listaProdutos = prod.listProd()

relatorio = open('relatorio.txt', mode="w",encoding="utf-8")
for item in dicCategoria:
    titulo = f'{dicCategoria[item][0]}\n{dicCategoria[item][1]}\n\nProdutos\n'
    prod = []
    for itemP in listaProdutos:
        if str(itemP[2]) == item:
            valor = f'{itemP[8]:.2f}'
            produto = '''{:<60} | R$ {:>8}
            ''' . format(str(itemP[1].capitalize() + ' ' + itemP[3])[0:60], valor)
            prod.append(produto)
    prod.sort()     #ordena a lista por ordem alfanumérica
    lista = ''        
    i = 1
    for p in prod:
        lista += '{:>4}. {}\n' . format(i,p)
        i += 1
    divisor = ' Categoria '.center(80,'*')    
    relatorio.write(divisor + '\n' + titulo + lista + '\n\n')               # a partir daqui, começa a escrever o relatório
categorias = 'Total de Categorias: {:>4}'.format(len(listaProdutos))
produtos = 'Total de produtos: {:>4}'.format(len(ListaProdutos))
resumo = ' Resumo '.center(80,"*")
final = '{}\n\n{:>80}'.format(resumo, categorias,produtos)
relatorio.write(final)
relatorio.close()

