'''
 Utilizando o metodo super() para herdar as caracteristicas
 da classe pai (phone), na classe filho (Smartphone)
'''

class Phone:
    def __init__(self, brand,model_name,price):
        self._brand = brand
        self._model_name = model_name
        self._price = price
        
    def __str__(self):
        return f'{self._brand}{self._model_name}'
    
    @staticmethod
    def make_a_call(phone_num):
        print(f'Ligando para {phone_num}')
        
class SmartPhone(Phone):
    def __init__(self, brand, model_name, price,ram, internal_memory,back_camera):
        super().__init__(brand, model_name, price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.back_camera = back_camera
        
Moto = Phone('Moto', 'G7', 1000)
print(Moto)
Moto.make_a_call(1312322)
print(f'Valor do {Moto._brand}{Moto._model_name} é {Moto._price}')
print(vars(Moto))

'''
O vars() é uma função embutida do Python que retorna o dicionário __dict__ de um objeto, 
módulo, classe ou qualquer outro tipo de objeto que tenha esse atributo. Esse dicionário armazena os atributos 
(variáveis de instância) e seus respectivos valores para o objeto em questão.
No código que você forneceu, print(vars(Iphone)) exibirá um dicionário contendo todos os atributos do objeto Iphone e 
seus valores atuais, como 'Iphone', '13', 5000, etc.
'''
Iphone = SmartPhone('Iphone', '13', 5000, '4GB', '128GB', '25MP')
print(Iphone)
Iphone.make_a_call(2433534)
print(f'Valor do {Iphone._brand}{Iphone._model_name} é {Iphone._price}')
print(vars(Iphone))