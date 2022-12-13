import io
from Arquivos import tabCat
#importando a classe tabCat do arquivo denominado Arquivos.py
from Arquivos import tabProd

cat = tabCat() #instanciando o objeto da classe
prod = tabProd() #instanciando o objeto da classe

dicCategoria = cat.dicCat() #chamando a funcao/metodo do objeto
listaProdutos = prod.listProd() #chamando a funcao/metodo do objeto

relatorio = open("relatorio.txt", mode="w", encoding="utf-8")
#open metodo que no modo 'w' ele edita escreve cria um arquivo
for item in dicCategoria: #percorrendo(loop) no dicionario de categoria
    titulo = f'{dicCategoria[item][0]}\n{dicCategoria[item][1]}\n\nProdutos\n'
    
    prod = []
    #lista vazia para armazenar todos os produtos por categoria
    for itemP in listaProdutos: #percorre a listaProdutos do arquivo
        if str(itemP[2]) == item: #compar a coluna 2 com o valor de item
            valor = f'{itemP[8]:.2f}' #pego valor do produto e formato
            produto = '''{:<60} | R$ {:>8} 
            ''' . format(str(itemP[1].capitalize() + ' ' + itemP[3])[0:60], valor) 
            #pego a descricao e embalagem e formato a frase
            prod.append(produto)
            #adiciona produto na lista prod
    prod.sort()
    #ordeno a lista por ordem alfanumerico
    lista = ''
    i = 1
    #indice para ordem 'codigo' do relatorio
    for p in prod: #percorre a lista de produtos
        lista += '{:>4}. {}\n' . format(i,p)
        i+=1 #incrementa mais um na posicao do item no relatorio
    divisor = ' Categoria ' .center(80,'*')
    #divisor de relatorio
    relatorio.write(divisor + '\n' + titulo + lista + '\n\n')
    #escrever no arquivo texto
categorias = 'Total de Categorias: {:>4}' . format(len(dicCategoria))
produtos = 'Total de produtos: {:>4}' . format(len(listaProdutos))
resumo = ' Resumo ' .center(80,"*")
final = '{}\n\n{:>80}\n{:>80}' . format(resumo, categorias, produtos)
relatorio.write(final)
relatorio.close()
