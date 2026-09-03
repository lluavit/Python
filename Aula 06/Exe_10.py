from os import system
system ('cls')

qtd = 0
while (qtd <= 0):
    qtd = int(input('Informe a quantidade de temperaturas: '))
    if (qtd <=0 ):
        print('A quantidade deve ser positiva!')
soma = 0
for i in range(0, qtd):
    temp = float(input(f'Informe a temperatura {i + 1}: '))
    if('maior'not in vars()) or (temp > maior):
        maior = temp
        #not in vars() verifica se a variável maior ainda não foi definida, cria e atribui a temperatura
    if('menor' not in vars()) or (temp < menor):
        menor = temp
    soma += temp 

media = soma / float(qtd)
print(f'A média das temperaturas: {media:.1f}')
print('Maior temperatura: ', maior)
print('Menor temperatura: ', menor)

