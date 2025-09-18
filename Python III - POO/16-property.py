'''
Esse decorator é usado para dar funcionalidade 'especial' a certos métodos para
fazê-los agir como getters, setters ou deleters.
'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @property # funciona como getter
    def name(self):
        return self._name
    
    @name.setter # aqui esta o setter pra buscar o nome protegido
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Nome deve ser uma string')
        self._name = value
        
pessoa = Person('Fulano', 12)
print(vars(pessoa))
