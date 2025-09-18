class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
        
class ContactBook:   
    def __init__(self):
        self.contacts = []
    
    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f'Contato {contact.name} adicionado com sucesso.')
    
    def list_contacts(self):
        if not self.contacts:
            print('A agenda de contatos está vazia.')
            return
        print('\n--- Lista de Contatos ---')
        for contact in self.contacts:
            print(f'Nome: {contact.name},\nTelefone: {contact.phone},\nEmail: {contact.email}')
    
    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print('\n--- Contato Encontrado ---')
                print(f'Nome: {contact.name},\nelefone: {contact.phone},\nEmail: {contact.email}')
                return contact
            else:
                print(f'Contato com o nome {name} não encontrado.')
                return None
    
    def remove_contact(self, name):
        contact_to_remove = self.search_contact(name)
        if contact_to_remove:
            self.contacts.remove(contact_to_remove)
            print(f'Contato com o nome {name} removido com sucesso.')
        else:
            print(f'Não foi possivel remover, contato com o nome {name} não encontrado.')