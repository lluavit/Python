from os import system
system ('cls')

numero = int(input('Informe o número que você quer ver na tabuada: '))
print('TABUADA DE', numero, ':')
for i in range(1,11):
    print(f'{numero} x {i} = {numero * i}')
    