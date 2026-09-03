from os import system
system ('cls')

'''
criar um retângulo de 6 x 6, utilizando um caracter
ex:
@@@@@@
@@@@@@
@@@@@@
@@@@@@
@@@@@@
@@@@@@
'''

linha = 6
coluna = 6
simbolo = '&'

for l in range(linha):
    for c in range(coluna):
        print(simbolo, end='')
    print()

    
    # l para linhas - outer loop
    # c para colunas - inner lopp    