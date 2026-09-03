from os import system
system('cls')

def area_circulo(raio):
    PI = 3.14
    area = PI * pow(raio, 2)
    return area

#...código
#...código

r = float(input('Digite o valor do raio: '))
a = area_circulo(r)

print(f'O valor da área do círculo de raio {r} é igual a {a}')

