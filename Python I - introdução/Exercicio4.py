"""
Exercício 4:
* Contagem Regressiva:
-> Faça um programa para escrever a contagem regressiva
do lançamento de um foguete.
O programa deve imprimir 10, 9, 8...1, 0 e disparar um "beep".
"""
# for i in range(10, -1, -1):
#     print(i)
# print("beep")

# x = 10
# while x >= 0:
#     print(x)
#     x-=1 # x = x - 1
# print("Beep")

"""
* Tabuada:
-> Faça um programa que Calcule a tabuada de um número, com valores
iniciais e finais informados pelo usuário.
"""
# numero = int(input("Digite o numero da tabuada:\n"))
# inicio = int(input("Digite o valor inicial:\n"))
# fim = int(input("Digite o valor final:\n"))
# print(f"Tabuada do {numero} de {inicio} ate {fim}\n")
# for i in range(inicio, fim +1):
#     print(f"{numero} x {i} = {numero * i}")

# segunda forma
number = int(input("Tabuada de: \n"))
begin = int(input("De: \n"))
end = int(input("Até: \n"))

x = begin

while x <= end:
    print(f"Tabuada de {number} x {x} = {number * x}")
    x += 1