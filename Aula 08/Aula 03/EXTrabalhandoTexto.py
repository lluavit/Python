from os import system
system("cls") # No Linux/Mac use: system("clear")

nomecompleto = input("Informe o seu nome completo: ")

# 1. Quantidade de caracteres
print("1. Quantidade de caracteres:", len(nomecompleto))

# 2. Nome em maiúsculo
print("2. Nome em maiúsculo:", nomecompleto.upper())

# 3. Nome em minúsculo
print("3. Nome em minúsculo:", nomecompleto.lower())

# 4. Primeira letra em maiúsculo
print("4. Primeira letra em maiúsculo:", nomecompleto.capitalize())

# 5. Somente o primeiro nome
espaco = nomecompleto.find(" ")
print("5. Somente o primeiro nome:", nomecompleto[0:espaco])

# 6. Nome sem espaços
print("6. Nome sem espaços:", nomecompleto.replace(" ", ""))

# 7. Verifica se tem somente letras
print(
"7. Tem somente letras? (temos que tirar os espaços para verificar):",
nomecompleto.replace(" ", "").isalpha()
)

# 8. Verifica se é alfanumérico
print(
"8. É alfanumérico? tem letras ou números (temos que tirar os espaços para verificar):",
nomecompleto.replace(" ", "").isalnum()
)

# 9. Quebrar o texto em cada espaço
print("9. Quebrar o texto a cada espaço em branco:", nomecompleto.split(" "))

# 10. Centralizar o nome entre *
print("10. Centralizar o nome entre *")
print(nomecompleto.center(80, "*"))