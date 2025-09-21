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
Pra manipular dicionario com a função sorted, precisamos
criar funções expecificas, pois o sorted ele pega a chave e retorna none, porem 
temos valores nas chaves, logo retorna erro.
'''
#criando função para 'language'
def get_language(course):
    return course['language']

#criando função para 'category'
def get_category(course):
    return course['category']


#Manipulando crescente
for course in sorted(courses, key=get_language):
    print(f"{course['language']} -{course['category']}")

print('------------------------------------')
#Manipulando decrescente
for course in sorted(courses, key=get_language, reverse=True):
    print(f"{course['language']} -{course['category']}")
    
print('------------------------------------')

#Manipulando pela categoria
for course in sorted(courses, key=get_category):
    print(f"{course['language']} -{course['category']}")