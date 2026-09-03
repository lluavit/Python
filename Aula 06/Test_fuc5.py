from os import system
system('cls')

def potencia(num, exp = 2):
    resultado = pow(num, exp)
    return resultado

#....código
#....código

n = float(input('Digite o número: '))
e = int(input('Expoente: '))

print(f'Valor com expoente: {potencia(n, e)}')
print(f'Valor sem expoente: {potencia(n)}')