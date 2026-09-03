from os import system
system('cls')

def retornaInvertido(valor):
    return valor[::-1]

#Fatiamento [inicio:fim:passo]
#Colchetes após uma variável é um fatimaneto.

numero = input('Informe um número: ')
print(retornaInvertido(numero))