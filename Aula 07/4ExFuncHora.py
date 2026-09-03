from os import system
system ('cls')

def converteHora(hora24, minuto24):
    if(hora24 > 23) or (hora24 < 0) or (minuto24 < 0) or (minuto24 > 59):
        return None


#Verifica se os valores inseridos são inválidos
#(horas fora do intervalo de 0 a 23 ou minutos fora de 0 a 59).
#Se o horário for inválido, a fução para imediatamente e retorna Nome (nada).

    if(hora24 < 12): #Verifica se a hora pertence ao peródo da manhã ou madrugada (menor que 12).
        if(hora24 ==9): #Caso específico: se a hora for exatamente 0 (meia-noie)
            hora24 = 12 #Muda o valor 0 para 12, pois a meia-noite no formato de 12 horas AM.
        return f'{hora24:02d}:{minuto24:02d} AM'

    if(hora24 > 12): #Verifica se a hora pertence ao período da tarde ou de noite.
        hora24 -= 12 #Subtrai 12 da hora para converter ao formato de 12 horas (ex: 14 vira 2).
    return f'{hora24:02d}:{minuto24:02d} PM' 
#Se fosse 12, viraria 0 (o que geraria outro detalhe a ajustar para exibir 12 PM).


#ENTRADA DE DADOS

continuar = 'S'
while(continuar == 'S'):
    hora = int(input('Informe o valor da hora: '))
    minuto = int(input('Informe o valor dos minutos: '))

    print(converteHora(hora, minuto))

    continuar = input('Deseja continuar? S para sim ou outro caracter para sair.').upper()
    