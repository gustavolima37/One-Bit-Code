class Movie:
    def __init__(self, name, yearLaunch, includedPlan, note, durationMinutes): #metodo construtor ou damber
        self.name = name
        self.yearLaunch = yearLaunch
        self.includedPlan = includedPlan
        self.note = note
        self;durationMinutes = durationMinutes
        
    def __str__(self): #metodo __str__ sobrescrever uma informação. uma apresentação do objeto.
        return f'Filme: {self.name}'

        
movie = Movie('Super Mario bross', 2023, False, 5.0, 130)
movie2 = Movie('Avatar', 2023, False, 4.5, 220)
print(movie.name)
print(movie2.name)
print(movie)
print(movie2)
