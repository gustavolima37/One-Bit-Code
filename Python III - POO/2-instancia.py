class Movie:
    name = '' #nome
    yearLaunch = 0 #Ano de lançamento
    includedPlan = False #incluido no Plano
    note = 0 #nota
    durationMinutes = 0 #duração minutos  
    
# Primeiro Filme #
movie = Movie()
movie.name = 'Super Mario Bros'
movie.yearLaunch = 2023
movie.includedPlan = False
movie.note = 5.0
movie.durationMinutes = 130

# Criando o 2 Filme e reutilizando a class Movie #
movie2 = Movie()
movie2.name = 'Arena Of Valor'
movie2.yearLaunch = 2015
movie2.includedPlan = True
movie2.note = 9.8
movie2.durationMinutes = 160

print('## Dados do Filme 1 ##')
print(f'Nome do Filme: {movie.name} \nAno de Lançamento: {movie.yearLaunch}')

print('## Dados do Filme 2 ##')
print(f'Nome do Filme: {movie2.name} \nNota do Filme: {movie2.note}')