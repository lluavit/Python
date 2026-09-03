from os import system
system ('cls')

soma = 0
for i in range(0,5):
    numero = int(input('Informe um número: '))
    soma += numero
print(f'A soma dos números digitados é {soma}.')
print(f'A média dos números digitados é {soma / 5:.1f}.')

