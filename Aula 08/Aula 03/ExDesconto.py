from os import system
system('cls')

valorCompra = float(input('Digite o valor da compra: R$ '))

if valorCompra > 200:
    desconto = 0.2
elif valorCompra > 100:
    desconto = 0.1
else:
    desconto = 0.05

valorFinal =  valorCompra - (valorCompra * desconto)

print(f'O valor final com desconto é de R$ {valorFinal:.2f}')

