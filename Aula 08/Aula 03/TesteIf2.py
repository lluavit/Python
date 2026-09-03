from os import system
system('cls')

idade = int(input('Digite a sua idade: '))

#if idade < 18:
    #print('Menor de Idade!')
#elif idade >= 18 and idade < 60:
 #   print('Maior de Idade!')
#else:
 #   print('Idoso!')

if idade < 18:
    print('Menor de Idade!')
elif 18 <= idade < 60:
    print('Maior de Idade!')
else:
    print('Idoso!')

    

