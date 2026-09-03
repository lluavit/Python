from os import system
system ('cls')

# somar todos os digitos de um número.Exe: 15 = 1 + 5 = 6

numero = input('Entre com um número: ')

soma = 0
for digito in numero:
    soma += int(digito) # soma = soma + 1
print(f'A soma é igual a {soma}.')

