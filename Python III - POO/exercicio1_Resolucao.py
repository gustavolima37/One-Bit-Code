class Movie:
    def __init__(self, name, yearLaunch, includedPlan, durationMinutes): #metodo construtor ou damber
        self.name = name
        self.yearLaunch = yearLaunch
        self.includedPlan = includedPlan
        self.totalEvaluation = 0 #total e avaliações
        self.durationMinutes = durationMinutes
        self.evaluators = 0 #avaliador
        
    def __str__(self): #metodo __str__ sobrescrever uma informação. uma apresentação do objeto.
        return f'Filme: {self.name}'
    
    def techinal_sheet(self): #metodo para chamar o objeto sem duplicar codigo.
        print('## Dados do Filme ##')
        print(f'Nome do filme: {self.name}')
        print(f'Ano de Lançamento: {self.yearLaunch}')
        print(f'Esta no plano? {self.includedPlan}')
        print(f'Avaliação do filme: {self.totalEvaluation}')
        print(f'Duração do filme: {self.durationMinutes}')
        print(f'Total Avaliadores: {self.evaluators}\n')
        
    def evaluate(self, note):
        self.totalEvaluation += note
        self.evaluators += 1
        
    def average(self):
        print(f'Média do Filme: {self.name}: {self.totalEvaluation / self.evaluators}')
        
mario = Movie('Super Mario Bros', 2023, False, 135)
avatar = Movie('Avatar', 2023, False, 180)
mario.evaluate(9.5)
mario.evaluate(10.0)
mario.techinal_sheet()
mario.average()
avatar.evaluate(8.5)
avatar.evaluate(9)
avatar.techinal_sheet()
avatar.average()