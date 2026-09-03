from os import system
system('cls')

proprietarios = {}

while True:
    apto = int(input('Digite o apartamento: '))
    if apto != -1:
        proprietario = input("Proprietário: ")
        proprietarios.update({apto:proprietario})
    else:
        break

edificio = dict(sorted(proprietarios.items()))

for chave, valor in edificio.items():
    print(f'{chave} - {valor}')

print(f'Total de apartamentos: {len(edificio)}')


