def my_decorator(func):
    def wrapper():
        print('Antes de executar a função')
        func()
        print('Depois de executar a função')
    return wrapper

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

def split_string(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string
    return wrapper

'''
Um decorator permite adicionar um comportamento a um objeto já existente em tempo
de execução, ou seja, agrega dinamicamente responsabilidades adicionais a um objeto.
'''