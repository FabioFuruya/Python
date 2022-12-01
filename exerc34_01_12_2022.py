from os import system
import os.path, datetime
system('cls')

arquivo = 'categorias.csv' #caminho do arquivo
categorias = open(arquivo, 'r' , encoding='utf-8')
# abre somente leitura o caminho do arquivo e armazena em uma variável
dicCategoria = {} #instanciar uma variavel do tipo dicionário

if os.path.isfile(arquivo):
    for line in categorias:
        colunas = line.strip().split(';')
        dados = [colunas[1], colunas[2]]
        dicCategoria[colunas[0]] = dados

    categorias.close()    #fecha o arquivo
    print(dicCategoria)    #exibe o dicionário


