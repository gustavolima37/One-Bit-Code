gamesSet = {"Fifa23", "Red Dead 2", "Star Wars",
              "Mario Odyssey", "The Legend of Zelda"}

print(gamesSet)
print(type(gamesSet))

# 1 - Buscar o tamanho do set
print(len(gamesSet))

# 2 - True e 1 são considerados o mesmo valor
exempleSet = {"Fifa 23", True, 1, 90.50}
print(exempleSet)

# 3 - Adicionar item de outro set
gamesSet.update(exempleSet)
print(gamesSet)
# Não repete o item caso ja tenha o mesmo no set ou tupla. Na lista sim.

# 4 - Remover um item do set
gamesSet.remove(True)
gamesSet.remove(90.50)
print(gamesSet)
# - Não possibilita recuperar valores via fatiamento ou slice
# ex: print(gamesSet[:2])