from os import system
system ('cls')

#Publicar um produto com comissão de 10% se for acima de R$20,00

valor = float(input('Digite o valor do seu produto em R$: '))

while valor > 20:
    valor = (valor * 0.10) + valor 
    print(f'O valor final do seu produto será de R$ {valor:.2f}')
    break