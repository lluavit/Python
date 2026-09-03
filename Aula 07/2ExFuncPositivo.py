from os import system
system ('cls')

def verifica_positivo(valor):
    if valor > 0:
        return 'P'
    else:
        return 'N'
 
#ENTRADA DE DADOS
#ENTRADA DE DADOS
 
numero = int(input('Informe um número: '))
print(f'Resultado: {verifica_positivo(numero)}')
 
 