'''
Nessa aula vamos aprender a remover dados de uma tabela em nosso BD.
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

# 3 - Solicitando dados do usuario
id = int(input('Informe o id do filme que deseja remover:\n'))

# 4 - Removendo dados
cursor.execute("""
        DELETE FROM movies
        WHERE id = ?        
               """, (id,))
# Se deixar apenas (id) pode ser que tenha erro, o certo, mesmo que seja 1 argumento, deixe uma virgula apos ele (id,)

connection.commit()
print('Filme removido com sucesso!')

# 5 - Fechando conexão
connection.close()