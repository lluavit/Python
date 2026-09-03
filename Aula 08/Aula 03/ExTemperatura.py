from os import system
system('cls')


temp = int(input('Digite uma temperatura: '))

if temp < 10:
    print('Está muito frio!')
elif temp < 20:
    print('Está fresco!')
else:
    print('Está quente!')

    

