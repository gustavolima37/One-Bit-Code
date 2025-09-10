'''
1 - Desenvolva uma classe em Python para atender as 
seguintes especificidades de um Produto:
Cada produto deve ter um preço e um nome.
2 - A classe deve ter um método construtor e o 
método dundle str.
3 - A classe deve ter um método para desconto. 
O método deve receber o desconto em percentual 
e realizar o cálculo de quanto ficaria o preço 
final com o desconto.
'''

class Produto:
    def __init__(self, nome, preço, desconto):
        self.nome = nome
        self.preço = preço
        self.desconto = desconto
        
        
    def __str__(self):
        print(f'Produto: {self.nome}\nValor: R$ {self.preço}')
        print(f'Com desconto de: {self.desconto} %')
        print(f'Novo valor: R$ {self.preço - (self.preço * (self.desconto/100))}')
        
doce = Produto('Doce', 100.00, 15)
doce.__str__()