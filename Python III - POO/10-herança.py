'''
- Nessa aula vamos aprender a implementar a herança de classes em Python.
Possibilita que uma classe(filha) possa herdar atributos e métodos de outra classe(pai).
O relacionamento de herança é definido por 'É um'. Exemplo: 'Cachorro é um Animal. 'Carro é um Veículo'.etc...
temos uma imagem:

'''

class Animal: #class pai
    name = ''
    size = ''
    color = ''
    
    def eat(self):
        print('Animal se alimentando')
        
class Horse(Animal): #class filho
    race = ''
    
    def escape(self):
        print('Cavalo fugindo')
        
class Lion(Animal): #class filho
    juba = ''
    
    def hunt(self):
        print('Leão caçando')
        
h = Horse()
h.name = 'Carpeado'
h.color = 'Branco'
h.escape()
h.eat()

l = Lion()
l.name = 'Simba'
l.color = 'Marron'
l.hunt()
l.eat()