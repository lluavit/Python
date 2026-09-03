from os import system
system ('cls')

#Define os valores iniciais das populações e crescimento dos países 
pop_A = 80000
pop_B = 200000
cresc_A = 1.03
cresc_B = 1.015

#Realiza cálculo de anos 

ano = 0
while (pop_A <= pop_B):
    pop_A *= cresc_A
    pop_B *= cresc_B
    ano += 1

#Imprime o resultado

print('Serão necessários', ano, 'anos para que a população do país A')
print('Ultrapasse a população do país B.')

print(pop_A)
print(pop_B)