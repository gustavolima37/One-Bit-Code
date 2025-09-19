'''
Nessa aula vamos aprender a ordenar valores na leitura dos dados de um arquivo txt.
'''

# Criamos uma lista vazia
names = []

# Colocamos os dados linha a linha, mas adicionamos na lista names.
with open('dados/names.txt', 'r', encoding='utf-8') as file:
    for line in file:
        names.append(line.rstrip())

# Ordenando a lista com a função sorted()        
for name in sorted(names):
    print(f'Olá, {name}')