'''
Nessa aula vamos aprender a utilizar o módulo json 
na linguagem Python.
Neste módulo vamos aprender a ler dados em json 
de forma externa, salvar um arquivo json em .txt, 
formatar a visualização de um json, etc.
'''

import json

# 1 - Strings para Dicionarios
person = '{"name": "Rodrigo", "languagens":["Python", "Javascript"]}'
person_dict = json.loads(person)
print(person_dict)
print(person_dict['languagens'])

# 2 - Convertendo dicionario para json
person_json = json.dumps(person_dict)
print(person_json)
print(type(person_json))
print(type(person_dict))

'''
json.dumps(): O s significa string. 
Ele converte um objeto Python (como um dicionário ou lista) 
em uma string no formato JSON.

json.dump(): Ele escreve um objeto Python 
diretamente em um arquivo no formato JSON.
'''

# 3 - Formatando json
print(json.dumps(person_dict, indent=4, sort_keys=True))

# 4 - Salvando json em txt
with open('person.txt', 'w') as json_file: #Crie um arquivo txt, com a referencia 'as' 'json_file'
    json.dump(person_dict, json_file) #conteudo 'person_dict' com a referencia 'json_file'
    
# 5 - Lendo json externo
with open('person.txt', 'r') as f:
    data = json.load(f)
    print(data)
'''
Linha 1: with open('person.txt', 'r') as f:
Essa linha usa um gerenciador de contexto (with) para abrir o arquivo person.txt.

open(): É a função que abre o arquivo. O primeiro argumento ('person.txt') é o nome do arquivo, 
e o segundo ('r') é o modo, que significa read (leitura).

as f: Atribui o arquivo aberto à variável f. 
Você pode usar essa variável para ler ou escrever no arquivo.

with: O gerenciador de contexto with garante que o arquivo seja automaticamente 
fechado assim que o bloco de código terminar, mesmo que ocorra um erro. Isso evita problemas de vazamento de recursos.

Linha 2: data = json.load(f)
Essa é a linha que faz a conversão de formato.

json.load(): É uma função do módulo json que lê um arquivo (ou, mais precisamente, 
um objeto de arquivo como f) e analisa seu conteúdo, esperando que seja um formato JSON válido.

O que ele faz? Ele traduz a string JSON que está no arquivo em um objeto Python. Por exemplo, 
um objeto JSON ({"nome": "João"}) se torna um dicionário Python ({'nome': 'João'}).

O resultado dessa conversão é armazenado na variável data.

Linha 3: print(data)
Esta linha é bem simples.

print(): Imprime o conteúdo da variável data no terminal.

O que será impresso não é o texto puro do arquivo person.txt, mas sim a estrutura de dados Python (dicionário, lista, etc.)
que foi criada a partir da conversão do JSON.
'''