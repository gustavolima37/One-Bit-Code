'''
Nesta aula vamos aprender a ler dados de um arquivo txt.
Utilizamos a propriedade 'r' no método open(), que significa 'read'.
Na função open('arquivo a ser lido', 'modo a ser utilizado, 'encoding='utf-8' é a forma de escrita para adicionar caracteres especiais.)
'''

with open('dados/names.txt', 'r', encoding='utf-8') as file:
    for line in file:
        print(f'Olá, {line.rstrip()}') #rstrip() remove o espaço de 1 linha.