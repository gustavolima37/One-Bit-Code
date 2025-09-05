'''
Nessa aula vamos aprender alguns comandos utilitários do Pip.
Bem, o primeiro comando que temos de importante do pip, é o pip list. 
Esse comando vai nos ajudar a listar as bibliotecas que estão instaladas no projeto.


Note que foram listadas apenas duas bibliotecas, 
que são bibliotecas utilitárias para o funcionamento do ambiente virtual de desenvolvimento.
Um comando muito útil é o pip install. Ele serve para instalar bibliotecas. 
Vamos experimentar instalando a biblioteca pyinstaller, com o comando: pip install pyinstaller


Outro comando bem útil também, é o pip freeze. 
Esse comando retorna o resultado com um formato pronto para que possamos copiar 
as bibliotecas e versões e instalar com o pip.


Por último, poderíamos adicionar o resultado anterior para um arquivo .txt, 
que vai ficar responsável pela listagem das bibliotecas, bem como de suas versões. 
Podemos usar esse comando: pip freeze -l > requirements.txt.
Agora que temos a informação pronta no arquivo requirements.txt, 
é só executar o comando pip install -r requirements.txt e todas as bibliotecas serão instaladas.


pip list
pip install
pip freeze (mostrar informação da versão da biblioteca)

pip freeze -l > requirements.txt
'''