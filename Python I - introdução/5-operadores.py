num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))

# Aritmpeticos
sum = num1 + num2
sub = num1 - num2
div = num1 / num2
mult = num1 * num2
mod = num1 % num2
exp = num1 ** num2
print(f"Resto da divisao de {num1} por {num2} é {mod}")
print(f"Potência do numero {num1} por {num2} é {exp}")

# Comparação
bigger = num1 > num2
smaller = num1 < num2
equal = num1 == num2
different = num1 != num2
bigger_equal = num1 >= num2
smaller_equal = num1 <= num2

print(f"Os numeros {num1} e {num2} são iguais? {equal}")
print(f"O numero {num1} é maior ou igual a {num2}? {bigger_equal}")

# Atribuição
num1 += 1 # num1 = num1 + 1
num1 -= 1 # num1 = num1 - 1
num1 *= 1 # num1 = num1 * 1
num1 /= 1 # num1 = num1 / 1