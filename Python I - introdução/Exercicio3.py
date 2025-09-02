"""
Exercício 3:
* Cálculo da Distância:
-> Escreva um programa que pergunte a distância
que um passageiro deseja percorrer em km.
Calcule o preço da passagem, cobrando R$ 0,50 por km
para viagens de até 200km, e R$ 0,35 para viagens mais longas.

* Aumento salário funcionário:
-> Escreva um programa que pergunte o salário do funcionario
e calcule o valor do aumento.
Para salários superiores a R$ 1.250,00, calcle um aumento de 10%.
Para os inferiores ou iguais, de 15%.
"""

# Primeiro desafio

distancia = float(input("Qual a distancia que deseja percorrer em km? \n"))

if distancia <= 200:
    valor = distancia * 0.50
else:
    valor = distancia * 0.35
print(f"A passagem fica no valor de {valor:.2f}")

#-----------------------------------------------------

# Segundo desafio

salario = float(input("Digite o valor do seu salario: \n"))
perc_increase = 0.15

if salario > 1250.00:
    perc_increase = 0.10
increase = salario * perc_increase

print(f"Seu novo salario é: R$ {increase:.2f}")