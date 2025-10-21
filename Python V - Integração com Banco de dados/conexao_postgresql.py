'''
Nessa aula vamos aprender a ler dados da tabela do PostgreSQL utilizando a linguagem Python.
Precisamos instalar a biblioteca psycopg2 com o comando pip install psycopg2.
'''
import psycopg2
from dotenv import dotenv_values

config = dotenv_values('.env')

# Conecta ao banco usando variáveis de ambiente
conn = psycopg2.connect( 
                        database=config["DB_NAME"], 
                        user=config["DB_USER"], 
                        password=config["DB_PASSWORD"], 
                        host=config["DB_HOST"], 
                        port=config["DB_PORT"] 
)

'''
Essa informações estao no pgadmin 4, em PostgreSQL abaixo de Servers, clica e rola a tela para baixo.
'''

