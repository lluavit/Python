from os import system
system ('cls')

pop_A = 80000
pop_B = 200000

#Na estrutura for será necessário chutar um limite alto de anos (ex: 500)
for anos in range(1, 501):
    pop_A += pop_A * 0.03
    pop_B += pop_B * 0.015

    if pop_A >= pop_B:
        print(f'Serão necessários {anos} anos.')
        break #Força a parada do loop

print(pop_A)
print(pop_B)