from os import system
system ('cls')

def somaImposto(taxaImposto, custo):
    custo = custo + (custo * taxaImposto /100)
    return custo

taxa = float(input('Informe o valor da taxa: '))
custo = float(input('Informe o custo do produto: '))

custo = somaImposto(taxa, custo)

print(f'O preço com imposto é: {custo:.2f}')