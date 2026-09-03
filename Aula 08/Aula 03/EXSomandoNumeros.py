from os import system
system('cls')

print("Vamos fazer a soma de números inteiros")

num1 = input("Informe o primeiro número: ")
num2 = input("Informe o segundo número: ")

soma = num1 + num2

print("A soma entre {} e {} é igual {}".format(num1, num2, soma))

print("Toda informação recebida pelo comando input é do tipo", type(num1))

print("É necessário converter os dados em número, agora a soma vai ficar correta")

soma = int(num1) + int(num2)

print("A soma correta é {}".format(soma))