'''
Nessa aula vamos criar a nossa primeira classe em Python.
Vamos nos basear em um exemplo real para modelar
uma classe de Filmes. O nosso exemplo será: The Movie Database (TMDB)
Acessando o site do TMDB, escolheremos um filme para servir de 
base para nossa análise.
Diante da imagem do filme, podemos notar algumas
caracteristicas do filme, como nome, gênero, sinopse, etc...
essas informações referem-se aos atributos de uma classe.
'''


class Movie:
    name = '' #nome
    yearLaunch = 0 #Ano de lançamento
    includedPlan = False #incluido no Plano
    note = 0 #nota
    durationMinutes = 0 #duração minutos  