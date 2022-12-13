from requests import get
from bs4 import BeautifulSoup
from os import system
system('cls')

url = 'https://economia.uol.com.br/'

response = get(url)

html_soup = BeautifulSoup(response.text, 'html.parser')

secaoDinheiro = html_soup.find_all('section', class_='currencies')

print(len(secaoDinheiro))
print(secaoDinheiro)

info = html_soup.find_all('div', class_ = 'info')
print(len(info))
print(info)
print(info[0].text)

infoValor = html_soup.find_all('span', class_= 'value bra')
print(infoValor)

arquivoHtml = open('uol.txt', mode='w', encoding='utf-8')
arquivoHtml.write(html_soup.prettify())

valores = html_soup.find_all('a', class_='subtituloGrafico subtituloGraficoValor')
print("QTD Class: 'subtituloGrafico subtituloGraficoValor':", len(valores))

for valor in valores:
    print(valor.text)

