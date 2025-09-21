'''
Nessa aula vamos aprender a lê valores de um arquivo csv.
Iremos criar duas colunas, a primeira é para informmar o nome
da linguagem ou tecnologia do curso e a segunda coluna 
para informar a categoria daquele curso ou tecnologia.
'''
with open('dados/courses.csv', 'r', encoding='utf-8') as file:
    for line in file:
        # row = line.strip().split(',')
        # print(f'{row[0]} - {row[1]}')
        language, category = line.strip().split(',') #colocando as colunas nas variaveis e separando os dados pela ','
        print(f'{language} -{category}')