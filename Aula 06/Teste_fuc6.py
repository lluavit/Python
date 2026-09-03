from os import system
system('cls')


def potencia(num, exp2=1):
    '''Função que calcula a potência de um número.

    Parâmetros:
        num (float): número a ser elevado.
        exp2 (int): expoente da potência. O valor padrão é 1.

    Retorna:
        float: resultado da potência.
    '''
    resultado = pow(num, exp2)
    return resultado


# .... código
# .... código

n = float(input('Digite o número: '))
e = int(input('Expoente: '))

print(f'Valor com expoente: {potencia(n, e)}')
print(f'Valor sem expoente: {potencia(n)}')

print('-------------------------------------------------------------')
help(potencia)