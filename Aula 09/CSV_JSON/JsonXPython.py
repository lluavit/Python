from os import system
system('cls')

import json

with open('sample1.json', 'r', encoding='utf-8') as arquivo:
    sample1_dict = json.load(arquivo)

for chave, valor in sample1_dict.items():
    print({chave: valor})

       