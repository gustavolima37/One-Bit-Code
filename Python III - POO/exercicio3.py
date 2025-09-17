# modelos.py
# (coloque o código das classes Usuario e Viagem aqui)

class Usuario:
    def __init__(self, nome):
        self.nome = nome

class Viagem:
    def __init__(self, destino, duracao, preco):
        self.destino = destino
        self.duracao = duracao
        self.preco = preco
    
    def __str__(self):
        return (f'A viagem para: {self.destino}\n'
                f'Duração de: {self.duracao}\n'
                f'Custa: {self.preco}')


# main.py
# (coloque o código principal aqui)

def mostrar_menu_viagens(viagens):
    print('=== Opções de Viagem Disponíveis ===')
    for i, viagem in enumerate(viagens):
        print(f'{i}. Destino: {viagem.destino}')

# 1. Cria as instâncias e a lista de viagens
viagens_disponiveis = [
    Viagem('Paraíba', '3 dias', 2500),
    Viagem('Campina Grande', '3 dias', 3000),
    Viagem('Fortaleza', '3 dias', 2700),
    Viagem('Pernambuco', '3 dias', 2450)
]

# 2. Pede o nome do usuário
nome_do_usuario = input('Digite seu nome para cadastrar a viagem: ')
pessoa = Usuario(nome_do_usuario)

# 3. Exibe o menu e trata a escolha
mostrar_menu_viagens(viagens_disponiveis)

try:
    escolha_do_usuario = int(input('Digite o número da viagem desejada: '))
    viagem_escolhida = viagens_disponiveis[escolha_do_usuario]
    
    # 4. Exibe a mensagem de sucesso (FINAL)
    print("\n--- Mensagem de Confirmação ---")
    print(f"Parabéns, {pessoa.nome}!")
    print(f"O cadastro da sua viagem para **{viagem_escolhida.destino}** foi feito com sucesso.")
    print("Aguarde mais informações sobre os detalhes da viagem.")
    print("---------------------------------")

except (ValueError, IndexError):
    print('Escolha inválida! Por favor, digite um número da lista.')