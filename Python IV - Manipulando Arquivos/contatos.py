class Contato:
    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero
        
    def __str__(self):
        return f'Nome: {self.nome} - Número: {self.numero}'
    
class AgendaContato:
    def __init__(self, arquivo_csv='contatos.csv'):
        self.contatos = []
        with open(arquivo_csv, 'r', encoding='utf-8') as file:
            for line in file:
                dados = line.strip().split(',')
                nome, numero = dados
                contato = Contato(nome, numero)
                self.contatos.append(contato)
     
    def adicionar_contato(self, contato):
        self.contatos.append(contato)
        print(f'Contato -> {contato.nome} adicionado com sucesso.')
        
    def deletar_contato(self, contato):
        self.contatos.remove(contato)
        print(f'Contato -> {contato.nome} foi deletado.')
                    
    def listar_contatos(self):
        print('---------- Lista de Contatos ----------')
        if not self.contatos:
            print('Nenhum contato encontrado na agenda.')
            return
        for contato in self.contatos:
            print(contato)
        print('---------------------------------------')