gameName = input("Digite o nome do jogo:\n")
qtdRating = 0
totalRating = 0
rating = 0
avarage = 0

while(rating != -1):
    rating = float(input("Informe a nota do jogo:\n"))
    if(rating != -1):
        totalRating += rating # totalRating = totalRating + rating
        qtdRating += 1 # qtdRating = qtdRating + 1
        avarage = totalRating / qtdRating
print(f"Média das avaliações do jogo {gameName} é {avarage:.2f}")