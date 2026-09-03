from os import system
system('cls')
 
import random
 
def embaralhaPalavra(palavra):
    posicao = []
    tamanho = len(palavra)
    for i in range(0, tamanho):
        posicao.append(i)
    for i in range(0, tamanho):
        pos1 = random.randint(0, tamanho - 1)
        pos2 = random.randint(0, tamanho - 1)
 
        aux = posicao[pos1]
        posicao[pos1] = posicao[pos2]
        posicao[pos2] = aux
 
    retorno = ''
    for i in posicao:
        retorno += palavra[i]
 
    return retorno.upper()
 
#ENTRADA DE DADOS
 
palavra = input('Informe uma palavra: ')
print(embaralhaPalavra(palavra))