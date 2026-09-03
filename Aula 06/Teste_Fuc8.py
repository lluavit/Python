from os import system
system('cls')

def comida_favorita(**kwargs):
    for chave in kwargs:
        print(f'{chave} gosta de {kwargs[chave]}')

comida_favorita(Ana = 'Bacalhoada', Marcelo = 'Macarronada', Adriana = 'Feijoada')
