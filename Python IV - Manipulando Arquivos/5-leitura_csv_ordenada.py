'''
Ordenar os dados no arquivo csv assim como foi no txt.
Criando uma lista.
'''
courses = []
with open('dados/courses.csv', 'r', encoding='utf-8') as file:
    for line in file:
        language, category = line.strip().split(',')
        courses.append(f'{language} -{category}')
        
for course in sorted(courses): # ou sorted(courses, reverse=True) pra inverter a ordem. 
    print(course)