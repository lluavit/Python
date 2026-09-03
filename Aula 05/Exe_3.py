from os import system
system ('cls')

#Validação do nome 
nome = '' 
while (len(nome) <=3):
    nome = input('Informe um nome: ')
    if (len(nome) <=3):
        print('O nome deve ter mais que três caracteres!')

#Validação da idade
idade = -1
while (idade < 0) or (idade > 150):
    idade = int(input('Informe a idade: '))
    if (idade < 0) or (idade > 150):
        print('Idade deve estar entre 0 e 150')

#Validação de salário
salario = 0
while (salario <= 0):
    salario = int(input('Informe o salário: '))
    if (salario <= 0):
        print('O salário deve ser maior que zero!')

#Validação do sexo
sexo = ''
while (sexo != 'F') and (sexo != 'M'):
    sexo = input('Informe o sexo: ').upper()
    if (sexo != 'F') and (sexo != 'M'):
        print('O sexo deve ser informado como M - masculino ou F - feminino')

#Validação do estado civil
civil = 'A'
while ('SCVD'.find(civil) < 0):
    civil = input('Informe o estado civil: ').upper()
    if ('SCVD'.find(civil) < 0):
        print('Estado civil deve ser informado S - solteiro, C - casado, V - viuvo ou D - divorciado')      