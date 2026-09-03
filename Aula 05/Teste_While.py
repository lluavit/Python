from os import system
system ('cls')

tentativas = 5

while tentativas > 0:
    print(f'Você tem {tentativas} tentativas.')
    tentativas = tentativas - 1 # loop diminuindo o contador

print('Fim do jogo!')    
