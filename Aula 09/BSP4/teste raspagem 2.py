import requests
from bs4 import BeautifulSoup

pagina = requests.get('https://quotes.toscrape.com/')

dados_pagina = BeautifulSoup(pagina.text, 'html.parser')
print(dados_pagina.prettify())

#todas_frases = dados_pagina.find_all('div', class_='quote')

#for div in todas_frases:
    #texto = div.find('span', class_='text').text
    #print(texto)

todas_frases = dados_pagina.find_all('span', itemprop='text')

for div in todas_frases:
    print(div.text)

