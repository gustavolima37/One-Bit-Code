'''
Nessa aula vamos aprender a escrever dados em um arquivo txt.
Para escrever em arquivos utilizamos a função opne() e podemos utilizar algumas opções como
parâmetro, como as opções 'w' e 'a'.
'''

name = input('Digite seu nome:\n ')
'''
- Arquivos:
1 - opção w - write (escrever)
2 - opção a - append (adicionar)
3 - opção r - read (ler)
'''
# Alternativa 1
# file = open('names.txt', 'a')
# file.write(f'{name}\n')
# file.close()

# Alternativa 2

with open('names.txt', 'a') as file: #Abrindo o arquivo names.txt, opção de adicionar e criando um apelido 'file'
    file.write(f'{name}\n') #simplificando a alternativa 1 em 2 linhas.