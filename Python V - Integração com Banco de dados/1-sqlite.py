'''
Nessa aula vamos utilizar o módulo SQLite em Python para criar o nosso banco de dados.
O banco de dados fica dentro de um arquivo, quando utilizaamos o SQLite.
'''
import sqlite3

# 1 - Criando o BD
connection = sqlite3.connect('title.db')

# 2 - Verifica se houve alterações na base de dados
print(connection.total_changes)