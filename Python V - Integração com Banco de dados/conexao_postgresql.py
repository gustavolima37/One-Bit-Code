'''
Nessa aula vamos aprender a ler dados da tabela do PostgreSQL utilizando a linguagem Python.
Precisamos instalar a biblioteca psycopg2 com o comando pip install psycopg2.
'''
import psycopg2
import os
from dotenv import load_dotenv

# Carrega variáveis do .env
load_dotenv()

# Conecta ao banco usando variáveis de ambiente
conn = psycopg2.connect(
    database = os.getenv("DB_NAME"),
    user = os.getenv("DB_USER"),
    password = os.getenv("DB_PASSWORD"), # senha guardada
    host = os.getenv("DB_HOST"),
    port = os.getenv("DB_PORT")
)

'''
Essa informações estao no pgadmin 4, em PostgreSQL abaixo de Servers, clica e rola a tela para baixo.
'''
print("psycopg2 está funcionando!")
