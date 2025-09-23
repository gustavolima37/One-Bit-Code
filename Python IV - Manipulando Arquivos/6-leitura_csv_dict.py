'''
Vamos adicionar o arquivo csv numa lista para criar seu dicionario.
'''
#criando a lista
courses = []

#Abrindo e lendo os arquivos csv
with open('dados/courses.csv', 'r', encoding='utf-8') as file:
    for line in file:
        language, category = line.strip().split(',')
        #criando o dicionario 
        course = {}
        #Adicionando chave e valor
        course['language'] = language
        course['category'] = category
        #adicionando a lista
        courses.append(course)
        
print(courses)

#Manipulando
for course in courses:
    print(f"{course['language']} -{course['category']}")