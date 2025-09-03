'''
Verificar conteúdo da String
 - Escreva um programa em Python para verificar 
 se uma string contém apenas um determinado conjunto 
 de caracteres (neste caso, a-z, A-Z e 0-9).
'''

import re

def check_caracter(string):
    rule = re.compile(r'[^a-zA-Z0-9]') #r'' = raw string ou string bruta, ^a-zA-Z0-9 é a regra pra buscar na variavel.
    string = rule.search(string)
    return not bool(string) #retorna True para texto, retorna False caso seja caracter especial (@ # $ % &...)

print(check_caracter('ASDFGHasdfghhj1234568'))
print(check_caracter('$#@%^=+*/'))