'''
Nessa aula vamos aprender a ler dados de uma tabela em nosso banco de dados.
'''
import sqlite3

# 1 - Conectando no BD
connection = sqlite3.connect('title.db')

# 2 - Criando cursor
'''
Cursor é um interador que permite navegar
e manipular os registros em um BD
'''

cursor = connection.cursor()

# 3 - Lendo dados da tabela

'''data = cursor.execute("""
            SELECT name, year, score FROM movies          
                      """)'''
# ou

data = cursor.execute("""
            SELECT * FROM movies          
                      """)

# Com SELECT vc seleciona as colunas que quer, tipo as 3 iformadas, ou pode ser todas
# colocando apenas um * depois de SELECT
# utilizando o *, tbm adiciona um contador no inicio de cada filme no BD

print(data.fetchall())

# 4 - Interando os Dados
for row in cursor.execute("SELECT * FROM movies"):
    print(f'{row}\n')


# 5 - Ordenando os Dados pelo Score (normalmente crescente, mas se adicionar 'desc' no final, fica decrescente)

for row in cursor.execute("SELECT * FROM movies ORDER BY score desc"):
    print(f'{row}')
    
# 6 - Fechando conexão
connection.close()