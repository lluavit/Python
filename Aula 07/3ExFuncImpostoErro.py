from os import system
system ('cls')

def somaImposto(taxaImposto, custo):
    custo = custo + (custo * taxaImposto /100)
    return custo

#O loop while true froça o programa a repetir até que os dados estejam corretos
while True:
    try:
        taxa = float(input('Informe o valor da taxa: '))
        custo = float(input('Informe o custo do produto: '))
#Se a conversão para float der certo, o break sai do loop while
        break
    except ValueError:
        print('Erro: por favor, digite apenas números válido! Use ponto para decimais.')

custo = somaImposto(taxa, custo)

print(f'O preço com imposto é: {custo:.2f}')        