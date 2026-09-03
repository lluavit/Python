from os import system
system('cls')

from csv import reader

with open('exemplo.csv') as arquivo:
    leitor_csv = reader(arquivo)
    for linha in leitor_csv:
        print(f'C1 : {linha[0]} C2 : {linha[1]}  C3 : {linha[2]} C4 : {linha[3]} ')





