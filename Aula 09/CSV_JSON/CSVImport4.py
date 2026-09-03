from os import system
system('cls')

from csv import reader

with open('PS4_GamesSales.csv') as arquivo:
    leitor_csv = reader(arquivo)
    #next(leitor_csv) para não exibir cabeçalho
    for linha in leitor_csv:
        print(f'C1: {linha[0]} C2: {linha[1]} C3: {linha[2]} C4: {linha[3]} \
C5: {linha[4]} C6: {linha[5]} C7: {linha[6]} C8: {linha[7]} C9: {linha[8]}')