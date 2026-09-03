from os import system
system('cls')

from csv import DictReader

with open('exemplo.csv') as arquivos:
    leitor_csv = DictReader(arquivos, delimiter=',')
    for linha in leitor_csv:
     print(f'C1 : {linha['CotaMensal']} C2 : {linha['DataInicio']} \
C3 : {linha['NomeProprietario']} C4 : {linha['Usuario']}') 