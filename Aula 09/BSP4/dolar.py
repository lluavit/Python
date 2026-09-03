import requests
from bs4 import BeautifulSoup

link = 'https://www.google.com/search?q=cotacao+dolar'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36'}
requisicao = requests.get(link, headers=headers)
print(requisicao)
#print(requisicao.text)

site = BeautifulSoup(requisicao.text, 'html.parser')
#print(site.prettify())

#titulo = site.find('title')
#print(titulo)

pesquisa = site.find('span', class_="SwHCTb")
print(pesquisa.get_text())


# <span class="chart-info-val ng-binding" ng-bind="graphicView.bidvalue">5,598</span>



