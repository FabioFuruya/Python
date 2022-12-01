

class tabCat:
    def dicCat(self):
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
        return dicCategoria

class tabProd:
    def listProd(self):
        arquivo = 'produtos.csv'

        if os.path.isfile(arquivo):
            produtos = open(arquivo, 'r',encoding='utf-8')              # utf-8 - trabalha com acentuação     'r' - somente leitura
            listaProdutos = []    
            for linha in produtos:
                colunas = linha.strip().split(";")                
                colunas[0] = int(colunas[0])
                colunas[2] = int(colunas[2])
                colunas[4] = int(colunas[4])
                colunas[5] = int(colunas[5])
                colunas[6] = int(colunas[6])
                colunas[7] = int(colunas[7])
                colunas[8] = float(colunas[8])
                colunas[9] = float(colunas[9])
                listaProdutos.append(colunas)
            produtos.close()
            return listaProdutos
        