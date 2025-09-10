import re

def from_text(string):
    #item = re.findall('é \w*', string) versão antiga
    item = re.findall(r'é \w*', string) # versão nova com r'' (raw string ou string bruta)
    return item[0][2:]

print(from_text('Meu video game é WiiU e o preço é 1000 reais'))