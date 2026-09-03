from os import system
system ('cls')

"""
Digitar a idade de 5 pessoas e 
calcular a média entre as idades.
"""

soma = 0
for i in range(1,6):
    idade = int(input(f'Entre com a idade {i}: '))
    soma = soma + idade 
media = soma / 5
print(f'A média das idades é: {media:.2f}')    