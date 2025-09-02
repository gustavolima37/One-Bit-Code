def traduzir_para_dragao(mensagem):
    """
    Função para traduzir uma mensagem para a linguagem dos dragões,
    considerando letras maiúsculas e minúsculas.
    Outros caracteres permanecem inalterados.
    """
    traducao = ''
    for char in mensagem:
        if 'a' <= char <= 'z':  # Letras minúsculas
            traducao += chr(219 - ord(char))
        elif 'A' <= char <= 'Z':  # Letras maiúsculas
            traducao += chr(155 - ord(char))
        else:
            traducao += char  # Outros caracteres permanecem inalterados
    return traducao

def main():
    print("Bem-vindo ao Desafio: Linguagem dos Dragões 🐉")
    print("Digite uma mensagem em linguagem humana para traduzir.")
    print("Digite 'sair' para encerrar o programa.\n")
    
    while True:
        mensagem = input("Você: ")
        if mensagem.lower() == 'sair':
            print("Encerrando o desafio dos dragões... Até mais! 🐲")
            break
        else:
            traducao = traduzir_para_dragao(mensagem)
            print(f"Dragão = {traducao}\n")  # Exibe o resultado no formato desejado

# Executa o programa
if __name__ == "__main__":
    main()