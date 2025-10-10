import random

def jogo_adivinhacao():
    # Gera um número aleatório entre 0 e 100
    numero_secreto = random.randint(0, 100)
    tentativas = 0
    acertou = False

    print("🎯 Bem-vindo ao Jogo de Adivinhação!")
    print("Tente adivinhar o número entre 0 e 100.\n")

    # Loop até o jogador acertar
    while not acertou:
        try:
            palpite = int(input("Digite seu palpite: "))
            tentativas += 1

            if palpite < numero_secreto:
                print("🔻 Muito baixo. Tente novamente.\n")
            elif palpite > numero_secreto:
                print("🔺 Muito alto. Tente novamente.\n")
            else:
                print(f"✅ Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
                acertou = True
        except ValueError:
            print("⚠️ Entrada inválida. Por favor, digite um número inteiro.\n")

# Executa o jogo
jogo_adivinhacao()