'''
Lendo n linhas de um arquivo
- Escreva um programa para ler as primeiras n linhas de um arquivo.
1- O nome do arquivo e a quantidade de linhas devem
ser passadas via parâmetro na função.
'''

# eu:

# def ler_n_linhas(arquivo, numero_linhas):
#     with open(arquivo, 'r', encoding='utf-8') as file:
#         for i, linha in enumerate(file):
#             if i >= numero_linhas:
#                 break
#             print(f'N.{i+1} - {linha.strip()}')
            
# ler_n_linhas('dados/names.txt', 4)
#_________________________________________________________

# Prof.

def file_read_from_line(fname, nlines):
    from itertools import islice
    with open(fname, encoding='utf-8') as file:
        for line in islice(file, nlines):
            print(line.strip())
            
file_read_from_line('dados/frases.txt', 2)