from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import dotenv_values

config = dotenv_values('.env')

user = config['DB_USER']
password = config['DB_PASSWORD']
host = config['DB_HOST']
database = 'blog'

DATABASE_URI = f'postgresql://{user}:{password}@{host}/{database}'

engine = create_engine(DATABASE_URI)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

'''
Codigo base para usar em qualquer SGBD(mysql, postgresql etc..)
mudando alguns detalhes como o user, password, host e database
assim como no DATABASE_URI, nesse caso, estamos usando postgresql, mas podemos usar o mysql, so precisaria
alterar o nome.
'''