from os import system
system ('cls')

#soma dos algarismo de um número 
#na forma número modulo 10 pega o número mais a direta 

numero = int(input('Entre com um número: '))
soma = 0
resto = 0

while numero != 0:
    resto = numero % 10
    soma += resto
    numero = int(numero/10)
print(f'A soma é igual a {soma}.')    