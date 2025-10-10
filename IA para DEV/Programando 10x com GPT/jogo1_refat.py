import random

# 🔧 Modularização do Código (Prompt 4)
def generate_secret_number(difficulty):
    # 🔧 Adicionar Opções de Dificuldade (Prompt 2)
    # Define o intervalo de acordo com a dificuldade escolhida
    if difficulty == "fácil":
        return random.randint(0, 50)
    elif difficulty == "médio":
        return random.randint(0, 100)
    elif difficulty == "difícil":
        return random.randint(0, 500)
    else:
        print("⚠️ Dificuldade inválida. Usando nível médio por padrão.")
        return random.randint(0, 100)

def get_user_guess():
    # Solicita o palpite do jogador
    try:
        return int(input("Digite seu palpite: "))
    except ValueError:
        print("⚠️ Entrada inválida. Por favor, digite um número inteiro.\n")
        return None

def play_game():
    # 🔧 Tradução para Inglês (Prompt 3): nomes de funções e variáveis em inglês
    print("🎯 Bem-vindo ao Jogo de Adivinhação!")
    print("Escolha o nível de dificuldade: fácil / médio / difícil")
    difficulty = input("Digite a dificuldade: ").lower()
    secret_number = generate_secret_number(difficulty)
    attempts = 0
    is_correct = False

    print(f"\nTente adivinhar o número secreto!\n")

    while not is_correct:
        guess = get_user_guess()
        if guess is None:
            continue

        attempts += 1

        if guess < secret_number:
            print("🔻 Muito baixo. Tente novamente.\n")
        elif guess > secret_number:
            print("🔺 Muito alto. Tente novamente.\n")
        else:
            print(f"✅ Parabéns! Você acertou o número {secret_number} em {attempts} tentativas.")
            is_correct = True

# 🔧 Permitir Reinício do Jogo (Prompt 1)
def main():
    while True:
        play_game()
        print("\nDeseja jogar novamente? (s/n)")
        restart = input("Digite sua escolha: ").lower()
        if restart != "s":
            print("👋 Obrigado por jogar! Até a próxima.")
            break

# 🔧 Adesão aos Style Guides (Prompt 5): uso de boas práticas como if __name__ == "__main__"
if __name__ == "__main__":
    main()

'''
### ✅ Refatorações Aplicadas:

| Prompt | Modificação | Local |
|-------|-------------|-------|
| 1. Reinício do jogo | Loop principal com opção de jogar novamente | `main()` |
| 2. Opções de dificuldade | Faixas de número ajustadas por nível | `generate_secret_number()` |
| 3. Tradução para inglês | Funções e variáveis em inglês, mantendo textos em português | todo o código |
| 4. Modularização | Separação em funções específicas | `generate_secret_number()`, `get_user_guess()`, `play_game()` |
| 5. Style Guide (PEP 8) | Estrutura clara, nomes consistentes, `if __name__ == "__main__"` | todo o código |

Se quiser, posso te ajudar a criar testes automatizados para esse jogo ou transformar isso em um projeto com interface gráfica. Quer seguir por esse caminho?

'''