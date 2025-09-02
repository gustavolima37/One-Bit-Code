name = input('Digite o nome do jogo\n')
yearLaunch = int(input('Digite o ano de lançamento do jogo\n'))
gamePrince = float(input('Digite o preço do jogo\n')) 
planIncluded = input('Está incluso no serviço mensal?\n')

print("###Dados do Jogo###")
print("===================")
# Alternativa 1 print multiplos
# print("Nome do Jogo:", name)
# print("Ano do Jogo:", yearLaunch)
# print("Preço do Jogo:", gamePrince)
# print("Está incluído no plano?", planIncluded)

# Alternativa 2 print unico
# print("Nome do Jogo:", name, "\nAno do lançamento:", yearLaunch,
#       "\nPreço do Jogo:", gamePrince, "\nEstá incluso no serviço?", planIncluded)

# Alternativa 3 f string (formatada)
print(f"Nome do Jogo: {name} \nAno de lançamento: {yearLaunch} \nPreço do Jogo: {gamePrince} \nEstá incluso no serviço? {planIncluded}")