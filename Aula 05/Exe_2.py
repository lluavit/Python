from os import system
system ('cls')

usuario = senha = ''
while (usuario == senha):
    usuario = input('Informe um nome de usuário: ')
    senha = input ('Informe a senha: ')
    if (usuario == senha):
        print('A senha não pode ser igual ao nome do usuário!')