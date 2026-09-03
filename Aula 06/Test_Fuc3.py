from os import system
system('cls')

def area_circulo(raio):
    PI = 3.14
    area = PI * pow(raio, 2)
    return area

def area_cilindro(raio,altura):
    area = area_circulo(raio) * altura
    return area

#...código
#...código

r = float(input('Digite o valor do raio do cilindro: '))
h = float(input('Digite o valor da altura do cilindro: '))
a = area_cilindro(r,h)

print(f'O valor da área do cilindro é {a}')
