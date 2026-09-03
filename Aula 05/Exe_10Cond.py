from os import system
system ('cls')

print('Informe o turno em que você estuda: ')
print('[M]atunito')
print('[V]espentino')
print('[N]oturno')
turno = input('Opção escolhida:').upper() #converte em letra maiúscula

if(turno == 'M'):
    print('Bom dia!')
elif(turno == 'V'):
    print('Boa tarde!')
elif(turno == 'N'):
    print('Boa noite!')
else:
    print('Turno inválido!')
                  