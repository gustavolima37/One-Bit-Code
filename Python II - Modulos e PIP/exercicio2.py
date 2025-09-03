'''
Agendamento de desligamento
Crie duas funções em python para agendar o desligamento 
do computador em uma hora e meia hora.
'''
import os

# Windowns
# desligar o pc em 1 hora
def desligarPC_1h(systema):
    os.system('shutdown /s /t 3600')
    print('Seu PC irá desligar em 1 hora.')

'''
Exemplo: shutdown /s /t 60
shutdown: Inicia o comando de desligamento.
/s: Ação é desligar a máquina.
/t 60: Tempo de espera de 60 segundos antes de 
executar a ação.
Juntos, esses componentes criam uma instrução clara 
para o sistema: "Desligue a máquina em 60 segundos".
'''  

# desligar o pc em 30 minutos    
def desligarPC_30min(systema):
    os.system('shutdown /s /t 1800')
    print('Seu PC irá desligar em 30 minutos')
    
# abortar o desligamento    
def abortar_deslig(systema):
    os.system('shutdown /a')
    print('Abortando comando de desligar.')
    
# desligar em 1 minuto
def desligarPC_1min(systema):
    os.system('shutdown /s')
    print('Seu PC irá desligar em 1minuto')
    
# Linux
# Desligar o PC
os.system("sudo shutdown now")    