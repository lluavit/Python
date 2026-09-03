import requests
from bs4 import BeautifulSoup

# URL do site que contém a frase
url = 'https://www.pensador.com/melhores_frases_de_motivacao_e_inspiracao/'

# Fazendo a requisição para obter o conteúdo da página
response = requests.get(url)

# Verificando se a requisição foi bem-sucedida
if response.status_code == 200:
    # Parseando o HTML com BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Aqui, você precisa inspecionar o HTML da página para identificar onde a frase está
    # Como exemplo, vamos supor que a frase está dentro de uma tag <p> com uma classe específica
    # Você pode usar o navegador para inspecionar e descobrir o seletor correto
    
    # Exemplo fictício:
    # frase_element = soup.find('p', class_='frase-motivacional')
    
    # Como não tenho acesso ao HTML exato, vou te mostrar uma abordagem geral:
    # Suponha que a frase esteja dentro de um elemento <div> com uma classe específica
    # Você pode ajustar o seletor conforme necessário
    
    # Aqui está um exemplo genérico:
    frase_element = soup.find_all('div', class_='frase')  # Substitua pelo seletor correto
    
    if frase_element:
        frase = frase_element.get_text(strip=True)
        print('Frase encontrada:', frase)
    else:
        print('Não foi possível encontrar a frase na página.')
else:
    print('Falha ao acessar a página:', response.status_code)