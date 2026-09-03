from os import system
system('cls')

def soma(*args):
    return sum(args)

#args não denine a quantidade de parâmetros
print(soma(1,3,5,8,9,10))