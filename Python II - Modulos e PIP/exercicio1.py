import modulo_string
'''
Módulo de strings

Escreva um módulo em python para tratar algumas 
strings e que possua as seguintes funcionalidades:
- Inverter uma string de trás pra frente.
- Retornar apenas letras com índice par.
- Retornar apenas letras com índice ímpar.
'''

name = input('Digite uma palavra: ').upper()
print(f'Palavra escrita: {name}\nPalavra Invertida: {modulo_string.invert(name)}')
print('')
print(f'Retornando apenas letras indice par: {modulo_string.caracter_par(name)}')
print(f'Retornando apenas letras indice impar: {modulo_string.caracter_impar(name)}')