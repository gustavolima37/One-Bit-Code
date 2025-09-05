'''
- Nessa aula vamos aprender a criar um ambiente virtual de desenvolvimento na linguagem Python.
- A principal vantagem de ter um ambiente virtual de desenvolvimento, 
é que isolamos as bibliotecas que serão utilizadas em um projeto, 
o que vai facilitar bastante quando se quiser fazer o deploy de um projeto.
- Em nosso caso, o deploy do aplicativo será a geração do arquivo instalador da aplicação do Tkinter. 
Por isso, vamos nos certificar de que apenas as bibliotecas necessárias sejam utilizadas no projeto.
- Para criar o ambiente virtual de desenvolvimento, pode-se executar o comando no terminal: python -m venv .venv
- Estamos indicando que vamos criar um diretório .venv, que vai ser o diretório que armazenará as 
bibliotecas que instalarmos nesse ambiente de desenvolvimento.
- Para ativar o ambiente virtual de desenvolvimento, pode ser executado o comando: ./.venv/Scripts/activate


para voltar a pasta Python II, no terminal colocar 'cd ..' ate voltar pra pasta Python II

Como usar o comando deactivate
- No terminal, certifique-se de que a linha de comando ainda tem o prefixo (.venv).
- Digite deactivate e pressione Enter.
- Depois de executar o comando, o prefixo (.venv) desaparecerá, 
indicando que o ambiente virtual está desativado.

'''