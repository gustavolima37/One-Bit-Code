gamesList = ["Fifa", "God of War", "Red Dead 2", "Uncharted", 90.50]
# 1 - Iterando valores de uma lista
for game in gamesList:
    print(game)
print("-" * 20)
    

# 2 - Quando a condição for atendida, o loop será encerrado
for game in gamesList:
    if game == "Red Dead 2":
        break
    print(game)
print("-" * 20)

# 3 - Quando a condição for atendida, o loop vai para a proxima interação
for game in gamesList:
    if game == "Red Dead 2":
        continue
    print(game)
print("-" * 20)

# 4 - Avaliação do jogo
gameName = input("Digite o nome do jogo\n")
gameRating = int(input("Digite quantas avaliações deseja fazer no jogo\n"))

sum = 0
for i in range(gameRating):
    note = float(input("Digite a nota para este jogo\n"))
    sum += note # sum = sum + note
print(f"Média de avaliação do jogo {gameName} é {sum/gameRating :.2f}")
print("-" * 20)