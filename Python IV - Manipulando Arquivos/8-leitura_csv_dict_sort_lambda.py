'''
Vamos ordenar o arquivo csv num dicionario utilizando funções.
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
        
#print(courses)

'''
repetindo a aula 7, porem usando a expressão anonima 'lambda'
'''

#Manipulando crescente
for course in sorted(courses, key=lambda course: course['language']):
    print(f"{course['language']} -{course['category']}")

print('-----------------------------------')
#Manipulando reverso
for course in sorted(courses, key=lambda course: course['language'], reverse=True):
    print(f"{course['language']} -{course['category']}")
