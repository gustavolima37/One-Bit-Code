import pprint #Melhora a Legibilidade

gameDict = {
    "resident evil 4": {
        "yearLaunch": 2023,
        "classification": 9.8,
        "genre": ["ação", "aventura"]
    },
    "mario odyssey": {
        "yearLaunch": 2017,
        "classification": 10.0,
        "genre": ["aventura", "3d"]
    },
    "donkey kong country": {
        "yearLaunch": 1995,
        "classification": 9.5,
        "genre": ["aventura", "plataforma"]
    }
}

# Melhora a Legibilidade
pp = pprint.PrettyPrinter(depth=4)
pp.pprint(gameDict)

# 1 - Buscar informação dentro de um dicionário aninhado
print(gameDict['mario odyssey']['genre'])

# 2 - Adicionar novo item
gameDict['mario odyssey']['players'] = 1
print(gameDict['mario odyssey'])

# 3 - Excluir dicoonário
del gameDict['resident evil 4']
pp.pprint(gameDict)