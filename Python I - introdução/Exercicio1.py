"""
Exercício 1:
* Antecessor e Sucessor de um número:
-> Escreva um programa em Python que leia um numero
e represente o número antecessor e sucessor desse
número que foi lido, utilizando operadores de atribuição.

* Média de 4 notas:
-> Escreva um programa em Python que leia quatro números
e calcule a média entre esses números.
"""
# Desafio 1
number = int(input("Digite um número: "))
print(f"O número antecessor de {number} é {number-1} e o sucessor {number+1}")
print("========================================")

# Desafio 2
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))
num4 = float(input("Digite o quarto número: "))
media = (num1 + num2 + num3 + num4) / 4 

print(f"A média das notas é: {media}")
