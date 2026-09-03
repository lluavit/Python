from os import system
system('cls')
 
from csv import writer
 
# w - cria o arquivo novo e escreve nele
# r - abre para leitura
# a - abre para escrita sem apagar o que ja existe
#encoding permite acentos, caracteres especiais
 
with open('filmes.csv', 'a', newline='', encoding='utf-8') as arquivo:
    escritor_csv = writer(arquivo)
 
    filme = None
 
    escritor_csv.writerow(['Título', 'Gênero', 'Duração'])
 
    while filme != 'sair':
        filme = input('Nome do filme: ')
 
        if filme != 'sair':
            genero = input('Gênero: ')
            duracao = input('Duração: ')
 
            escritor_csv.writerow([filme, genero, duracao])
            