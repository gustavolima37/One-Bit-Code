gameDescription = """"
Fifa 23 é um jogo de futebol
desenvolvido pela EA Sports
e que possibilita jogar localmente ou online
"""
gameName = "Fifa"
gameVersion = " 23"
line = "="

# 1 - Operação de Concatenação de Strings
print(line * 25)
gameFullName = gameName + gameVersion
print(gameFullName)

# 2 - Operação de multiplicação de Strings
print(line * 25)

# 3 - Proura palavra dentro de um texto
print("Fifa" in gameDescription)
print("futebol" in gameDescription)