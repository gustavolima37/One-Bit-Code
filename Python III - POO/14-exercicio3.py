from exercicio3_trip import Trip

trip_0 = Trip('Lençois Maranhense')
trip_1 = Trip('Florianópolis')
trip_2 = Trip('Gramado')
trip_3 = Trip('Campos do Jordão')
trip_4 = Trip('Caldas Novas')

print('E ai viajante, Temos algumas ofertas para você.')
viajante = input('Digite seu nome para começar: \n')
print(f"{viajante} Temos 5 destinos que combinam com vc:"
      '''
      [0] - Lençois Maranhense
      [1] - Florianópolis
      [2] - Gramado
      [3] - Campos do Jordão
      [4] - Caldas Novas
      
      ''')

escolha = int(input('Selecione o destino da viagem: \n'))
list_trip = [trip_0, trip_1, trip_2, trip_3, trip_4]

for opcao in list_trip:
    if escolha >= 5:
        print('Esta opção não esta inclusa em nossos destinos.')
        break
    else:
        print(f'{viajante} sua viagem para {list_trip[escolha].destino} esta marcada!')
        print('Boa Viajem!')
        break