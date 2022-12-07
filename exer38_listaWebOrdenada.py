# link Extrair dados:
# https://www.imdb.com/search/title/?release_date=2020-01-01,2020-12-31&sort=user_rating,desc

from requests import get
from bs4 import BeautifulSoup
from os import system
system('cls')

# dataInicial = input('Digite a data inidical no formado YYY-MM-DD ')
# dataFinal = input('Digite a data final, no formato YYY-MM-DD ')
# url = 'https://www.imdb.com/search/title/?release_date=' dataInicial2020-01-01,2020-12-31&sort=user_rating,desc'

url = 'https://www.imdb.com/search/title/?release_date=2020-01-01,2020-12-31&sort=user_rating,desc'
response = get(url)

html_soup = BeautifulSoup(response.text,'html.parser')

filmes = html_soup.find_all('div',class_='lister-item mode-advanced')
print(len(filmes))

for indice in range(10):        # vai buscar somente os 10 primeiros
    filme_dados = filmes[indice]
    nome = filme_dados.h3.a.text
    lancamento - filme_dados.h3.find('span',class_='lister-item-yeartext')
    votos = filme_dados.find('span',attrs = {'name':'nv'})
    episodios = filme_dados.h3.find('small','text-primary unbold')

    x = ''
    if episodios is not None:               # se o filme não tiver episódios
        ep = filme_dados.find.all('a')
        x = '- Episodio: ' + ep[2].text
    print(f'''
    {indice+1} - {nome} {lancamento.text}\nPontuação:
    {filme_dados.strong.text} - votos: {votos.text}
    ''')




