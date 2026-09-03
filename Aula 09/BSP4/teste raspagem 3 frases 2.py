import requests
from bs4 import BeautifulSoup

url = "https://www.pensador.com/melhores_frases_de_motivacao_e_inspiracao/"

try:
    response = requests.get(url)
    response.raise_for_status()  # Lança uma exceção para erros HTTP
    soup = BeautifulSoup(response.content, 'html.parser')
    article_content = soup.find('div', class_='article-content')
    if article_content:
        # Encontra todos os elementos <p> e <h2> dentro da div 'article-content'
        elements = article_content.find_all(['p', 'h2'])
        for element in elements:
            print(element.get_text(strip=True))
    else:
        print("Não foi possível encontrar a div 'article-content'.")

except requests.exceptions.RequestException as e:
    print(f"Erro ao acessar a página: {e}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")

    