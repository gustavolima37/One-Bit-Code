'''
Nessa aula vamos aprender a utilizar o módulo re (regular expression(expressão regular)) na 
linguagem Python.
Este módulo é muito importante, 
pois podemos buscar dados utilizando algumas 
expressões regulares na linguagem Python.
Vamos aprender a buscar índice inicial e final e 
a utilizar os operadores de início, fim de uma s
tring e lista de valores ou letras.
'''

import re

text = 'OneBitCode: Transformamos pessoas em programadores sem limites'
# 1 - Indice inicial e final de palavras
# O r significa que estamos trabalhando com uma string bruta (raw string)
match = re.search(r'pessoas em programadores', text) #procure pra mim, onde se encontra a expressão: 'pessoas em programadores', no texto 'text'
print('Indice inicial ', match.start())
print('Indice final ', match.end())

# 2 - Buscando o índice que possui o ponto
site = 'https://onebitcode.com'
#match = re.search(r'.', site)
match = re.search(r'\.', site) #pra achar o ponto, precisa colocar '\.', outro caracter nao precisa.
print(match)

# 3 - Buscando uma lista de caracteres dentro de uma frase
pattern = '[a-m]' #padrão de 'a' ate 'm'
result = re.findall(pattern, text) #busque o padrao dentro do texto
print(text)
print(result)

# 4 - Verificando o inicio de uma string
rule = r'^A' #regra começa '^' com a letra 'A'
phrases = ['A casa está suja', 'O dia está lindo', 'Vamos passear']
for f in phrases:
    if re.match(rule, f):
        print(f'Corresponde: {f}')
    else:
        print(f'Não corresponde: {f}')
        
# 5 - Verificando o final de uma string
rule_end = r'!$' #O sinal '$' significa buscar na string no final
phrases2 = 'O dia está lindo!'
match = re.search(rule_end, phrases2)
if match:
    print('Sim, corresponde')
else:
    print('Não corresponde')
