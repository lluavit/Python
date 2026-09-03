from os import system
system('cls')

nota = int(input('Digite a nota do aluno: '))

if nota >= 9:
    print('Excelente!\nVocê tirou um A.')
elif nota >= 7:
    print('Bom trabalho!\nVocê tirou um B.')
elif nota >= 5:
    print('Você passou, mas precisa melhorar.\nSua nota é C.')
else:
    print('Você foi REPROVADO!\nSinto muito!')

    
            