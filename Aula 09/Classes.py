from os import system
system('cls')

class Automovel:
    def __init__(self, placa):
        self.placa = placa

    def get_placa(self):
        return self.placa

    def dirigir(self, velocidade):
        print(f'Estou dirigindo a {velocidade} KM/H.')

#...código...código....        
meu_carro = Automovel('XYO0011')            
outro_carro = Automovel ('ZZZ9911')

print(meu_carro.get_placa())
print(outro_carro.get_placa())

meu_carro.dirigir(100)
outro_carro.dirigir(80)