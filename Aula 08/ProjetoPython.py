import random

def jogar_pedra_papel_tesoura():
    opcoes = ["pedra", "papel", "tesoura"]
    
    print("--- Bem-vindo ao Pedra, Papel e Tesoura! ---")
    
    # Jogador faz a escolha
    jogador = input("Escolha pedra, papel ou tesoura: ").strip().lower()
    
    # Validação da entrada do usuário
    if jogador not in opcoes:
        print("Opção inválida! Por favor, digite exatamente: pedra, papel ou tesoura.")
        return
        
    # Computador escolhe aleatoriamente
    computador = random.choice(opcoes)
    
    print(f"\nVocê escolheu: {jogador}")
    print(f"O computador escolheu: {computador}\n")
    
    # Determinando o vencedor
    if jogador == computador:
        print("O jogo terminou em EMPATE! ")
    elif (
        (jogador == "pedra" and computador == "tesoura") or
        (jogador == "papel" and computador == "pedra") or
        (jogador == "tesoura" and computador == "papel")
    ):
        print("Parabéns! Você VENCEU! ")
    else:
        print("O computador VENCEU! Tente novamente. ")

jogar_pedra_papel_tesoura()