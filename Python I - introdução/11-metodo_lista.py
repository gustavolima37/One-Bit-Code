gameList = ["Resident Evil 4", "Star Wars Jedi Survivor", 
            "The Legend of Zelda", "Red Dead 2", "Mario Odyssey",
            "Luigis Mansion 3"]

# 1 - Tamanho da Lista
print(len(gameList))

# 2 - Recuperar um item da lista pelo indice
print(gameList.index("Mario Odyssey"))

# 3 - Adicionar item ao final da lista
gameList.append("Gta V")
print(gameList)

# 4 - Ordenar a lista 
gameList.sort()
print(gameList)

# 5 - Copiar os itens de uma lista para outra
gameReset = gameList.copy()
gameReset.remove("Star Wars Jedi Survivor")
print(gameReset)

# 6 - Remove todos os itens da lista
gameList.clear()
print(gameList)