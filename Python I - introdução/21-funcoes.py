# 1 - Função para imprimir Hello World
def wellcome():
    print("Hello World")
wellcome()

# 2 - Função para somar dois numeros
def sum():
    #print(5 + 4) exemplo para imprimir na tela
    return 5 + 4 # exemplo sem imprimir, terar que por o print
sum() # exemplo 1
print(sum()) #exemplo 2

# 3 - Função para cadastrar um jogo
def create_game():
    name = input('Digite o nome do jogo\n')
    yearLaunch = int(input('Digite o ano de lançamento do jogo\n'))
    gamePrice = float(input('Digite o preço do jogo\n')) 
    noteRating = float(input('Digite a nota de avaliação do jogo\n'))
    print(f"{name} - R$ {gamePrice}")

create_game()
create_game()