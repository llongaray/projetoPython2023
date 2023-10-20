# Familiaridade com Bibliotecas Padrão em Python
# Python possui uma rica coleção de bibliotecas padrão que fornecem funcionalidades úteis para tarefas comuns. Vamos explorar a familiaridade com algumas delas.

# Biblioteca math
# A biblioteca math fornece funções matemáticas para operações avançadas. Você pode usar funções como sqrt, sin, cos, e muito mais.
import math

# Calcular a raiz quadrada
raiz_quadrada = math.sqrt(25)
print(f"Raiz quadrada de 25: {raiz_quadrada}")

# Calcular o seno e o cosseno
seno = math.sin(math.radians(45))
cosseno = math.cos(math.radians(60))
print(f"Seno de 45 graus: {seno}")
print(f"Cosseno de 60 graus: {cosseno}")

# Biblioteca random
# A biblioteca random é usada para gerar números aleatórios. Você pode criar números aleatórios inteiros, escolher elementos aleatórios de uma sequência e muito mais.
import random

# Gerar um número aleatório entre 1 e 100
numero_aleatorio = random.randint(1, 100)
print(f"Número aleatório entre 1 e 100: {numero_aleatorio}")

# Escolher um elemento aleatório de uma lista
lista = ["Maçã", "Banana", "Laranja", "Pera"]
elemento_aleatorio = random.choice(lista)
print(f"Elemento aleatório da lista: {elemento_aleatorio}")

# Biblioteca datetime
# A biblioteca datetime permite trabalhar com datas e horas. Você pode criar objetos de data e hora, formatá-los e realizar operações com datas.
from datetime import datetime

# Obter a data e hora atual
data_hora_atual = datetime.now()
print(f"Data e hora atuais: {data_hora_atual}")

# Formatar uma data
data_formatada = data_hora_atual.strftime("%d/%m/%Y %H:%M:%S")
print(f"Data formatada: {data_formatada}")

# Realizar operações com datas
from datetime import timedelta

data_atual = datetime.now()
um_dia = timedelta(days=1)
data_futura = data_atual + um_dia
print(f"Data futura: {data_futura}")

# Essas são apenas algumas das bibliotecas padrão em Python. Você pode explorar a documentação oficial do Python para obter mais informações sobre essas e outras bibliotecas disponíveis.
