# Bibliotecas e Módulos Básicos em Python
# Python é conhecido por sua ampla coleção de bibliotecas e módulos que fornecem funcionalidades adicionais. Você pode importar essas bibliotecas e módulos em seu código para aproveitar esses recursos. Aqui estão alguns exemplos:

# Importando um módulo
import math

# Usando funções do módulo math
valor = math.sqrt(16)  # Calcula a raiz quadrada de 16
seno = math.sin(math.radians(30))  # Calcula o seno de 30 graus
print(f"Raiz quadrada de 16: {valor}")
print(f"Seno de 30 graus: {seno}")

# Você também pode importar módulos específicos de uma biblioteca
from datetime import datetime

# Usando funções do módulo datetime
agora = datetime.now()  # Obtém a data e hora atuais
ano = agora.year  # Obtém o ano atual
print(f"Data e hora atuais: {agora}")
print(f"Ano atual: {ano}")

# Apelidos (aliases) para módulos
# Você pode criar apelidos para módulos para tornar seu uso mais conveniente
import random as rd

# Usando funções do módulo random com apelido
numero_aleatorio = rd.randint(1, 10)  # Gera um número aleatório entre 1 e 10
print(f"Número aleatório: {numero_aleatorio}")

# Importando todos os nomes do módulo
# Você pode importar todos os nomes de um módulo, mas tenha cuidado, pois isso pode criar conflitos de nomes no seu código.
from random import *

# Usando funções do módulo random diretamente (sem prefixo)
numero_aleatorio2 = randint(1, 10)
print(f"Número aleatório 2: {numero_aleatorio2}")

# Bibliotecas padrão
Python possui uma rica biblioteca padrão que oferece uma ampla variedade de módulos para tarefas comuns, como manipulação de dados, comunicação de rede, expressões regulares, etc. Você pode explorar a documentação oficial do Python para obter informações sobre esses módulos e suas funcionalidades.

# À medida que você desenvolve em Python, você descobrirá bibliotecas específicas para atender às suas necessidades, como NumPy para computação numérica, pandas para análise de dados, Django para desenvolvimento web e muito mais. A importação de módulos e bibliotecas é uma parte fundamental do desenvolvimento em Python.
