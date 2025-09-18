from agenda_contatos import Contact, ContactBook

# --- ARQUIVO PRINCIPAL ---
if __name__ == '__main__':
    agenda = ContactBook() 

while True:
    print('\n--- Menu da Agenda de Contatos ---')
    print('1. Adicionar contato')
    print('2. Listar contatos')
    print('3. Buscar contato')
    print('4. Remover contato')
    print('5. Sair')
    
    escolha = input('Esconta uma opção: ')
    
    if escolha == '1':
        name = input('Nome do contato: ')
        phone = input('Teleone do contato: ')
        email = input('Email do contato: ')
        novo_contato = Contact(name, phone, email)
        agenda.add_contact(novo_contato)
    
    elif escolha == '2':
        agenda.list_contacts()
        
    elif escolha == '3':
        name = input('Digite o nome do contato para buscar: ')
        agenda.search_contact(name)
    
    elif escolha == '4':
        name = input('Digite o nome do contato para remover: ')
        agenda.remove_contact(name)
        
    elif escolha == '5':
        print('Saindo da agenda de contatos.')
        break
    else:
        print('Opção inválida. Por favor, tente novamente.')