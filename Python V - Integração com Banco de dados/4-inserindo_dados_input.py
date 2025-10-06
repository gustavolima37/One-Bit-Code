'''
Nessa aula vamos utilizar inserir dados na tabela em nosso banco de dados
utilizando o input.
'''
import sqlite3

# 1 - conectando no BD
connection = sqlite3.connect('title.db')

# 2 - Criando um cursor
'''
Cursor é um interador que permite navegar
e manipular os registros em um BD
'''

cursor = connection.cursor()

# 3 - Solicitando dados do usuário
name = input('Nome do filme:\n')
year = int(input('Ano do filme:\n'))
score = float(input('Nota do filme:\n'))

# 4 - Inserindo dados
cursor.execute("""
    INSERT INTO movies (name, year, score)
    VALUES (?, ?, ?)           
               """, (name, year, score))

# 5 - Gravando dados no BD
connection.commit()
print('Dados inseridos com sucesso')

# 6 - Fechando conexão
connection.close()