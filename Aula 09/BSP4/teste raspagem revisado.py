from requests import get
from bs4 import BeautifulSoup
from os import system, name

# Limpa a tela dependendo do sistema operacional
system('cls' if name == 'nt' else 'clear')

url = 'http://economia.uol.com.br/'

try:
    response = get(url)
    response.raise_for_status()  # Verifica se a requisição foi bem-sucedida
except Exception as e:
    print(f"Erro ao fazer requisição: {e}")
    exit()

html_soup = BeautifulSoup(response.text, 'html.parser')

# Busca pela seção de moedas
secao_dinheiro = html_soup.find_all('section', class_='currencies')
print(f"Quantidade de seções 'currencies': {len(secao_dinheiro)}")
print(secao_dinheiro)

# Busca por informações adicionais
info = html_soup.find_all('div', class_='info')
print(f"Quantidade de divs 'info': {len(info)}")
if info:
    print(f"Primeiro conteúdo de 'info': {info[0].text}")

# Busca pelos valores
info_valor = html_soup.find_all('span', class_='value bra')
print(f"Quantidade de spans 'value bra': {len(info_valor)}")

# Salvando o HTML no arquivo
with open('uol.txt', mode='w', encoding='utf-8') as relatorio:
    relatorio.write(html_soup.prettify())

# Busca pelos links de valores gráficos
valores = html_soup.find_all('a', class_='subtituloGrafico subtituloGraficoValor')
print(f'QTD Class "subtituloGrafico subtituloGraficoValor": {len(valores)}')
for valor in valores:
    print(valor.text)

    