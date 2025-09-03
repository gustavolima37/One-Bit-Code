'''
Nessa aula vamos aprender a utilizar o módulo 
statistics na linguagem Python.
Esse módulo serve para facilitar introduzir a 
estatística aplicada na linguagem Python.
'''

import statistics

# 1 - Aplicar a média
print(statistics.mean([3, 2, 3, 8, 9]))

# 2 - Aplicar a mediana
print(statistics.median([1, 2, 4, 8, 9]))
print(statistics.median([1, 2, 3, 7, 8, 9]))

# 3 - Aplicar a moda
print(statistics.mode([2, 5, 3, 2, 8, 3, 9, 4, 2, 5, 6])) 
#O numero que mais se repete

# 4 - Desvio padrão
'''
- Quanto mais proximo de 0 for o desvio padrão,
significa que os dados do conjunto estão menos dispersos
'''
print(statistics.stdev([1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5]))
