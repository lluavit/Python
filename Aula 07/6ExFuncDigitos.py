from os import system
system ('cls')

def qtdDigitos(digito):
    if(digito == 0):
        return 0
    return 1 + qtdDigitos(int(digito /10))
#Divisão base 10 o computador somente conta os inteiros.
#ENTRADA DE DADOS

digito = int(input('Informe um número inteiro: '))
print(f'O número {digito} possui {qtdDigitos(digito)} digitos.')