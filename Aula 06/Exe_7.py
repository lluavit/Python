from os import system
system ('cls')

termo = 0
while (termo <=0):
    termo = int(input('Você quer a serie de Fibonaci até qual termo? '))
    if (termo <= 0):
        print('O termo deve ser positivo!')
primeiro = 1
print(primeiro)
segundo = 1
for i in range(1, termo):
    print(segundo)
    terceiro = primeiro + segundo
    primeiro = segundo
    segundo = terceiro        