'''
Nessa aula vamos aprender a lê valores lidos de um arquivo csv
utilizando o módulo built in csv.
Com o modulo, conseguimos ler o arquivo sem mostrar o titulo contigo no arquivo csv.
'''

import csv

courses = []

with open('dados/courses.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file) #utilizando a biblioteca csv
    for row in reader:
        courses.append({'language':row['language'], 'category':row['category']})
        
#extraindo os dados
for course in sorted(courses, key=lambda course: course['language'], reverse=True):
    print(f'{course['language']}-{course['category']}')