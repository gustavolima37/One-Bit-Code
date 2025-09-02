gameName = "Fifa 23"
gameDescription = """"
Fifa 23 é um jogo de futebol,
desenvolvido pela EA Sports,
e que possibilita jogar localmente ou online
"""
print(gameName.upper()) # Retorna string em maiúsculo
print(gameName.lower()) # Retorna string em minúsculo
print(gameName.capitalize()) # Apenas a primeira letra em miúsculo
print(gameName.title()) # Apenas a primeira letra em miúsculo
print(gameName.center(11, "-")) # Retorna a string centralizada com caractere de preenchimento
print(gameName.find("i")) # Retorna a posição de um determinado caractere
print(gameDescription.count("f")) # conta caractere
print(gameDescription.count("a")) # conta caractere
print(gameDescription.replace("Fifa", "Pes")) # Altera um elemento por outro
print(gameDescription.split(',')) # Quebra a string apartir de um caractere especifico.