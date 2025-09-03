'''
Nessa aula vamos aprender a utilizar o módulo hashlib 
na linguagem Python.
Modulo de criptografia.
Este módulo é utilizado para criptografar mensagens de 
texto, podendo aplicá-los a diferentes algoritmos, 
como o md5 e sha256.
'''

import hashlib

# 1 - Verificar os algoritmos disponiveis
print(hashlib.algorithms_available)

# 2 - Algoritmos disponiveis de acordo com o SO
print(hashlib.algorithms_guaranteed)

# 3 - Utilizando o Sha256 (mais atual)
algorithm = hashlib.sha256() 
print(algorithm.digest())
message = 'A melhor forma de prever o futuro é cria-lo'.encode()
algorithm.update(message)
print(algorithm.hexdigest())

'''
Explicação: 
Linha 1: algorithm = hashlib.sha256()
O que faz: Cria uma nova instância de um objeto de hash usando o algoritmo SHA-256. 
Pense nesse objeto como uma "calculadora de hash" vazia, pronta para receber dados.

Linha 2: print(algorithm.digest())
O que faz: Solicita o valor do hash do que foi processado até o momento. 
Como nada foi processado ainda (o objeto foi recém-criado), ele retorna o hash de uma string vazia.

Formato: O método digest() retorna o valor do hash em formato de bytes. 
A saída será uma sequência de bytes difícil de ler, como b'\xe3\xb0\xc4B....

Linha 3: message = 'A melhor forma de prever o futuro é cria-lo'.encode()
O que faz: Converte a string de texto em uma sequência de bytes. Como vimos antes, 
as funções de hash não trabalham com caracteres, mas sim com dados brutos (bytes). 
Essa linha prepara o texto para ser processado pelo algoritmo de hash.

Linha 4: algorithm.update(message)
O que faz: Esta é a linha mais importante. Ela "alimenta" a mensagem (agora em formato de bytes) 
para o objeto de hash. O algoritmo SHA-256 processa esses bytes e atualiza seu estado interno para calcular o hash final.

Linha 5: print(algorithm.hexdigest())
O que faz: Solicita o valor do hash novamente, mas desta vez, após a mensagem ter sido processada.

Formato: O método hexdigest() é mais fácil de usar, pois retorna o hash como uma string de caracteres hexadecimais. 
É o formato mais comum de hash que você vê por aí, com 64 caracteres.
'''

# 4 - Utilizando o MD5 (mais antigo)
md5 = hashlib.md5()
md5.update(message)
print(md5.hexdigest())

'''
IMPORTANTE: 
Abaixo, estão 5 das criptografias (ou, mais corretamente, 
funções de hash criptográficas) mais comuns do módulo hashlib, 
com um breve resumo de cada uma.

As 5 Funções de Hash Mais Usadas
SHA-256: Esta é a mais recomendada e amplamente utilizada hoje. 
Ela faz parte da família SHA-2 e gera um hash de 256 bits (64 caracteres hexadecimais). 
É o algoritmo usado em tecnologias como o Bitcoin e em muitos sistemas de segurança para 
verificar a integridade de dados e proteger senhas.

SHA-512: Também da família SHA-2, o SHA-512 gera um hash de 512 bits (128 caracteres hexadecimais). 
É mais lento, mas pode ser mais rápido em sistemas de 64 bits. É uma excelente alternativa ao SHA-256 
quando você precisa de um hash mais longo.

SHA-3 (ex: SHA3-256): Considerado a próxima geração de algoritmos de hash. 
O SHA-3 não é uma versão aprimorada do SHA-2, mas sim um design completamente novo. 
Ele foi desenvolvido como um "plano B" caso alguma falha fosse encontrada no SHA-2, 
mas hoje é visto como uma alternativa moderna e segura.

MD5:
⚠️ AVISO IMPORTANTE: Não use para segurança!
O MD5 é historicamente muito importante e ainda é usado para verificar a integridade de arquivos (como um checksum), 
mas é considerado criptograficamente quebrado. Isso significa que é relativamente fácil 
encontrar duas entradas diferentes que geram o mesmo hash. Nunca use MD5 para proteger senhas ou dados sensíveis.

SHA-1:
⚠️ AVISO IMPORTANTE: Não use para segurança!
Assim como o MD5, o SHA-1 foi amplamente utilizado no passado. No entanto, hoje é considerado inseguro e 
vulnerável a ataques de colisão. Ele foi removido de muitos navegadores e sistemas de segurança. 
Use apenas para manter a compatibilidade com sistemas legados, e não para novas aplicações.
'''