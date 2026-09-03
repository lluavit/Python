from os import system
system ('cls')

qtd = 0
while (qtd <=0):
    qtd = int(input('Você quer saber a média de quantas notas? '))
    if (qtd <=0):
        print('A quantidade deve ser positiva!')

soma = 0
for i in range(0, qtd):
    nota = -1
    while (nota < 0) or (nota > 10):
        nota = float(input(f'Informe a nota {i + 1}: '))
        if (nota < 0) or (nota > 10):
            print('A nota deve estar entre 0 e 10.')
    soma += nota
print(f'A média das notas é {soma / float(qtd):.1f}')            