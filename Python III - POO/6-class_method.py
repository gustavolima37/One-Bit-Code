'''
Nessa aula vamos aprender a utilizar métodos de classe em Python.
O método de classe pode acessar ou modificar o estado da classe. 
Para utilizá-lo, precisamos explicitar o decorator classmethod.
1- O método de classe utiliza o parâmetro referente a classe.
2- O método de classe pode acessar ou modificar o estado da classe.
3- Usamos o decorator @classmethod para criar um método de classe.
'''

class Console:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    @classmethod
    def from_text(cls, string):
        import re #importando expressões regulares
        item = re.findall(r'é \w*', string) #buscando na string a expressão apartir do: é + espaço ( \w*)
        name = item[0][2:] #item da posição 0, depois da 2: em diante
        price = item[1][2:] #item da posição 1, depois da 2: em diante
        return cls(name, int(price))
    
wiiU = Console.from_text('Meu video game é WiiW e o preço é 1000 reais.')
xboxone = Console.from_text('Meu video game é XboxOne e o preço é 1500 reais.')
print(wiiU.__dict__) #metodo para mostrar em dicionario
print(xboxone.__dict__)