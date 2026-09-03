from os import system
system ('cls')

salario = float(input('Informe o valor do salário do colaborador: '))

if(salario <= 280):
    percentual = 20
elif(salario <= 700):
    percentual = 15
elif(salario <= 1500):
    percentual = 10
else:
    percentual = 5

aumento = salario * (percentual / 100)
novoSalario = salario + aumento

print(f'Salário antes do reajuste: R$ {salario:.2f}')
print('Percentual de aumento: ', percentual, '%')
print(f'Valor do aumento: R$ {aumento:.2f}')
print(f'Novo salário: R$ {novoSalario:.2f}')