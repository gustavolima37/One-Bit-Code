teams = {}
done = False

# função para listar times
def print_teams():
    print("Times Listados:")
    for i, team in enumerate(teams.values()):
        print(f"{i+1}. {team['name']} ({len(team['players'])} jogadores)")

# função para listar jogadores de um time
def print_team_players(team):
    print(f"Jogadores do {team['name']}")
    for i, player in enumerate(team['players']):
        print(f"{i+1}. {player}")

while not done:
    # Opções no programa
    print("O que você deseja fazer?")
    print("1. Adicionar um time")
    print("2. Remover um time")
    print("3. Listar times")
    print("4. Adicionar jogador em um time")
    print("5. Remover jogador em um time")
    print("6. Listar jogadores de um time")
    print("7. Sair")
    
    choice = input(">")
    if choice =="1":
        team_name = input("Digite o nome do time:\n")
        teams[team_name] = {'name': team_name, 'players': []}
        print("Time adicionado.")
    elif choice == "2":
        if len(teams) == 0:
            print("Não há times para serem removidos.")
        else:
            print_teams()
            team_num = int(input("Informe o número do time que deseja remover:\n"))
            if team_num <= len(teams):
                team_name = list(teams.keys())[team_num - 1]
                del teams[team_name]
                print("Time removido.")
            else:
                print("Número do time inválido!")
    elif choice =="3":
        print_teams()
    elif choice =="4":
        print_teams()
        team_num = int(input("Informe o número do time que deseja adicionar o jogador:\n"))
        if team_num <= len(teams):
            team_name = list(teams.keys())[team_num -1]
            player_name = input("Informe o nome do jogador:\n")
            teams[team_name]['players'].append(player_name)
            print("Jogador adicionado no time!")
        else:
            print("Número do time esta inválido!!")
    elif choice =="5":
        print_teams()
        team_num = int(input("Informe o número do time que deseja remover o jogador:\n"))
        if team_num <= len(teams):
            team_name = list(teams.keys())[team_num -1]
            print_team_players(teams[team_name])
            player_num = int(input("Informe o número do jogador que deseja remover\n"))
            if player_num <= len(teams[team_name]['players']):
                del teams[team_name]['players'][player_num -1]
                print("Jogador removido do time")
            else:
                print("Número do jogador inválido!")
        else: 
            print("Número do time inválido!")
            
    elif choice =="6":
        print_teams()
        team_num = int(input("Informe o número do time que deseja listar o jogadores:\n"))
        if team_num <= len(teams):
            team_name = list(teams.keys())[team_num -1]
            if len(teams[team_name]) == 0:
                print("Não há jogadores no time.")
            else:
                print_team_players(teams[team_name])
        else:
            print("Número do time inválido!")
    elif choice =="7":
        done = True
    else:
        print("Opção inválida")