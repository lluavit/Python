from os import system
system ('cls')


def primo(numero):
    '''Função lógica que retorna True se o valor informado for primo
    Entrada: número = número inteiro
    Retorna: True se número for primo e False se não for primo
    '''

    eprimo = False
    resto = 0

    for i in range(1, numero):
        if(numero %i) == 0: 
            resto += 1

    if resto == 1:
        eprimo = True 

    return eprimo

#ENTRADA DE DADOS
#ENTRADA DE DADOS


n = int(input('Entre com um valor inteiro positivo e maior que zero: '))

if primo(n):
    print(f'O número {n}, É PRIMO!')
else:
    print(f'O número, NÃO É PRIMO!')
        