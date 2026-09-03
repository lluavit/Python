from os import system
system ('cls')


print('Loja Quase Dois - Tabela de Preços')
for i in range(1,81):
    print(f'{i:2d} - R$ {(i * 1.99):6.2f}')
    #Para alinhamento dos valores a direita :d2
    #Para alinhamneto dos valores em reais :6.2f, margem de 6 e 2 casas decimais