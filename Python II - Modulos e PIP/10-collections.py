'''
Nessa aula vamos aprender a utilizar o módulo collections na linguagem Python.
Neste módulo vamos aprender a contar itens de uma lista, 
ordenar dicionários e outras funcionalidades interessantes.
'''

from collections import Counter, namedtuple, deque
from operator import itemgetter

# 1 - Contar itens de uma lista
fruits = [
    'Maçã', 'Banana', 'Uva', 'Pêra', 'Banana',
    'Uva', 'Maçã', 'Laranja', 'Abacaxi',
    'Tangerina', 'Uva', 'Pêra', 'Banana'
]
print(fruits)
print(Counter(fruits)) #contar quantas vezes aparece a mesma palavra na lista

# 2 - Utilizando tupla nomeada
game = namedtuple('game', ['name', 'prince', 'note'])
g1 = game('Fifa23', 90.50, 8.5)
g2 = game('Residente Evil 4 Remake', 300, 10.0)
print(g1)
print(g2)

# 3 - Ordenando dicionarios
studants = {'Pedro':23, 'Ana':22, 'Ronaldo':26, 'Janaina':25}
a = sorted(studants.items(), key=itemgetter(0))
print(studants)
print(a)

# 4 - Utilizando fila ambas extremidades
deq = deque([20,40,60,80])
deq.appendleft(10) #Adiciona no inicio
print(deq)
deq.append(90) #Adiciona no final
print(deq)
deq.popleft() #Remove no inicio
print(deq)
deq.pop() #Remove no final
print(deq)