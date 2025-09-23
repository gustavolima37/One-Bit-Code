'''
Nesta aula vamos aprender a escrever dados csv em Python.
Utilizando o módulo csv, essa tarefa ficará bem mais tranquila.
E o melhor é que assim, podemos tornar o programa mais interativo com o usuário.
'''
import csv

name = input('Informe o nome da linguagem que deseja aprender: \n')
category = input('Qual categoria que a linguagem se encaixa? \n')

with open('dados/courses.csv', 'a', encoding='utf-8') as file:
    writer = csv.writer(file, lineterminator='\n') #escrever no arquivo
    writer.writerow([name, category]) #escrever na linha: nome, categoria