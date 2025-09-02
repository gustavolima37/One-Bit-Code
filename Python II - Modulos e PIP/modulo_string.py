#Utilizando ajuda da aula Slice.py de Python I

def invert(string):
    return string[::-1]#passo negativo, regressa: 3 2 1 0

def caracter_par(string):
    return string[::2] #passo de 2 em 2: 0 2 4 6

def caracter_impar(string):
    return string[1::2]#inicia no 1 e passo 2 em 2: 1 3 5 7