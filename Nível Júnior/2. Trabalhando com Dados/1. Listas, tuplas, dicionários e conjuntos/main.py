# Listas
# Listas são coleções ordenadas e mutáveis de elementos. Você pode armazenar diferentes tipos de dados em uma lista, incluindo números, strings e outras listas. Aqui está como trabalhar com listas:

# Criando uma lista
minha_lista = [1, 2, 3, "quatro", "cinco"]

# Acessando elementos da lista
primeiro_elemento = minha_lista[0]  # índice 0
segundo_elemento = minha_lista[1]  # índice 1

# Modificando elementos
minha_lista[3] = "4"  # Alterando o quarto elemento

# Adicionando elementos
minha_lista.append(6)  # Adicionando o número 6 ao final

# Removendo elementos
del minha_lista[1]  # Removendo o segundo elemento

# Verificando o comprimento da lista
tamanho = len(minha_lista)

# Tuplas
# Tuplas são semelhantes a listas, mas são imutáveis, o que significa que você não pode modificar seus elementos depois de criá-los. Elas são úteis quando você deseja garantir que os dados não mudem.

# Criando uma tupla
minha_tupla = (1, 2, 3, "quatro", "cinco")

# Acessando elementos da tupla
primeiro_elemento = minha_tupla[0]  # índice 0
segundo_elemento = minha_tupla[1]  # índice 1

# Dicionários
# Dicionários são coleções não ordenadas de pares chave-valor. Cada elemento em um dicionário tem uma chave única associada a um valor.

# Criando um dicionário
meu_dicionario = {"nome": "Alice", "idade": 30, "cidade": "São Paulo"}

# Acessando valores por chave
nome = meu_dicionario["nome"]
idade = meu_dicionario["idade"]

# Modificando valores
meu_dicionario["cidade"] = "Rio de Janeiro"

# Adicionando novos pares chave-valor
meu_dicionario["profissão"] = "Engenheiro"

# Removendo pares chave-valor
del meu_dicionario["idade"]

# Conjuntos
# Conjuntos são coleções desordenadas de elementos únicos. Eles são úteis para verificar a existência de elementos exclusivos ou para operações de conjuntos.

# Criando um conjunto
meu_conjunto = {1, 2, 3, 4, 5}

# Adicionando elementos
meu_conjunto.add(6)

# Removendo elementos
meu_conjunto.remove(3)

# Verificando a existência de elementos
existe_4 = 4 in meu_conjunto

# Cada uma dessas estruturas de dados tem seus usos específicos em Python. As listas são versáteis e mutáveis, as tuplas são imutáveis, os dicionários são úteis para mapear chaves a valores e os conjuntos são ótimos para elementos únicos e operações de conjuntos. Experimente criar e manipular essas estruturas de dados em seu ambiente Python para se familiarizar com elas.
