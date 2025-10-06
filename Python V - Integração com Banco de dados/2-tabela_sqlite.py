'''
Nessa aula vamos utilizar, ligar e criar a tabela para nosso banco de dados.
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

# 3 - Criando a Tabela
cursor.execute('''
        CREATE TABLE movies(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            year INTEGER NOT NULL,
            score REAL NOT NULL
            );
               ''')

# 4 - Fechando a Conexão
print('Tabela criada com sucesso')
connection.close()