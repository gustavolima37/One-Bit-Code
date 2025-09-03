'''
Nessa aula vamos aprender a utilizar o módulo random na linguagem Python.
Neste módulo vamos aprender a gerar números aleatórios, 
imprimir um valor aleatório para uma lista ou string, etc.
'''

import random

# 1 - Seleciona valor aleatorio de uma lista
list1 = [7,6,4,3,2,1]
print(random.choice(list1))

# 2 - Gera um número aleatório em um intervalo de valores
r1 = random.randint(5,15)
print(r1)

# 3 - Seleciona um caracter aleatório de uma string
name = 'Curso de Python'
r2 = random.choice(name)
print(r2)

# 4 - Seleciona mais de um valor aleatorio
# Sintaxe: random.sample(sequencia, tamanho)
print(random.sample(list1, 2))
print(random.sample(list1, 3))
s = 'Olá mundo'
print(random.sample(s, 2))