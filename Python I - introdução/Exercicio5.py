"""
Conta letras maiúsculas e minúsculas

Escreva uma função Python que receba uma string
e conte o número de letras maiúsculas e minúsculas
desta string.

Lista números pares e ímpares de uma lista

Escreva uma função Python para imprimir os
números pares e ímpares em duas listas separadas
para cada uma.
"""
# 1 - Verificador de letras maiusculas e minusculas

def check_char(text):  
    type = {"Uppercase": 0, "Lowercase": 0}  # Dicionário para contar maiúsculas e minúsculas
    for char in text:  # Percorre cada caractere da string
        if char.isupper():  # Verifica se é uma letra maiúscula
            type["Uppercase"] += 1
        elif char.islower():  # Verifica se é uma letra minúscula
            type["Lowercase"] += 1
    
    # Exibe os resultados
    print("Texto original:", text)  
    print("Número de letras maiúsculas:", type["Uppercase"])  
    print("Número de letras minúsculas:", type["Lowercase"])  

# Teste com uma string específica
check_char("Gustavo Henrique Cabral de Lima")


# 2 - Verifica número par ou impar
def check_numbers(numbers):
    par = []
    impar = []
    for number in numbers:
        if number % 2 == 0:
            par.append(number)
        else:
            impar.append(number)
    return par, impar
print(check_numbers([1, 2, 4, 6, 5, 7, 11, 20, 37]))