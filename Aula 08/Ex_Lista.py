from os import system
system('cls')

cidades = []

while True: #loop infinito, é necessário um break
    cidade = input('Digite uma cidade: ')
    if cidade == 'sair':
        break
    else:
        cidades.append(cidade)

if len(cidades) > 0:
    cidades.sort()

    for cidade in cidades:#loop para descarregar uma cidade por linha
        print(cidade)
else:
    print('A lista de cidades está vazia!')               