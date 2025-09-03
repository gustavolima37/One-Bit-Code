'''
1- Nessa aula vamos aprender a utilizar o módulo HttpServer no Python.

2- Esse módulo é muito legal, pois podemos compartilhar arquivos 
(imagens, código-fonte, músicas, vídeos, etc) entre diferentes máquinas, 
por meio de um servidor Http.

3- No meu caso, farei uma simulação entre a comunicação de arquivos 
entre minha máquina física e uma máquina virtual.

4- Você poderia fazer o teste entre a sua máquina física e um celular, 
ou um outro computador que esteja conectado na mesma rede.

5- Para iniciar o servidor http, digite o comando no terminal: python -m http.server
para encerrar o processo do servidor: ctrl + c
ou no cmd: netstat -ano | findstr ":8000"
- Abra na pasta que deseja ser compartilhada.

no cmd: ipconfig, seu ipv4 é o seu ip, no final dele coloca :8000
'''