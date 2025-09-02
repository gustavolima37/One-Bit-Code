def pode_formar_palindromo(assentos):
    # Passo 1: Contar a frequência de cada número
    contagem = {}
    for numero in assentos:
        if numero in contagem:
            contagem[numero] += 1
        else:
            contagem[numero] = 1

    # Passo 2: Verificar quantos números têm frequência ímpar
    impares = 0
    for quantidade in contagem.values():
        if quantidade % 2 != 0:
            impares += 1
    
    # Passo 3: Se mais de um número tem frequência ímpar, não forma um palíndromo
    return impares <= 1

# Teste com os exemplos fornecidos
print(pode_formar_palindromo([4, 5, 6, 4, 5]))  # Deve retornar True
print(pode_formar_palindromo([4, 5, 6]))        # Deve retornar False