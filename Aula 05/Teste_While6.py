from os import system
system ('cls')

n = 0
while True: 
    if (n % 2) ==0:
        n += 1
        continue
    print(f'O último valor de n é {n}.')
    n += 1
    if n > 9:
        break
