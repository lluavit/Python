from os import system
system ('cls')

def valorPagamento(valor, diasAtraso):
    if(valor < 0):
        return None
    if(diasAtraso > 0):
        multa = valor * 0.03
        adicionalAtraso = valor * (diasAtraso * 0.01)
        return valor + multa + adicionalAtraso
    else:
        return valor

#ENTRADA DE DADOS

valor = 1
while(valor != 0):
    valor = float(input('Informe o valor da prestação: '))
    if(valor != 0):
        diasAtraso = int(input('Informe a quantidade de dias em atraso: '))
        print(f'Valor a ser pago: {valorPagamento(valor, diasAtraso):.2f}')