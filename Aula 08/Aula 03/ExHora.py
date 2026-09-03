from os import system
system('cls')

hora = int(input('Digite um horário: '))

if hora < 12:
    print('Bom Dia!')
elif hora < 18:
    print('Boa Tarde!')
else:
    print('Boa Noite!')
    
       