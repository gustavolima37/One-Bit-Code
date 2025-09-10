'''
1- Nessa aula vamos aprender um dos importantes pilares da orientação a objetos, o encapsulamento.
2- Até aqui você pode notar a facilidade com que temos manipulado os atributos de uma classe, não é verdade? Bem, se estivéssemos mapeando um sistema de natureza mais crítica seria inviável fornecer tamanha flexibilidade para manipulação diretamente dos atributos.
3- Imagine por exemplo uma classe Conta Corrente, onde pudéssemos atribuir o valor de conta corrente diretamente para cada correntista, quão confiável esse sistema seria? Pensando nisso, temos então o pilar do encapsulamento para nos ajudar com essa questão.
4- A analogia mais simples de entender o encapsulamento, é um remédio de cápsula. O essencial do remédio é o que está protegido dentro da cápsula, para que aquele conteúdo não seja alterado.
5- E trazendo para a orientação a objetos, o nosso objetivo é proteger o acesso aos atributos, possibilitando o acesso a leitura ou escrita destes atributos, somente via métodos.

'''
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary # .__ significa atributo privado
        
    def show(self):
        print(f'Nome: {self.name} - Salário {self.__salary}')
        
fulano = Employee('Fulano', 4000)
sicrano = Employee('Sicrano', 5000)
fulano.show()
sicrano.show()
fulano.__salary = 40000 #pode vê mas nao pode modificar.
fulano.show()