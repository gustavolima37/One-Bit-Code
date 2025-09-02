# 1 - Liste valores de 0 a 10 que sejam menor do que 4.
# for i in range(10):
#     if i < 4:
#         print(i)
listNumber = [i for i in range(10) if i < 4]
print(listNumber)

gamesList = ["Mario Odyssey", "Dk Country",
             "Luigis Mansion", "Kirby"]

# 2 - Jogos que possuam a letra "a"
newList = [x for x in gamesList if "a" in x]
print(newList)

for newList2 in gamesList:
    if "a" in newList2:
        print(newList2)

# 3 - Jogos que eu zerei
gamesFinished = [x for x in gamesList if x != "Kirby"]
print(gamesFinished)