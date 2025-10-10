'''
Nessa aula vamos aprender a atualizar dados de uma tabela em nosso bando de dados.
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

# 3 - Solicitando Dados do Usuário
id = int(input('Informe o id do filme que deseja atualizar:\n'))
name = input('Informe o novo nome do filme:\n')
year = int(input("Informe o ano do novo filme:\n"))

# 4 - Atualizando Dados
cursor.execute("""
        UPDATE movies SET name = ?, year = ?
        WHERE id = ?       
               """, (name, year, id))
# para atualizar mais que 2 opções, adicione ',' na coluna que deseja atualizar.

connection.commit()
print('Dados atualizados com sucesso!')

# 5 - Fechando conexão
connection.close()