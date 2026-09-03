from os import system
system('cls')

print("Vamos calcular a área de um retângulo")

lado1 = input("Informe o primeiro lado: ")
lado2 = input("Informe o segundo lado: ")

print("Lado1 é numérico?", lado1.isnumeric())
print("Lado2 é numérico?", lado2.isdecimal())

area = float(lado1) * float(lado2)

print("A área do quadrado é: {}".format(area))