from os import system
system ('cls')

i = 1
num = int(input('Informe o número quer ver na tabuada: '))
print('TABUADA DE', num, ':')
while i <11:
    print(f'{i} X {num} = {i * num}')
    i += 1