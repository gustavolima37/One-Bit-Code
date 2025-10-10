'''
Nessa aula vamos aprender a ler dados da tabela do PostgreSQL utilizando a linguagem Python.
Precisamos instalar a biblioteca psycopg2 com o comando pip install psycopg2.
'''
import psycopg2

conn = psycopg2.connect(
    database = 'fliperama',
    user = 'postgres',
    password = '123456', #use a senha que vc colocou na instalação.
    host = 'localhost',
    port = '5432'
)

'''
Essa informações estao no pgadmin 4, em PostgreSQL abaixo de Servers, clica e rola a tela para baixo.
'''
print("psycopg2 está funcionando!")
