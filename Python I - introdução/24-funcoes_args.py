"""
*args - Utilizamos ele quando não temos certeza de quantos
argumentos queremos ter numa função.
- Os argumentos sao passados como uma tupla.

**kwargs - Além dos valores podemos passar tambem as respectivas chaves 
para cada argumento.
- Os argumentos sao passados como um dicionario.
"""

# 1 - Soma de números
def sum(*num):
    sum_total = 0
    for n in num:
        sum_total += n 
    print(f"Soma é: {sum_total}")
    
sum(7)
sum(7,9)
sum(7,10,9,8,7,6)


# 2 - Apresentação de cursos
def presentation(**data):
    for key, value in data.items():
        print(f"{key} - {value}")
      
print("#####Cursos#####")  
presentation(name="Python", category="Backend", level="iniciante")
presentation(name="Visão Computacional com Python", category="IA", level="Avançado")
presentation(name="Dashboards com Dash", category="Data Science", level="intermediario")