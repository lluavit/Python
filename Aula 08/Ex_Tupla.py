from os import system
system('cls')

lista_idades = []

while True:
    idade = int(input('Digite uma idade: '))
    if idade != -1:
        lista_idades.append(idade)
    else:
        break

tupla_idades = tuple(lista_idades)

qtd = len(tupla_idades)
total = sum(tupla_idades)
media = total / qtd

print(f'Total de idades digitada: {qtd}.')
print(f'A média das idades digitada é: {media:.2f}.')